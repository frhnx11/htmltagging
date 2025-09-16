#!/usr/bin/env python3
"""
Configuration settings for question tagging system
"""

import os

# Ollama Configuration - Using 20B+ model for maximum power
OLLAMA_CONFIG = {
    "host": "http://localhost:11434",  # Default Ollama host
    "model": "gemma2:9b",  # 9B parameter model
    "timeout": 120,  # 2 minutes timeout for 8B model
    "temperature": 0.02,  # Ultra-low temperature for maximum consistency
    "top_p": 0.7,  # More focused responses
    "max_retries": 2,  # Fewer retries due to long processing time
    "retry_delay": 5  # seconds - longer delay for massive model
}

# Alternative models to try if primary fails (in order of preference)
FALLBACK_MODELS = ["llama3.1:8b", "llama3:latest", "mistral:7b"]

# File Paths - Clear 3-folder structure with pre-initialized taxonomy
PATHS = {
    "input_folder": "input",  # HTML files go here
    "questions_file": "output/all_questions_combined.xlsx",  # Extracted questions (no subject mapping)  
    "progress_file": "results/tagging_progress.json",
    "error_log": "results/tagging_errors.log", 
    "output_file": "results/questions_tagged.xlsx"  # Final tagged results
    # REMOVED: taxonomy_file and taxonomy_json - now using constants
}

# Processing Configuration - Optimized for 70B model
PROCESSING_CONFIG = {
    "batch_size": 1,  # Single question processing for two-stage classification
    "max_concurrent": 1,  # Only 1 concurrent request for 70B model
    "save_interval": 10,  # Save very frequently due to slow processing
    "chunk_size": 500,  # Smaller chunks to manage memory with massive model
    "resume_enabled": True,
    "backup_enabled": True
}

# Prompt Configuration - Optimized for 70B model
PROMPT_CONFIG = {
    "max_taxonomy_items": 200,  # Even more options for the massive model
    "include_examples": True,
    "confidence_threshold": 0.8,  # Very high threshold for 70B model
    # REMOVED: No fallback classifications - system must work or fail
}

# Validation Rules - STRICT MODE ONLY
VALIDATION_CONFIG = {
    "strict_matching": True,  # ALWAYS require exact matches in taxonomy
    "allow_partial_matches": False,  # NO partial matches - must be exact
    "min_question_length": 10,  # Skip questions shorter than this
    "max_question_length": 2000,  # Truncate questions longer than this
    "skip_empty_questions": True,
    "reject_invalid_responses": True  # Reject any response not in taxonomy
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",  # DEBUG, INFO, WARNING, ERROR
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "file_logging": True,
    "console_logging": True,
    "max_log_size": 10 * 1024 * 1024,  # 10MB
    "backup_count": 5
}

# Performance Monitoring
PERFORMANCE_CONFIG = {
    "track_timing": True,
    "track_memory": True,
    "report_interval": 100,  # Report stats every N questions
    "target_questions_per_minute": 20,  # Performance target
    "memory_limit_mb": 4096  # 4GB memory limit
}

