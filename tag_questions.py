#!/usr/bin/env python3
"""
Main Question Tagging Script - Orchestrates the entire tagging process
"""

import os
import sys
import logging
import argparse
import signal
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from typing import List, Dict

from config import get_config, validate_config
# from taxonomy_loader import TaxonomyLoader  # No longer needed - using constants
from ollama_client import OllamaClient
from question_processor import QuestionProcessor

class QuestionTagger:
    def __init__(self, resume: bool = True, max_workers: int = None):
        self.config = get_config()
        self.resume_enabled = resume and self.config["processing"]["resume_enabled"]
        self.max_workers = max_workers or self.config["processing"]["max_concurrent"]
        
        # Setup logging
        self.setup_logging()
        self.logger = logging.getLogger(__name__)
        
        # Initialize components
        self.ollama_client = None
        self.question_processor = None
        # self.taxonomy_loader = None  # No longer needed - using constants
        
        # State management
        self.is_running = True
        self.pause_requested = False
        self.current_df = None
        
        # Statistics
        self.session_stats = {
            "session_start": datetime.now(),
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "batches_completed": 0,
            "errors": []
        }
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def setup_logging(self):
        """Setup logging configuration"""
        log_config = self.config["logging"]
        
        # Create logs directory
        log_dir = os.path.dirname(self.config["paths"]["error_log"])
        os.makedirs(log_dir, exist_ok=True)
        
        # Setup file handler
        file_handler = logging.FileHandler(self.config["paths"]["error_log"])
        file_handler.setLevel(getattr(logging, log_config["level"]))
        file_formatter = logging.Formatter(log_config["format"])
        file_handler.setFormatter(file_formatter)
        
        # Setup console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        
        # Configure root logger
        logging.basicConfig(
            level=getattr(logging, log_config["level"]),
            handlers=[file_handler, console_handler] if log_config["console_logging"] else [file_handler]
        )
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        self.logger.info(f"Received signal {signum}. Initiating graceful shutdown...")
        self.is_running = False
        self.save_progress()
    
    def initialize_components(self) -> bool:
        """Initialize all components using pre-initialized taxonomy"""
        try:
            # Initialize Question Processor with constants
            self.logger.info("Initializing question processor with pre-initialized taxonomy...")
            self.question_processor = QuestionProcessor()
            if not self.question_processor.load_taxonomy_data():
                self.logger.error("Failed to load taxonomy constants")
                return False
            
            # Initialize Ollama Client
            self.logger.info("Initializing Ollama client...")
            self.ollama_client = OllamaClient()
            if not self.ollama_client.check_ollama_status():
                self.logger.error("Ollama is not accessible")
                return False
            
            self.logger.info("All components initialized successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to initialize components: {e}")
            return False
    
    def load_questions(self) -> bool:
        """Load questions from Excel file"""
        try:
            self.current_df = self.question_processor.load_questions_file()
            if self.current_df is None:
                return False
            
            # Load progress if resuming
            if self.resume_enabled:
                self.question_processor.load_progress()
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load questions: {e}")
            return False
    
    def process_batch(self, batch_data: List[Dict]) -> List[Dict]:
        """Process a batch of questions"""
        if not batch_data:
            return []
        
        try:
            # Use batch processing if batch size > 1, otherwise single processing
            if len(batch_data) > 1:
                classifications = self.ollama_client.classify_batch_questions(
                    batch_data, 
                    self.question_processor.taxonomy_options
                )
            else:
                # Single question processing
                classification = self.ollama_client.classify_single_question(
                    batch_data[0]['question'],
                    self.question_processor.taxonomy_options
                )
                classifications = [classification]
            
            # Combine batch data with classifications
            results = []
            for i, (question_data, classification) in enumerate(zip(batch_data, classifications)):
                results.append({
                    'index': question_data['index'],
                    'question': question_data['question'],
                    'classification': classification
                })
            
            return results
            
        except Exception as e:
            self.logger.error(f"Failed to process batch: {e}")
            return [{'index': q['index'], 'question': q['question'], 'classification': None} for q in batch_data]
    
    def apply_results(self, results: List[Dict]):
        """Apply classification results to the DataFrame"""
        for result in results:
            row_index = result['index']
            classification = result['classification']
            
            if classification:
                if self.question_processor.apply_classification(self.current_df, row_index, classification):
                    self.session_stats["successful"] += 1
                    self.question_processor.progress["successful_classifications"] += 1
                    # Show real-time progress for successful classifications
                    subject = classification.get("subject", "")
                    topic = classification.get("topic", "")
                    subtopic = classification.get("subtopic", "")
                    print(f"✅ Question {row_index+1}: {subject} > {topic} > {subtopic}")
                else:
                    # Classification failed validation - REJECT the row completely
                    self.logger.error(f"Row {row_index}: Classification failed validation - SKIPPING")
                    self.session_stats["failed"] += 1
                    self.question_processor.progress["failed_classifications"] += 1
                    print(f"❌ Question {row_index+1}: Validation failed")
                    # Don't update the Excel - leave Subject/Topic/Subtopic empty for failed cases
            else:
                # No classification returned - REJECT the row completely  
                self.logger.error(f"Row {row_index}: No classification returned - SKIPPING")
                self.session_stats["failed"] += 1
                self.question_processor.progress["failed_classifications"] += 1
                print(f"❌ Question {row_index+1}: No classification returned")
                # Don't update the Excel - leave Subject/Topic/Subtopic empty for failed cases
            
            self.question_processor.progress["processed_questions"] += 1
            self.session_stats["total_processed"] += 1
            
            # Show progress every 10 questions
            if self.session_stats["total_processed"] % 10 == 0:
                processed = self.question_processor.progress["processed_questions"]
                total = self.question_processor.progress["total_questions"]
                successful = self.session_stats["successful"]
                print(f"📊 Progress: {processed}/{total} ({(processed/total)*100:.1f}%) | Success: {successful}/{processed} ({(successful/processed)*100:.1f}%)")
    
    def save_progress(self):
        """Save current progress and results"""
        try:
            # Save progress tracking
            self.question_processor.save_progress()
            
            # Save current results
            if self.current_df is not None:
                self.question_processor.save_results(self.current_df)
                
                # Create backup every hour
                current_time = datetime.now()
                if (hasattr(self, 'last_backup') and 
                    (current_time - self.last_backup).total_seconds() > 3600) or not hasattr(self, 'last_backup'):
                    self.question_processor.save_results(self.current_df, backup=True)
                    self.last_backup = current_time
            
            self.logger.info("Progress saved successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to save progress: {e}")
    
    def print_progress_report(self):
        """Print detailed progress report"""
        progress_summary = self.question_processor.get_progress_summary()
        ollama_stats = self.ollama_client.get_statistics()
        
        print(f"\n{'='*60}")
        print(f"PROGRESS REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        print(f"Questions: {progress_summary['processed_questions']:,} / {progress_summary['total_questions']:,} ({progress_summary['completion_percentage']:.1f}%)")
        print(f"Successful: {progress_summary['successful_classifications']:,} ({progress_summary['success_rate']:.1f}%)")
        print(f"Failed: {progress_summary['failed_classifications']:,}")
        print(f"Skipped: {progress_summary['skipped_questions']:,}")
        print(f"")
        print(f"Performance:")
        print(f"  Speed: {progress_summary['questions_per_minute']:.1f} questions/minute")
        print(f"  Elapsed: {progress_summary['elapsed_time_minutes']:.1f} minutes")
        print(f"  ETA: {progress_summary['eta_minutes']:.1f} minutes")
        print(f"")
        print(f"Ollama Stats:")
        print(f"  Model: {ollama_stats['current_model']}")
        print(f"  Success Rate: {ollama_stats['success_rate']:.1f}%")
        print(f"  Avg Response Time: {ollama_stats['average_response_time']:.2f}s")
        print(f"{'='*60}")
    
    def run(self) -> bool:
        """Main execution loop"""
        try:
            # Initialize components
            if not self.initialize_components():
                return False
            
            # Load questions
            if not self.load_questions():
                return False
            
            # Set start time if not resuming
            if not self.resume_enabled or not self.question_processor.progress.get("start_time"):
                self.question_processor.progress["start_time"] = datetime.now().isoformat()
            
            batch_size = self.config["processing"]["batch_size"]
            save_interval = self.config["processing"]["save_interval"]
            report_interval = self.config["performance"]["report_interval"]
            
            total_questions = len(self.current_df)
            start_from = self.question_processor.progress.get("resume_from", 0)
            
            self.logger.info(f"Starting processing from question {start_from + 1} of {total_questions}")
            
            # Process in batches
            processed_count = 0
            batch_futures = {}
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                current_pos = start_from
                
                while current_pos < total_questions and self.is_running:
                    # Prepare batch
                    batch = self.question_processor.prepare_questions_batch(
                        self.current_df, current_pos, batch_size
                    )
                    
                    if not batch:
                        current_pos += batch_size
                        continue
                    
                    # Submit batch for processing
                    future = executor.submit(self.process_batch, batch)
                    batch_futures[future] = batch
                    
                    # Process completed futures
                    completed_futures = [f for f in batch_futures.keys() if f.done()]
                    for future in completed_futures:
                        try:
                            results = future.result()
                            self.apply_results(results)
                            processed_count += len(results)
                            self.session_stats["batches_completed"] += 1
                        except Exception as e:
                            self.logger.error(f"Batch processing failed: {e}")
                            self.session_stats["errors"].append(str(e))
                        finally:
                            del batch_futures[future]
                    
                    # Progress reporting
                    if processed_count > 0 and processed_count % report_interval == 0:
                        self.print_progress_report()
                    
                    # Periodic saving
                    if processed_count > 0 and processed_count % save_interval == 0:
                        self.save_progress()
                    
                    current_pos += batch_size
                
                # Wait for remaining futures to complete
                for future in as_completed(batch_futures.keys()):
                    try:
                        results = future.result()
                        self.apply_results(results)
                        self.session_stats["batches_completed"] += 1
                    except Exception as e:
                        self.logger.error(f"Final batch processing failed: {e}")
                        self.session_stats["errors"].append(str(e))
            
            # Final save
            self.save_progress()
            
            # Final report
            self.print_progress_report()
            
            self.logger.info("Processing completed successfully!")
            return True
            
        except Exception as e:
            self.logger.error(f"Processing failed: {e}")
            self.save_progress()
            return False

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Tag questions using Ollama LLM")
    parser.add_argument("--no-resume", action="store_true", help="Start fresh (don't resume from previous session)")
    parser.add_argument("--workers", type=int, help="Number of concurrent workers")
    parser.add_argument("--validate-only", action="store_true", help="Only validate configuration")
    
    args = parser.parse_args()
    
    # Validate configuration
    print("Validating configuration...")
    errors = validate_config()
    if errors:
        print("Configuration errors found:")
        for error in errors:
            print(f"  ❌ {error}")
        return 1
    
    if args.validate_only:
        print("✅ Configuration is valid!")
        return 0
    
    print("✅ Configuration validated")
    
    # Initialize and run tagger
    tagger = QuestionTagger(
        resume=not args.no_resume,
        max_workers=args.workers
    )
    
    print(f"\n{'='*60}")
    print("QUESTION TAGGING SYSTEM STARTING")
    print(f"{'='*60}")
    print(f"Resume enabled: {'Yes' if tagger.resume_enabled else 'No'}")
    print(f"Max workers: {tagger.max_workers}")
    print(f"Batch size: {tagger.config['processing']['batch_size']}")
    print(f"Model: {tagger.config['ollama']['model']}")
    print(f"{'='*60}\n")
    
    success = tagger.run()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())