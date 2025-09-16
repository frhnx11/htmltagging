#!/usr/bin/env python3
"""
Question Processor - Handle reading questions from Excel and updating with classifications
"""

import pandas as pd
import json
import os
import logging
from typing import List, Dict, Optional, Tuple
from datetime import datetime
import numpy as np
from config import get_config
from taxonomy_constants import get_taxonomy_metadata

class QuestionProcessor:
    def __init__(self):
        self.config = get_config()
        self.paths = self.config["paths"]
        self.processing_config = self.config["processing"]
        self.validation_config = self.config["validation"]
        
        # Setup logging
        logging.basicConfig(
            level=getattr(logging, self.config["logging"]["level"]),
            format=self.config["logging"]["format"]
        )
        self.logger = logging.getLogger(__name__)
        
        # Progress tracking
        self.progress = {
            "total_questions": 0,
            "processed_questions": 0,
            "successful_classifications": 0,
            "failed_classifications": 0,
            "skipped_questions": 0,
            "start_time": None,
            "last_saved": None,
            "current_batch": 0,
            "resume_from": 0
        }
        
        # Taxonomy data
        self.taxonomy_data = None
        self.taxonomy_options = []
        
    def load_taxonomy_data(self) -> bool:
        """Load taxonomy data from pre-initialized constants"""
        try:
            # Use pre-initialized taxonomy constants for maximum efficiency
            taxonomy_metadata = get_taxonomy_metadata()
            self.taxonomy_options = taxonomy_metadata["all_paths"]
            self.taxonomy_data = taxonomy_metadata
            
            self.logger.info(f"Loaded pre-initialized taxonomy with {len(self.taxonomy_options)} classification options")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load taxonomy constants: {e}")
            return False
    
    def validate_question(self, question: str) -> bool:
        """Validate if a question should be processed"""
        if not question or pd.isna(question):
            return False
        
        question = str(question).strip()
        
        if self.validation_config["skip_empty_questions"] and not question:
            return False
        
        if len(question) < self.validation_config["min_question_length"]:
            return False
        
        return True
    
    def load_questions_file(self) -> Optional[pd.DataFrame]:
        """Load the questions Excel file"""
        try:
            if not os.path.exists(self.paths["questions_file"]):
                self.logger.error(f"Questions file not found: {self.paths['questions_file']}")
                return None
            
            self.logger.info(f"Loading questions from: {self.paths['questions_file']}")
            df = pd.read_excel(self.paths["questions_file"])
            
            self.logger.info(f"Loaded {len(df)} questions")
            self.logger.info(f"Columns: {list(df.columns)}")
            
            # Ensure required columns exist
            required_columns = ['Question with Statements', 'Subject', 'Topic', 'Subtopic']
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                self.logger.error(f"Missing required columns: {missing_columns}")
                return None
            
            self.progress["total_questions"] = len(df)
            return df
            
        except Exception as e:
            self.logger.error(f"Failed to load questions file: {e}")
            return None
    
    def load_progress(self) -> bool:
        """Load progress from previous session"""
        if not self.processing_config["resume_enabled"]:
            return False
        
        try:
            if os.path.exists(self.paths["progress_file"]):
                with open(self.paths["progress_file"], 'r') as f:
                    saved_progress = json.load(f)
                
                # Update progress with saved data
                for key in ["processed_questions", "successful_classifications", 
                           "failed_classifications", "skipped_questions", "resume_from"]:
                    if key in saved_progress:
                        self.progress[key] = saved_progress[key]
                
                self.logger.info(f"Resumed from previous session: {self.progress['processed_questions']}/{self.progress['total_questions']} questions processed")
                return True
                
        except Exception as e:
            self.logger.warning(f"Could not load previous progress: {e}")
        
        return False
    
    def save_progress(self):
        """Save current progress"""
        try:
            self.progress["last_saved"] = datetime.now().isoformat()
            
            with open(self.paths["progress_file"], 'w') as f:
                json.dump(self.progress, f, indent=2)
                
            self.logger.debug("Progress saved")
            
        except Exception as e:
            self.logger.warning(f"Could not save progress: {e}")
    
    def validate_classification(self, classification: Dict) -> bool:
        """Validation for two-stage classification (subject + topic)"""
        if not classification or not isinstance(classification, dict):
            self.logger.error("Classification is not a valid dictionary")
            return False
        
        required_fields = ["subject", "confidence"]
        if not all(field in classification for field in required_fields):
            self.logger.error(f"Missing required fields. Got: {list(classification.keys())}")
            return False
        
        # Get subject from classification
        subject = str(classification["subject"]).strip()
        topic = str(classification.get("topic", "")).strip()
        
        # Valid subjects list (updated with all current taxonomy subjects)
        valid_subjects = [
            "ANCIENT HISTORY",
            "ART AND CULTURE", 
            "Aptitude",
            "ECONOMY",
            "ENVIRONMENT",
            "English",
            "GOVERNANCE",
            "INDIAN PHYSICAL GEOGRAPHY",
            "INDIAN SOCIO-ECONOMIC GEOGRAPHY",
            "INTERNATIONAL BODIES & ORGANISATIONS",
            "MEDIEVAL HISTORY",
            "MODERN INDIA",
            "POLITY",
            "Reasoning",
            "SCIENCE AND TECHNOLOGY",
            "WORLD PHYSICAL GEOGRAPHY",
            "WORLD SOCIO-ECONOMIC GEOGRAPHY"
        ]
        
        # Check if subject is valid
        if subject not in valid_subjects:
            self.logger.error(f"INVALID subject: '{subject}' not in valid subjects")
            self.logger.error(f"Valid subjects: {valid_subjects}")
            return False
        
        # If topic is provided, validate it exists for this subject
        if topic:
            # Get valid topics for this subject
            subject_topics = []
            for option in self.taxonomy_options:
                if option.startswith(f"{subject} > "):
                    option_topic = option.split(" > ")[1]  # Get topic part
                    if option_topic not in subject_topics:
                        subject_topics.append(option_topic)
            
            if topic not in subject_topics:
                # Try to find a close match for topics too
                closest_topic_match = None
                for valid_topic in subject_topics:
                    # Check if they're very similar
                    if (topic.lower().replace(' ', '') == valid_topic.lower().replace(' ', '') or
                        abs(len(topic) - len(valid_topic)) <= 2 and 
                        sum(c1 != c2 for c1, c2 in zip(topic.lower(), valid_topic.lower())) <= 2):
                        closest_topic_match = valid_topic
                        break
                
                if closest_topic_match:
                    self.logger.warning(f"FUZZY MATCH: LLM returned topic '{topic}', using closest match '{closest_topic_match}'")
                    # Update the classification with the exact match
                    classification["topic"] = closest_topic_match
                    topic = closest_topic_match  # Update local variable for subtopic validation
                else:
                    self.logger.error(f"INVALID topic: '{topic}' not found for subject '{subject}'")
                    self.logger.error(f"Valid topics for {subject}: {subject_topics[:5]}...")
                    return False
        
        # If subtopic is provided, validate it exists for this subject > topic combination
        subtopic = str(classification.get("subtopic", "")).strip()
        if subtopic and topic:
            # Get valid subtopics for this subject > topic combination
            subject_topic_subtopics = []
            for option in self.taxonomy_options:
                if option.startswith(f"{subject} > {topic} > "):
                    option_subtopic = option.split(" > ")[2]  # Get subtopic part
                    if option_subtopic not in subject_topic_subtopics:
                        subject_topic_subtopics.append(option_subtopic)
            
            if subtopic not in subject_topic_subtopics:
                # Try to find a close match (for cases like "Substances" vs "Subtrances")
                closest_match = None
                for valid_subtopic in subject_topic_subtopics:
                    # Check if they're very similar (allowing for minor typos/spelling differences)
                    if (subtopic.lower().replace(' ', '') == valid_subtopic.lower().replace(' ', '') or
                        abs(len(subtopic) - len(valid_subtopic)) <= 2 and 
                        sum(c1 != c2 for c1, c2 in zip(subtopic.lower(), valid_subtopic.lower())) <= 2):
                        closest_match = valid_subtopic
                        break
                
                if closest_match:
                    self.logger.warning(f"FUZZY MATCH: LLM returned '{subtopic}', using closest match '{closest_match}'")
                    # Update the classification with the exact match
                    classification["subtopic"] = closest_match
                else:
                    self.logger.error(f"INVALID subtopic: '{subtopic}' not found for '{subject} > {topic}'")
                    self.logger.error(f"Valid subtopics for {subject} > {topic}: {subject_topic_subtopics[:5]}...")
                    return False
        
        self.logger.debug(f"VALID classification: Subject='{subject}', Topic='{topic}', Subtopic='{subtopic}'")
        return True
    
    def apply_classification(self, df: pd.DataFrame, row_index: int, classification: Dict) -> bool:
        """Apply classification to a DataFrame row"""
        try:
            if not classification:
                return False
            
            # Validate classification first
            if not self.validate_classification(classification):
                return False
            
            # Check confidence threshold
            confidence = classification.get("confidence", 0)
            if confidence < self.config["prompt"]["confidence_threshold"]:
                self.logger.debug(f"Classification confidence {confidence} below threshold {self.config['prompt']['confidence_threshold']}")
                return False
            
            # Apply two-stage classification results
            df.at[row_index, 'Subject'] = classification["subject"]
            
            # Apply topic if available
            if classification.get("topic"):
                df.at[row_index, 'Topic'] = classification["topic"]
            
            # Apply subtopic if available
            if classification.get("subtopic"):
                df.at[row_index, 'Subtopic'] = classification["subtopic"]
            
            # Store confidence and reasoning
            if 'Confidence' in df.columns:
                df.at[row_index, 'Confidence'] = confidence
            if 'Reasoning' in df.columns and 'reasoning' in classification:
                df.at[row_index, 'Reasoning'] = classification["reasoning"]
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to apply classification to row {row_index}: {e}")
            return False
    
    def apply_fallback_classification(self, df: pd.DataFrame, row_index: int):
        """Apply fallback classification when LLM fails - REMOVED: No fallbacks allowed"""
        raise Exception(f"Classification failed for row {row_index}. No fallback classifications allowed.")
    
    def prepare_questions_batch(self, df: pd.DataFrame, start_idx: int, batch_size: int) -> List[Dict]:
        """Prepare a batch of questions for classification"""
        end_idx = min(start_idx + batch_size, len(df))
        batch = []
        
        for i in range(start_idx, end_idx):
            question_text = df.iloc[i]['Question with Statements']
            
            if self.validate_question(question_text):
                # Check if already classified
                if (pd.notna(df.iloc[i]['Subject']) and 
                    str(df.iloc[i]['Subject']).strip() and 
                    str(df.iloc[i]['Subject']).strip() != self.config["prompt"]["fallback_subject"]):
                    # Skip already classified questions
                    continue
                
                # Build the full question with options
                full_question = str(question_text).strip()
                
                # Add options if they exist
                options = []
                for opt in ['A', 'B', 'C', 'D', 'E']:
                    opt_col = f'Option {opt}'
                    if opt_col in df.columns and pd.notna(df.iloc[i][opt_col]):
                        option_text = str(df.iloc[i][opt_col]).strip()
                        if option_text:
                            options.append(f"{opt}) {option_text}")
                
                if options:
                    full_question += "\n\nOptions:\n" + "\n".join(options)
                
                batch.append({
                    'index': i,
                    'question': full_question[:self.validation_config["max_question_length"]]
                })
        
        return batch
    
    def save_results(self, df: pd.DataFrame, backup: bool = False):
        """Save the updated DataFrame to Excel"""
        try:
            output_file = self.paths["output_file"]
            if backup:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_file = output_file.replace(".xlsx", f"_backup_{timestamp}.xlsx")
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            # Save with formatting
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Questions', index=False)
                
                # Auto-adjust column widths
                worksheet = writer.sheets['Questions']
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    
                    adjusted_width = min(max_length + 2, 50)  # Cap at 50 characters
                    worksheet.column_dimensions[column_letter].width = adjusted_width
            
            self.logger.info(f"Results saved to: {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to save results: {e}")
            return False
    
    def get_progress_summary(self) -> Dict:
        """Get current progress summary"""
        if self.progress["start_time"]:
            elapsed_time = (datetime.now() - datetime.fromisoformat(self.progress["start_time"])).total_seconds()
            questions_per_minute = (self.progress["processed_questions"] / elapsed_time * 60) if elapsed_time > 0 else 0
            eta_minutes = ((self.progress["total_questions"] - self.progress["processed_questions"]) / questions_per_minute) if questions_per_minute > 0 else 0
        else:
            elapsed_time = 0
            questions_per_minute = 0
            eta_minutes = 0
        
        return {
            "total_questions": self.progress["total_questions"],
            "processed_questions": self.progress["processed_questions"],
            "successful_classifications": self.progress["successful_classifications"],
            "failed_classifications": self.progress["failed_classifications"],
            "skipped_questions": self.progress["skipped_questions"],
            "success_rate": (self.progress["successful_classifications"] / self.progress["processed_questions"] * 100) if self.progress["processed_questions"] > 0 else 0,
            "elapsed_time_minutes": elapsed_time / 60,
            "questions_per_minute": questions_per_minute,
            "eta_minutes": eta_minutes,
            "completion_percentage": (self.progress["processed_questions"] / self.progress["total_questions"] * 100) if self.progress["total_questions"] > 0 else 0
        }

def main():
    """Test the question processor"""
    processor = QuestionProcessor()
    
    print("Testing Question Processor...")
    
    # Load taxonomy
    if processor.load_taxonomy_data():
        print(f"✅ Taxonomy loaded: {len(processor.taxonomy_options)} options")
    else:
        print("❌ Failed to load taxonomy")
        return
    
    # Load questions
    df = processor.load_questions_file()
    if df is not None:
        print(f"✅ Questions loaded: {len(df)} questions")
        
        # Test validation
        sample_question = df.iloc[0]['Question with Statements']
        is_valid = processor.validate_question(sample_question)
        print(f"✅ Question validation test: {'Valid' if is_valid else 'Invalid'}")
        
        # Test batch preparation
        batch = processor.prepare_questions_batch(df, 0, 3)
        print(f"✅ Batch preparation test: {len(batch)} questions in batch")
        
    else:
        print("❌ Failed to load questions")

if __name__ == "__main__":
    main()