# Prompt Templates
SUBJECT_CLASSIFICATION_PROMPT = """
You are an educational content classifier. Your task is to classify questions into the correct SUBJECT ONLY.

QUESTION TO CLASSIFY (including answer options when available):
{question}

AVAILABLE SUBJECTS (choose exactly one):\n1. ANCIENT HISTORY - Historical events and periods\n2. ART AND CULTURE - Arts, literature, cultural traditions\n3. Aptitude - General topics in this domain\n4. ECONOMY - Economics, finance, mathematics, statistics\n5. ENVIRONMENT - Environmental issues, ecology\n6. English - General topics in this domain\n7. GOVERNANCE - Government, politics, administration\n8. INDIAN PHYSICAL GEOGRAPHY - Physical or socio-economic geography\n9. INDIAN SOCIO-ECONOMIC GEOGRAPHY - Physical or socio-economic geography\n10. INTERNATIONAL BODIES & ORGANISATIONS - General topics in this domain\n11. MEDIEVAL HISTORY - Historical events and periods\n12. MODERN INDIA - General topics in this domain\n13. POLITY - Government, politics, administration\n14. Reasoning - General topics in this domain\n15. SCIENCE AND TECHNOLOGY - Science, technology, innovations\n16. WORLD PHYSICAL GEOGRAPHY - Physical or socio-economic geography\n17. WORLD SOCIO-ECONOMIC GEOGRAPHY - Physical or socio-economic geography\n\nCLASSIFICATION GUIDE:
- Mathematical/calculation questions → Aptitude
- Logic/reasoning/pattern questions → Reasoning
- Business/Financial/Economic policy questions → ECONOMY
- Physical world features → WORLD PHYSICAL GEOGRAPHY
- Indian geography → INDIAN PHYSICAL GEOGRAPHY
- Historical events → ANCIENT HISTORY/MEDIEVAL HISTORY/MODERN INDIA
- Government/Politics → POLITY
- Science concepts → SCIENCE AND TECHNOLOGY
- Use the answer options to understand the question's domain and context

REQUIRED OUTPUT FORMAT (JSON only):
{{
    "subject": "EXACT_SUBJECT_NAME",
    "confidence": 0.85
}}

CRITICAL RULES:
1. Pick EXACTLY ONE subject from the 14 options above
2. Use the EXACT subject name as listed
3. Return ONLY the JSON, no explanations
4. Consider the primary focus of the question
"""

TOPIC_CLASSIFICATION_PROMPT = """
You are an educational content classifier. You have already determined the SUBJECT is: {subject}

Now classify this question into the correct TOPIC within that subject.

QUESTION TO CLASSIFY (including answer options when available):
{question}

AVAILABLE TOPICS for {subject}:
{topics}

REQUIRED OUTPUT FORMAT (JSON only):
{{
    "topic": "EXACT_TOPIC_NAME",
    "confidence": 0.85
}}

CRITICAL RULES:
1. Pick EXACTLY ONE topic from the options above
2. Use the EXACT topic name as listed - DO NOT modify spelling or wording
3. Copy the topic name EXACTLY as shown - including any apparent typos or unusual spelling
4. Return ONLY the JSON, no explanations
5. The topic must be from the {subject} subject
6. DO NOT correct what you think are spelling errors - use the exact text provided
"""

SUBTOPIC_CLASSIFICATION_PROMPT = """
You are an educational content classifier. You have already determined:
- SUBJECT: {subject}
- TOPIC: {topic}

Now classify this question into the correct SUBTOPIC within that topic.

QUESTION TO CLASSIFY (including answer options when available):
{question}

AVAILABLE SUBTOPICS for {subject} > {topic}:
{subtopics}

REQUIRED OUTPUT FORMAT (JSON only):
{{
    "subtopic": "EXACT_SUBTOPIC_NAME",
    "confidence": 0.85
}}

CRITICAL RULES:
1. Pick EXACTLY ONE subtopic from the options above
2. Use the EXACT subtopic name as listed - DO NOT modify spelling or wording
3. Copy the subtopic name EXACTLY as shown - including any apparent typos or unusual spelling
4. Return ONLY the JSON, no explanations
5. The subtopic must be from the {subject} > {topic} combination
6. DO NOT correct what you think are spelling errors - use the exact text provided

WARNING: Any response that doesn't match exactly will be rejected."""

