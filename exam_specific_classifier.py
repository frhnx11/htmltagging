#!/usr/bin/env python3
"""
Exam-Specific Question Classifier - Single-stage AI-powered classification

Classifies questions using exam-specific taxonomies in a single-stage approach:
- Directly selects the best Subject-Topic-Subtopic triplet from exam-specific options
- Maps "Subject" from taxonomy to "Chapter" in output
- Supports dual providers: OpenAI (primary) and Ollama (fallback)
"""

import json
import logging
import time
import os
from typing import Dict, Optional, Tuple
from datetime import datetime

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from taxonomy_constants import get_taxonomy_for_exam

# Import rule-based classifier
try:
    from rule_based_classifier import RuleBasedClassifier, create_default_rules, get_classification_dict
    RULE_BASED_AVAILABLE = True
except ImportError:
    RULE_BASED_AVAILABLE = False
    RuleBasedClassifier = None

# Import AI clients
try:
    from openai_client import OpenAIClient, create_openai_client
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAIClient = None


class ExamSpecificClassifier:
    """
    Single-stage question classifier using exam-specific taxonomies

    For each exam type (TNPSC, Banking, SSC-Railways), directly selects
    the best matching Subject-Topic-Subtopic triplet in one AI call.
    """

    def __init__(self, exam_type: str, config: Dict, ollama_client=None):
        """
        Initialize exam-specific classifier

        Args:
            exam_type: Exam type ("TNPSC", "Banking", or "SSC-Railways")
            config: Configuration dictionary with provider settings
            ollama_client: Optional OllamaClient instance for fallback
        """
        self.exam_type = exam_type
        self.config = config
        self.provider_config = config.get("provider", {})
        self.ollama_client = ollama_client
        self.openai_client = None

        # Setup logging
        self.logger = logging.getLogger(__name__)

        # Load exam-specific taxonomy
        taxonomy = get_taxonomy_for_exam(exam_type)
        if not taxonomy:
            raise ValueError(f"Invalid exam type: {exam_type}")

        self.subjects = taxonomy['subjects']
        self.triplets = taxonomy['triplets']
        self.triplet_dict = taxonomy['triplet_dict']

        # Determine primary and fallback providers
        self.primary_provider = self.provider_config.get("primary_provider", "openai")
        self.fallback_provider = self.provider_config.get("fallback_provider", "ollama")
        self.auto_fallback = self.provider_config.get("auto_fallback", True)

        # Initialize providers
        self.initialize_providers()

        # Initialize rule-based classifier
        self.rule_based_config = config.get("rule_based", {})
        self.rule_classifier = None
        if RULE_BASED_AVAILABLE and self.rule_based_config.get("enabled", True):
            try:
                rules = create_default_rules()
                self.rule_classifier = RuleBasedClassifier(rules)
                self.logger.info(f"Rule-based classifier initialized with {len(rules)} rules")
            except Exception as e:
                self.logger.warning(f"Failed to initialize rule-based classifier: {e}")
                self.rule_classifier = None

        # Statistics
        self.stats = {
            'total_classifications': 0,
            'successful_classifications': 0,
            'failed_classifications': 0,
            'validation_failures': 0,
            'rule_based_matches': 0,
            'openai_requests': 0,
            'ollama_requests': 0,
            'provider_fallbacks': 0,
            'total_cost_usd': 0.0,
            'cost_savings_usd': 0.0,
            'average_response_time': 0,
            'start_time': datetime.now()
        }

        self.logger.info(f"Exam-specific classifier initialized for {exam_type}")
        self.logger.info(f"  {len(self.subjects)} subjects, {len(self.triplets)} triplets")
        self.logger.info(f"  Primary: {self.primary_provider}, Fallback: {self.fallback_provider}")

    def initialize_providers(self):
        """Initialize AI providers based on configuration"""
        # Initialize OpenAI if available and configured
        if OPENAI_AVAILABLE and (self.primary_provider == "openai" or self.fallback_provider == "openai"):
            openai_config = self.config.get("openai", {})
            api_key = openai_config.get("api_key") or os.getenv("OPENAI_API_KEY")

            if api_key:
                try:
                    # Pass FULL config (not just openai_config) - OpenAIClient expects full config
                    self.openai_client = create_openai_client(self.config)
                    self.logger.info("OpenAI client initialized")
                except Exception as e:
                    self.logger.warning(f"Failed to initialize OpenAI client: {e}")
                    self.openai_client = None
            else:
                self.logger.warning("OpenAI API key not found")
                self.openai_client = None

        # Ollama client is passed in constructor
        if self.ollama_client:
            self.logger.info("Ollama client available")

    def create_classification_prompt(self, question: str, explanation: str = "") -> str:
        """
        Create prompt for single-stage classification

        Args:
            question: Question text
            explanation: Optional explanation text

        Returns:
            Formatted prompt string
        """
        # Combine question and explanation
        combined_text = question
        if explanation and explanation.strip() and explanation.lower() != 'nan':
            combined_text += f"\n\nExplanation: {explanation}"

        # Format available triplets - Show ALL triplets so AI doesn't invent categories
        triplet_list = self.triplets  # Show all triplets
        triplets_formatted = "\n".join([f"{i+1}. {t}" for i, t in enumerate(triplet_list)])

        # Add special instructions for SSC-Railways
        special_instructions = ""
        if self.exam_type == "SSC-Railways":
            special_instructions = """
⚠️ SPECIAL INSTRUCTIONS FOR SSC-RAILWAYS:

SUBJECT MAPPING RULES:
When you identify what the question is about, use these subject mappings:

📊 SPORTS (cricket, football, olympics, tournaments, athletes, games)
   → Search the numbered list for: "Static GK > Static GK > Sports"
   → Select that EXACT triplet

📚 HISTORY (ancient, medieval, modern, dynasties, empires, historical events)
   → Search the numbered list for triplets starting with: "General Studies > Ancient - History >" OR "General Studies > Medieval - History >" OR "General Studies > Modern - History >"
   → Find the CLOSEST match and copy it EXACTLY

🗺️ GEOGRAPHY (countries, rivers, mountains, climate, regions, maps)
   → Search the numbered list for triplets starting with: "General Studies > Geography >"
   → Find the CLOSEST match and copy it EXACTLY

⚖️ POLITY (government, constitution, laws, parliament, judiciary)
   → Search the numbered list for triplets starting with: "General Studies > Polity >"
   → Find the CLOSEST match and copy it EXACTLY

💰 ECONOMY (budget, GDP, banking, finance, trade, economics)
   → Search the numbered list for triplets starting with: "General Studies > Economy >"
   → Find the CLOSEST match and copy it EXACTLY

🔬 PHYSICS (motion, energy, electricity, magnetism, laws of physics)
   → Search the numbered list for triplets starting with: "General Studies > Physics >"
   → Find the CLOSEST match and copy it EXACTLY

🧪 CHEMISTRY (elements, compounds, reactions, periodic table)
   → Search the numbered list for triplets starting with: "General Studies > Chemistry >"
   → Find the CLOSEST match and copy it EXACTLY

🧬 BIOLOGY (animals, plants, human body, cells, life science)
   → Search the numbered list for triplets starting with: "General Studies > Biology >"
   → Find the CLOSEST match and copy it EXACTLY

CRITICAL: COPY EXACTLY FROM THE NUMBERED LIST
✅ Look through the NUMBERED LIST above
✅ Find a triplet that matches the question topic
✅ Copy the ENTIRE triplet EXACTLY character-by-character
✅ Include all three parts: Subject > Topic > Subtopic
✅ DO NOT invent your own triplets - only use what's in the list
"""

        prompt = f"""You are classifying a question for the {self.exam_type} exam.

QUESTION TO CLASSIFY:
{combined_text}

AVAILABLE SUBJECT > TOPIC > SUBTOPIC COMBINATIONS:
{triplets_formatted}
{special_instructions}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨 CRITICAL INSTRUCTION - READ THIS FIRST 🚨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UNDERSTANDING THE LIST STRUCTURE:
The numbered list above shows ALL valid triplets for this exam.
Each line has this EXACT format:
    [NUMBER]. [SUBJECT] > [TOPIC] > [SUBTOPIC]

Example from the list:
    523. History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Justice Party and the Home Rule Movement

ABSOLUTE RULES YOU MUST FOLLOW:
1. ✅ YOU CAN ONLY SELECT FROM THE NUMBERED LIST ABOVE
2. ✅ YOU MUST COPY THE EXACT TEXT - EVERY CHARACTER, SPACE, AND PUNCTUATION MARK
3. ✅ YOU MUST CITE THE LINE NUMBER WHERE YOU FOUND IT
4. ❌ YOU CANNOT CREATE YOUR OWN SUBJECT NAMES - ONLY USE WHAT'S IN THE LIST
5. ❌ YOU CANNOT CREATE YOUR OWN TOPIC NAMES - ONLY USE WHAT'S IN THE LIST
6. ❌ YOU CANNOT CREATE YOUR OWN SUBTOPIC NAMES - ONLY USE WHAT'S IN THE LIST
7. ❌ YOU CANNOT MODIFY, SHORTEN, OR PARAPHRASE ANY PART OF THE TRIPLET
8. ❌ YOU CANNOT COMBINE PARTS FROM DIFFERENT LINES - TAKE THE COMPLETE LINE AS-IS

IF YOUR ANSWER IS NOT FOUND EXACTLY IN THE NUMBERED LIST ABOVE, IT IS WRONG!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP-BY-STEP REASONING PROCESS (FOLLOW EXACTLY IN THIS ORDER):

STEP 1: UNDERSTAND THE QUESTION
- Read the question and explanation carefully
- Identify what specific knowledge area it tests (e.g., "This tests knowledge about Justice Party in Tamil Nadu")

STEP 2: SEARCH FOR MATCHING SUBJECT (EXACT NAME)
- Scan through the numbered list above
- Find subjects that might match the knowledge area
- BE CAREFUL: Some subjects have similar names - you MUST match EXACTLY
- Example: "History, Culture of India and Indian National Movement" ≠ "History, Culture, Heritage & Socio-Political Movements in Tamilnadu"
- Write down the EXACT subject name you found (copy character-by-character)

STEP 3: FIND MATCHING TOPIC WITHIN THAT SUBJECT
- Look only at triplets that start with the exact subject from Step 2
- Find the topic that best matches the question
- Write down the EXACT topic name

STEP 4: FIND MATCHING SUBTOPIC WITHIN THAT TOPIC
- Look only at triplets with the subject AND topic from Steps 2-3
- Find the subtopic that best matches
- Write down the EXACT subtopic name

STEP 5: VERIFY THE COMPLETE TRIPLET EXISTS IN THE NUMBERED LIST
- Scroll through the numbered list and find the EXACT line that matches your triplet
- Write down the line number (e.g., "Found at line 523")
- Verify EVERY character matches: Subject name, " > ", Topic name, " > ", Subtopic name
- If you cannot find this EXACT triplet in the list, YOU MUST GO BACK and choose a different one

STEP 6: RETURN YOUR ANSWER IN JSON FORMAT
- Copy the exact triplet from that line number
- Include the line number in your response
- Provide your complete step-by-step reasoning

REQUIRED OUTPUT FORMAT (JSON ONLY - NO OTHER TEXT):
{{
    "reasoning_steps": "Step 1: Question tests [specific knowledge area]. Step 2: Searched list and found subject '[EXACT subject name from list]'. Step 3: Within that subject, found topic '[EXACT topic name from list]'. Step 4: Within that topic, found subtopic '[EXACT subtopic name from list]'. Step 5: Verified complete triplet exists at line number [XXX].",
    "line_number": XXX,
    "triplet": "Subject > Topic > Subtopic",
    "subject": "Subject",
    "topic": "Topic",
    "subtopic": "Subtopic",
    "confidence": 0.85
}}

⚠️ MANDATORY: The "line_number" field must contain the actual number from the list where you found this triplet.
⚠️ If you cannot find your answer in the numbered list, it means you are INVENTING it - which is FORBIDDEN!

⚠️ CRITICAL WARNINGS - COMMON MISTAKES TO AVOID:
1. DO NOT mix up similar subject names - verify EXACT character match
2. DO NOT create your own topics/subtopics - only use what exists in the list
3. DO NOT abbreviate or paraphrase - copy EXACTLY including spacing and punctuation
4. DO NOT skip the verification step - confirm the triplet exists in the numbered list
5. Return ONLY valid JSON, no extra text before or after

EXAMPLE OF CORRECT REASONING:
Question about "Justice Party in Tamil Nadu during Home Rule Movement"

✓ CORRECT ANSWER:
{{
    "reasoning_steps": "Step 1: Question tests knowledge of Justice Party during Home Rule Movement in Tamil Nadu. Step 2: Searched the numbered list and found subject 'History, Culture, Heritage & Socio-Political Movements in Tamilnadu' (NOT 'History, Culture of India and Indian National Movement' - that's different!). Step 3: Within that subject, found topic 'Justice Party'. Step 4: Within that topic, found subtopic 'Justice Party and the Home Rule Movement'. Step 5: Verified complete triplet exists at line number 523.",
    "line_number": 523,
    "triplet": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Justice Party and the Home Rule Movement",
    "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
    "topic": "Justice Party",
    "subtopic": "Justice Party and the Home Rule Movement",
    "confidence": 0.90
}}

✗ WRONG ANSWER (THIS WILL FAIL):
{{
    "triplet": "History, Culture of India and Indian National Movement > Justice Party > Justice Party and the Home Rule Movement",
    ...
}}
❌ REASON: "History, Culture of India and Indian National Movement" doesn't have any "Justice Party" topics in the list! You mixed up two different subjects!
"""

        return prompt

    def parse_classification_response(self, response_text: str) -> Optional[Dict]:
        """
        Parse AI response to extract classification

        Args:
            response_text: Raw response from AI

        Returns:
            Dictionary with subject, topic, subtopic or None if parsing fails
        """
        try:
            # Check for None response first
            if response_text is None:
                self.logger.error("Received None response from AI provider")
                return None
            
            # Ensure response_text is a string
            if not isinstance(response_text, str):
                self.logger.error(f"Expected string response, got {type(response_text)}")
                return None
            
            # Try to find JSON in response
            response_text = response_text.strip()

            # Remove markdown code blocks if present
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]

            response_text = response_text.strip()

            # Parse JSON
            data = json.loads(response_text)

            # Extract fields with safe None handling
            subject = data.get('subject') or ''
            topic = data.get('topic') or ''
            subtopic = data.get('subtopic') or ''
            triplet = data.get('triplet') or ''
            
            # Safely strip whitespace
            subject = subject.strip() if subject else ''
            topic = topic.strip() if topic else ''
            subtopic = subtopic.strip() if subtopic else ''
            triplet = triplet.strip() if triplet else ''
            confidence = data.get('confidence', 0.0)
            reasoning_steps = data.get('reasoning_steps', '')
            line_number = data.get('line_number', None)

            # Log reasoning steps and line number (helps debug classification)
            if reasoning_steps:
                self.logger.debug(f"AI Reasoning: {reasoning_steps}")
            if line_number:
                self.logger.info(f"Selected from line #{line_number}: {triplet}")

            if not (subject and topic and subtopic):
                self.logger.error("Missing required fields in response")
                return None

            return {
                'subject': subject,
                'topic': topic,
                'subtopic': subtopic,
                'triplet': triplet,
                'confidence': confidence,
                'reasoning_steps': reasoning_steps,
                'line_number': line_number
            }

        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse JSON response: {e}")
            self.logger.debug(f"Response text: {response_text}")
            return None
        except Exception as e:
            self.logger.error(f"Error parsing response: {e}")
            return None

    def validate_classification(self, result: Dict) -> bool:
        """
        Validate that classification exists in exam-specific taxonomy with enhanced debugging

        Args:
            result: Classification result dictionary

        Returns:
            True if valid, False otherwise
        """
        triplet = result.get('triplet', '')
        subject = result.get('subject', '')
        topic = result.get('topic', '')
        subtopic = result.get('subtopic', '')
        line_number = result.get('line_number')
        
        # Construct the triplet for validation
        constructed_triplet = f"{subject} > {topic} > {subtopic}"

        # Check if constructed triplet exists in taxonomy
        if constructed_triplet in self.triplet_dict:
            result['triplet'] = constructed_triplet  # Ensure consistency
            return True

        # If direct triplet was provided, also check it
        if triplet and triplet in self.triplet_dict:
            return True

        # Enhanced debugging for validation failures
        self.logger.warning(f"Classification not found in {self.exam_type} taxonomy: {constructed_triplet}")
        
        # Check if individual components exist in other combinations
        subject_matches = [t for t in self.triplets if t.startswith(subject + " >")]
        if subject_matches:
            self.logger.info(f"Subject '{subject}' exists in {len(subject_matches)} valid triplets")
            if len(subject_matches) <= 5:  # Show a few examples
                for match in subject_matches[:3]:
                    self.logger.info(f"  Valid example: {match}")
        else:
            # Check for similar subjects (fuzzy matching)
            similar_subjects = []
            for valid_triplet in self.triplets:
                valid_subject = valid_triplet.split(" > ")[0]
                if subject.lower() in valid_subject.lower() or valid_subject.lower() in subject.lower():
                    similar_subjects.append(valid_subject)
            
            if similar_subjects:
                unique_similar = list(set(similar_subjects))[:3]
                self.logger.warning(f"Subject '{subject}' not found. Similar subjects: {unique_similar}")

        # Verify line number if provided
        if line_number:
            try:
                line_idx = int(line_number) - 1  # Convert to 0-based index
                if 0 <= line_idx < len(self.triplets):
                    actual_triplet = self.triplets[line_idx]
                    if actual_triplet != constructed_triplet:
                        self.logger.warning(f"Line number mismatch! Line {line_number} contains: '{actual_triplet}', but AI claimed: '{constructed_triplet}'")
                else:
                    self.logger.warning(f"Invalid line number {line_number}. Valid range: 1-{len(self.triplets)}")
            except (ValueError, TypeError):
                self.logger.warning(f"Invalid line number format: {line_number}")

        return False

    def classify_with_provider(self, prompt: str, provider: str) -> Optional[str]:
        """
        Get classification from specified provider

        Args:
            prompt: Classification prompt
            provider: "openai" or "ollama"

        Returns:
            Raw response text or None if failed
        """
        try:
            if provider == "openai" and self.openai_client:
                self.stats['openai_requests'] += 1
                response = self.openai_client.make_request(
                    prompt=prompt,
                    question="",
                    operation="classification"
                )
                return response

            elif provider == "ollama" and self.ollama_client:
                self.stats['ollama_requests'] += 1
                response = self.ollama_client.generate(prompt)
                return response

            else:
                self.logger.error(f"Provider '{provider}' not available")
                return None

        except Exception as e:
            self.logger.error(f"Error calling {provider}: {e}")
            return None

    def classify_question(self, question: str, explanation: str = "") -> Optional[Dict]:
        """
        Classify a question using single-stage approach

        Args:
            question: Question text
            explanation: Optional explanation text

        Returns:
            Dictionary with chapter, topic, subtopic or None if failed
        """
        start_time = time.time()
        self.stats['total_classifications'] += 1

        try:
            # Try rule-based classification first
            if (self.rule_classifier and 
                self.rule_based_config.get("enabled", True) and 
                self.rule_based_config.get("priority") == "before_ai"):
                
                rule_result = self.rule_classifier.classify_question(question, self.exam_type)
                
                if rule_result.matched:
                    # Rule matched - use rule-based classification
                    self.stats['rule_based_matches'] += 1
                    
                    # Calculate cost savings (approximate cost per question)
                    cost_savings = 0.000054  # Approximate cost per question with GPT-4o mini
                    self.stats['cost_savings_usd'] += cost_savings
                    
                    classification = {
                        'subject': rule_result.rule.chapter,
                        'topic': rule_result.rule.topic,
                        'subtopic': rule_result.rule.subtopic,
                        'confidence': rule_result.confidence
                    }
                    
                    # Update statistics
                    self.stats['successful_classifications'] += 1
                    elapsed = time.time() - start_time
                    
                    # Update average response time
                    total = self.stats['total_classifications']
                    current_avg = self.stats['average_response_time']
                    self.stats['average_response_time'] = ((current_avg * (total - 1)) + elapsed) / total
                    
                    if self.rule_based_config.get("log_matches", True):
                        self.logger.info(f"Rule-based classification: {classification['subject']} > "
                                       f"{classification['topic']} > {classification['subtopic']} "
                                       f"(rule: {rule_result.rule.description})")
                    
                    return classification
            
            # No rule matched or rule-based disabled - proceed with AI classification with retry
            validation_config = self.config.get("validation", {})
            max_retries = validation_config.get("max_validation_retries", 3)
            for attempt in range(max_retries):
                # Create prompt
                prompt = self.create_classification_prompt(question, explanation)
                
                if attempt > 0:
                    self.logger.info(f"Retry attempt {attempt + 1}/{max_retries} for validation failure")
                    # Add stricter instructions for retries
                    prompt += f"""

🚨 RETRY ATTEMPT {attempt + 1} - VALIDATION FAILED BEFORE 🚨

Your previous classification was REJECTED because it was not found in the taxonomy.
This means you either:
1. Created a triplet that doesn't exist in the numbered list
2. Made a typo in copying the exact text
3. Mixed up subjects/topics/subtopics from different lines

DOUBLE-CHECK YOUR WORK:
- Find the EXACT line number in the numbered list above
- Copy EVERY character exactly (including spaces, punctuation, capitalization)
- Do NOT create custom names - only use what's in the list
- Verify the complete triplet exists before submitting

"""

                # Try primary provider
                self.logger.debug(f"Attempting classification with {self.primary_provider} (attempt {attempt + 1})")
                response_text = self.classify_with_provider(prompt, self.primary_provider)

                # If primary fails and auto-fallback enabled, try fallback
                if not response_text and self.auto_fallback:
                    self.logger.info(f"Primary provider failed, falling back to {self.fallback_provider}")
                    self.stats['provider_fallbacks'] += 1
                    response_text = self.classify_with_provider(prompt, self.fallback_provider)

                if not response_text:
                    self.logger.error(f"All providers failed on attempt {attempt + 1}")
                    continue

                # Parse response
                result = self.parse_classification_response(response_text)
                if not result:
                    self.logger.error(f"Failed to parse response on attempt {attempt + 1}")
                    continue

                # Validate classification
                if self.validate_classification(result):
                    self.logger.info(f"Validation successful on attempt {attempt + 1}")
                    break
                else:
                    self.logger.warning(f"Classification validation failed on attempt {attempt + 1}")
                    self.stats['validation_failures'] += 1
                    if attempt == max_retries - 1:
                        self.logger.error(f"All {max_retries} attempts failed validation")
                        self.stats['failed_classifications'] += 1
                        return None
            else:
                # All retries exhausted without success
                self.stats['failed_classifications'] += 1
                return None

            # Map AI result to output format
            classification = {
                'subject': result['subject'],
                'topic': result['topic'],
                'subtopic': result['subtopic'],
                'confidence': result.get('confidence', 0.0)
            }

            # Update statistics
            self.stats['successful_classifications'] += 1
            elapsed = time.time() - start_time

            # Update average response time
            total = self.stats['total_classifications']
            current_avg = self.stats['average_response_time']
            self.stats['average_response_time'] = ((current_avg * (total - 1)) + elapsed) / total

            self.logger.info(f"Classified: {classification['subject']} > {classification['topic']} > "
                           f"{classification['subtopic']} (confidence: {classification['confidence']:.2f})")

            return classification

        except Exception as e:
            self.logger.error(f"Classification error: {e}")
            self.stats['failed_classifications'] += 1
            return None

    def get_statistics(self) -> Dict:
        """Get classification statistics"""
        success_rate = 0
        if self.stats['total_classifications'] > 0:
            success_rate = (self.stats['successful_classifications'] /
                          self.stats['total_classifications']) * 100

        return {
            **self.stats,
            'success_rate': round(success_rate, 2),
            'exam_type': self.exam_type,
            'taxonomy_size': len(self.triplets)
        }


def create_exam_classifier(exam_type: str, config: Dict, ollama_client=None) -> ExamSpecificClassifier:
    """
    Create an exam-specific classifier

    Args:
        exam_type: Exam type ("TNPSC", "Banking", or "SSC-Railways")
        config: Configuration dictionary
        ollama_client: Optional Ollama client

    Returns:
        ExamSpecificClassifier instance
    """
    return ExamSpecificClassifier(exam_type, config, ollama_client)


# Module testing
if __name__ == "__main__":
    from config import get_config

    print("EXAM-SPECIFIC CLASSIFIER TESTING")
    print("=" * 50)

    config = get_config()

    # Test classifier for each exam
    for exam_type in ["TNPSC", "Banking", "SSC-Railways"]:
        print(f"\nTesting {exam_type} classifier...")
        try:
            classifier = create_exam_classifier(exam_type, config)
            stats = classifier.get_statistics()
            print(f"  Initialized successfully")
            print(f"  Subjects: {len(classifier.subjects)}")
            print(f"  Triplets: {stats['taxonomy_size']}")
        except Exception as e:
            print(f"  Error: {e}")

    print("\nExam-specific classifier testing completed!")
