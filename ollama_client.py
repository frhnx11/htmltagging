#!/usr/bin/env python3
"""
Ollama Client - Handle interactions with Ollama API for question classification
"""

import json
import requests
import time
import logging
from typing import List, Dict, Optional, Tuple
import random
from config import get_config

class OllamaClient:
    def __init__(self):
        self.config = get_config()
        self.ollama_config = self.config["ollama"]
        self.fallback_models = self.config["fallback_models"]
        self.current_model = self.ollama_config["model"]
        
        # Setup logging
        logging.basicConfig(
            level=getattr(logging, self.config["logging"]["level"]),
            format=self.config["logging"]["format"]
        )
        self.logger = logging.getLogger(__name__)
        
        # Statistics
        self.stats = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "total_questions_processed": 0,
            "average_response_time": 0,
            "model_switches": 0
        }
    
    def check_ollama_status(self) -> bool:
        """Check if Ollama server is running and accessible"""
        try:
            response = requests.get(f"{self.ollama_config['host']}/api/tags", timeout=5)
            if response.status_code == 200:
                available_models = [model["name"] for model in response.json().get("models", [])]
                self.logger.info(f"Ollama is running. Available models: {available_models}")
                
                # Check if our preferred model is available
                if self.current_model not in available_models:
                    self.logger.warning(f"Preferred model '{self.current_model}' not found.")
                    # Try to find a fallback model
                    for model in self.fallback_models:
                        if model in available_models:
                            self.logger.info(f"Switching to fallback model: {model}")
                            self.current_model = model
                            self.stats["model_switches"] += 1
                            break
                    else:
                        self.logger.error("No suitable models found!")
                        return False
                
                return True
            else:
                self.logger.error(f"Ollama returned status code: {response.status_code}")
                return False
                
        except requests.RequestException as e:
            self.logger.error(f"Cannot connect to Ollama: {e}")
            return False
    
    def make_request(self, prompt: str, max_retries: Optional[int] = None) -> Optional[str]:
        """Make a request to Ollama API with retry logic"""
        if max_retries is None:
            max_retries = self.ollama_config["max_retries"]
        
        for attempt in range(max_retries + 1):
            try:
                start_time = time.time()
                
                payload = {
                    "model": self.current_model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": self.ollama_config["temperature"],
                        "top_p": self.ollama_config["top_p"]
                    }
                }
                
                self.logger.debug(f"Making request to Ollama (attempt {attempt + 1})")
                response = requests.post(
                    f"{self.ollama_config['host']}/api/generate",
                    json=payload,
                    timeout=self.ollama_config["timeout"]
                )
                
                response_time = time.time() - start_time
                self.stats["total_requests"] += 1
                
                if response.status_code == 200:
                    result = response.json()
                    response_text = result.get("response", "")
                    
                    # Update statistics
                    self.stats["successful_requests"] += 1
                    self.stats["average_response_time"] = (
                        (self.stats["average_response_time"] * (self.stats["successful_requests"] - 1) + response_time) 
                        / self.stats["successful_requests"]
                    )
                    
                    self.logger.debug(f"Request successful in {response_time:.2f}s")
                    return response_text
                else:
                    self.logger.warning(f"Request failed with status {response.status_code}: {response.text}")
                    
            except requests.RequestException as e:
                self.logger.warning(f"Request attempt {attempt + 1} failed: {e}")
                
            # Wait before retry (with exponential backoff)
            if attempt < max_retries:
                wait_time = self.ollama_config["retry_delay"] * (2 ** attempt) + random.uniform(0, 1)
                self.logger.info(f"Waiting {wait_time:.1f}s before retry...")
                time.sleep(wait_time)
        
        self.stats["failed_requests"] += 1
        self.logger.error(f"All {max_retries + 1} attempts failed")
        return None
    
    def classify_single_question(self, question: str, taxonomy_options: List[str] = None) -> Optional[Dict]:
        """Three-stage classification: Subject → Topic → Subtopic"""
        
        # STAGE 1: Classify subject
        subject_result = self.classify_subject(question)
        if not subject_result:
            return None
            
        subject = subject_result["subject"]
        
        # STAGE 2: Classify topic within the subject
        topic_result = self.classify_topic(question, subject, taxonomy_options)
        if not topic_result:
            # If topic classification fails, return subject-only result
            return {
                "subject": subject,
                "topic": "",
                "subtopic": "",
                "confidence": subject_result["confidence"]
            }
        
        topic = topic_result["topic"]
        
        # STAGE 3: Classify subtopic within the subject > topic
        subtopic_result = self.classify_subtopic(question, subject, topic, taxonomy_options)
        if not subtopic_result:
            # If subtopic classification fails, return subject + topic result
            return {
                "subject": subject,
                "topic": topic,
                "subtopic": "",
                "confidence": min(subject_result["confidence"], topic_result["confidence"])
            }
        
        # Combine all three stages
        return {
            "subject": subject,
            "topic": topic,
            "subtopic": subtopic_result["subtopic"],
            "confidence": min(subject_result["confidence"], topic_result["confidence"], subtopic_result["confidence"])
        }
    
    def classify_subject(self, question: str) -> Optional[Dict]:
        """Stage 1: Classify question into subject only"""
        prompt = self.config["templates"]["subject_only"].format(
            question=question.strip()
        )
        
        response = self.make_request(prompt)
        if not response:
            return None
        
        return self._parse_json_response(response, ["subject", "confidence"])
    
    def classify_topic(self, question: str, subject: str, taxonomy_options: List[str] = None) -> Optional[Dict]:
        """Stage 2: Classify question into topic within the given subject"""
        
        # Get topics for this subject from taxonomy
        if not taxonomy_options:
            from taxonomy_constants import get_taxonomy_metadata
            taxonomy_options = get_taxonomy_metadata()["all_paths"]
        
        # Filter topics for the specific subject
        subject_topics = []
        for option in taxonomy_options:
            if option.startswith(f"{subject} > "):
                topic = option.split(" > ")[1]  # Get the topic part
                if topic not in subject_topics:
                    subject_topics.append(topic)
        
        if not subject_topics:
            self.logger.warning(f"No topics found for subject: {subject}")
            return None
        
        # Format topics for prompt
        topics_text = "\n".join([f"- {topic}" for topic in subject_topics])
        
        # Create topic classification prompt
        prompt = self.config["templates"]["topic_only"].format(
            subject=subject,
            question=question.strip(),
            topics=topics_text
        )
        
        response = self.make_request(prompt)
        if not response:
            return None
            
        return self._parse_json_response(response, ["topic", "confidence"])
    
    def classify_subtopic(self, question: str, subject: str, topic: str, taxonomy_options: List[str] = None) -> Optional[Dict]:
        """Stage 3: Classify question into subtopic within the given subject > topic"""
        
        # Get subtopics for this subject > topic from taxonomy
        if not taxonomy_options:
            from taxonomy_constants import get_taxonomy_metadata
            taxonomy_options = get_taxonomy_metadata()["all_paths"]
        
        # Filter subtopics for the specific subject > topic combination
        subject_topic_subtopics = []
        for option in taxonomy_options:
            if option.startswith(f"{subject} > {topic} > "):
                subtopic = option.split(" > ")[2]  # Get the subtopic part
                if subtopic not in subject_topic_subtopics:
                    subject_topic_subtopics.append(subtopic)
        
        if not subject_topic_subtopics:
            self.logger.warning(f"No subtopics found for subject: {subject} > topic: {topic}")
            return None
        
        # Format subtopics for prompt
        subtopics_text = "\n".join([f"- {subtopic}" for subtopic in subject_topic_subtopics])
        
        # Create subtopic classification prompt
        prompt = self.config["templates"]["subtopic_only"].format(
            subject=subject,
            topic=topic,
            question=question.strip(),
            subtopics=subtopics_text
        )
        
        response = self.make_request(prompt)
        if not response:
            return None
            
        return self._parse_json_response(response, ["subtopic", "confidence"])
    
    def _parse_json_response(self, response: str, required_fields: List[str]) -> Optional[Dict]:
        """Parse JSON response with required fields validation"""
        try:
            # Clean response - handle wrapped JSON responses from LLMs
            response = response.strip()
            
            # Remove markdown code blocks
            if response.startswith("```json"):
                response = response[7:]
            if response.endswith("```"):
                response = response[:-3]
            response = response.strip()
            
            # Extract JSON from wrapped responses
            start_idx = response.find('{')
            if start_idx != -1:
                # Count braces to find the matching closing brace
                brace_count = 0
                end_idx = start_idx
                for i, char in enumerate(response[start_idx:]):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end_idx = start_idx + i + 1
                            break
                
                if brace_count == 0:  # Found complete JSON object
                    json_str = response[start_idx:end_idx]
                    self.logger.debug(f"Extracted JSON: {json_str}")
                    result = json.loads(json_str)
                else:
                    # Malformed JSON, try parsing entire response
                    result = json.loads(response)
            else:
                # No JSON object found, try parsing entire response
                result = json.loads(response)
            
            # Validate required fields
            if all(field in result for field in required_fields):
                return result
            else:
                self.logger.warning(f"Missing required fields {required_fields} in response: {result}")
                return None
                
        except json.JSONDecodeError as e:
            self.logger.warning(f"Failed to parse JSON response: {e}")
            self.logger.debug(f"Raw response: {response}")
            return None
    
    def classify_batch_questions(self, questions: List[Dict], taxonomy_options: List[str]) -> List[Optional[Dict]]:
        """Classify multiple questions in a batch"""
        # Limit taxonomy options
        max_items = self.config["prompt"]["max_taxonomy_items"]
        if len(taxonomy_options) > max_items:
            taxonomy_sample = random.sample(taxonomy_options, max_items)
        else:
            taxonomy_sample = taxonomy_options
        
        # Format questions
        questions_text = ""
        for i, q_data in enumerate(questions, 1):
            questions_text += f"{i}. {q_data['question'].strip()}\n\n"
        
        # Format taxonomy
        taxonomy_text = "\n".join([f"- {option}" for option in taxonomy_sample])
        
        # Create prompt
        prompt = self.config["templates"]["batch"].format(
            questions=questions_text,
            taxonomy_options=taxonomy_text
        )
        
        # Make request
        response = self.make_request(prompt)
        if not response:
            return [None] * len(questions)
        
        # Parse JSON response
        try:
            # Clean response
            response = response.strip()
            if response.startswith("```json"):
                response = response[7:]
            if response.endswith("```"):
                response = response[:-3]
            response = response.strip()
            
            results = json.loads(response)
            
            if not isinstance(results, list) or len(results) != len(questions):
                self.logger.warning(f"Batch response length mismatch: expected {len(questions)}, got {len(results) if isinstance(results, list) else 'not a list'}")
                return [None] * len(questions)
            
            # Validate each result
            validated_results = []
            for result in results:
                if isinstance(result, dict) and all(field in result for field in ["subject", "topic", "subtopic", "confidence"]):
                    validated_results.append(result)
                    self.stats["total_questions_processed"] += 1
                else:
                    validated_results.append(None)
            
            return validated_results
            
        except json.JSONDecodeError as e:
            self.logger.warning(f"Failed to parse batch JSON response: {e}")
            self.logger.debug(f"Raw response: {response}")
            return [None] * len(questions)
    
    def get_statistics(self) -> Dict:
        """Get current statistics"""
        success_rate = (self.stats["successful_requests"] / self.stats["total_requests"] * 100) if self.stats["total_requests"] > 0 else 0
        
        return {
            **self.stats,
            "success_rate": success_rate,
            "current_model": self.current_model,
            "questions_per_minute": (self.stats["total_questions_processed"] / (self.stats["average_response_time"] / 60)) if self.stats["average_response_time"] > 0 else 0
        }
    
    def reset_statistics(self):
        """Reset all statistics"""
        self.stats = {key: 0 for key in self.stats.keys()}

def main():
    """Test the Ollama client"""
    client = OllamaClient()
    
    print("Testing Ollama connection...")
    if client.check_ollama_status():
        print("✅ Ollama is accessible")
        
        # Test single classification
        print("\nTesting single question classification...")
        test_question = "What is the capital of India and what are its geographical features?"
        test_taxonomy = [
            "INDIAN PHYSICAL GEOGRAPHY > Political Geography > Capitals and Administrative Centers",
            "INDIAN PHYSICAL GEOGRAPHY > Urban Geography > Major Cities",
            "WORLD PHYSICAL GEOGRAPHY > Political Geography > World Capitals"
        ]
        
        result = client.classify_single_question(test_question, test_taxonomy)
        if result:
            print(f"✅ Classification successful: {result}")
        else:
            print("❌ Classification failed")
        
        # Show statistics
        stats = client.get_statistics()
        print(f"\nStatistics: {stats}")
        
    else:
        print("❌ Cannot connect to Ollama")
        print("Make sure Ollama is running with: ollama serve")

if __name__ == "__main__":
    main()