BATCH_CLASSIFICATION_PROMPT = """
You are a strict educational content classifier. You MUST classify ALL questions using ONLY the exact Subject-Topic-Subtopic combinations from the taxonomy. NO other words allowed.

QUESTIONS TO CLASSIFY:
{questions}

STRICT TAXONOMY - USE ONLY THESE EXACT OPTIONS:
{taxonomy_options}

CRITICAL RULES FOR ALL QUESTIONS:
1. You MUST use EXACT Subject, Topic, and Subtopic names from the taxonomy above
2. You CANNOT create new subjects, topics, or subtopics  
3. You CANNOT use "MATH", "SCIENCE", "SOCIAL SCIENCE" - these don't exist
4. Every response MUST match an existing taxonomy path exactly
5. Pick the closest match from available options

REQUIRED OUTPUT FORMAT (JSON Array only - no extra text):
[
    {{
        "question_id": 1,
        "subject": "EXACT_SUBJECT_FROM_TAXONOMY",
        "topic": "EXACT_TOPIC_FROM_TAXONOMY",
        "subtopic": "EXACT_SUBTOPIC_FROM_TAXONOMY", 
        "confidence": 0.85
    }},
    {{
        "question_id": 2,
        "subject": "EXACT_SUBJECT_FROM_TAXONOMY",
        "topic": "EXACT_TOPIC_FROM_TAXONOMY",
        "subtopic": "EXACT_SUBTOPIC_FROM_TAXONOMY",
        "confidence": 0.90
    }}
]

WARNING: Any response with taxonomy items NOT in the provided list will be rejected.
Return ONLY the JSON array. No explanations.
"""

def get_config():
    """Get complete configuration dictionary"""
    return {
        "ollama": OLLAMA_CONFIG,
        "fallback_models": FALLBACK_MODELS,
        "paths": PATHS,
        "processing": PROCESSING_CONFIG,
        "prompt": PROMPT_CONFIG,
        "validation": VALIDATION_CONFIG,
        "logging": LOGGING_CONFIG,
        "performance": PERFORMANCE_CONFIG,
        "templates": {
            "subject_only": SUBJECT_CLASSIFICATION_PROMPT,
            "topic_only": TOPIC_CLASSIFICATION_PROMPT,
            "subtopic_only": SUBTOPIC_CLASSIFICATION_PROMPT,
            "single": SUBJECT_CLASSIFICATION_PROMPT,  # Use three-stage approach
            "batch": SUBJECT_CLASSIFICATION_PROMPT   # Use three-stage approach
        }
    }

def validate_config():
    """Validate configuration settings"""
    errors = []
    
    # Check if required directories exist
    if not os.path.exists(PATHS["input_folder"]):
        errors.append(f"Input folder not found: {PATHS['input_folder']}")
    
    # Create output directories if they don't exist
    os.makedirs(os.path.dirname(PATHS["questions_file"]), exist_ok=True)
    os.makedirs(os.path.dirname(PATHS["output_file"]), exist_ok=True)
    
    # Validate batch size
    if PROCESSING_CONFIG["batch_size"] < 1 or PROCESSING_CONFIG["batch_size"] > 20:
        errors.append("Batch size should be between 1 and 20")
    
    # Validate confidence threshold
    if not 0 <= PROMPT_CONFIG["confidence_threshold"] <= 1:
        errors.append("Confidence threshold should be between 0 and 1")
    
    # Check Ollama host format
    if not OLLAMA_CONFIG["host"].startswith("http"):
        errors.append("Ollama host should start with http:// or https://")
    
    # Validate taxonomy constants are available
    try:
        from taxonomy_constants import get_taxonomy_metadata
        metadata = get_taxonomy_metadata()
        if not metadata.get("all_paths"):
            errors.append("Taxonomy constants are empty or invalid")
    except ImportError:
        errors.append("Taxonomy constants module not found")
    except Exception as e:
        errors.append(f"Error loading taxonomy constants: {e}")
    
    return errors

if __name__ == "__main__":
    # Validate configuration when run directly
    errors = validate_config()
    if errors:
        print("Configuration Errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✅ Configuration is valid!")
        
    print(f"\nConfiguration Summary:")
    print(f"  Model: {OLLAMA_CONFIG['model']}")
    print(f"  Batch Size: {PROCESSING_CONFIG['batch_size']}")
    print(f"  Max Concurrent: {PROCESSING_CONFIG['max_concurrent']}")
    print(f"  Confidence Threshold: {PROMPT_CONFIG['confidence_threshold']}")