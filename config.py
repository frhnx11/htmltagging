#!/usr/bin/env python3
"""
Configuration settings for question tagging system
"""

import os

# Ollama Configuration - Using 20B+ model for maximum power
OLLAMA_CONFIG = {
    "host": "http://localhost:11434",  # Local Ollama server 
    "model": "gemma2:9b",  # Fast 8B model - much better performance
    "timeout": 60,  # 1 minute timeout - should be plenty for 8B model
    "temperature": 0.02,  # Ultra-low temperature for maximum consistency
    "top_p": 0.7,  # More focused responses
    "max_retries": 3,  # Standard retries for 8B model
    "retry_delay": 3  # seconds - shorter delay for faster model
}

# Alternative models to try if primary fails (in order of preference)
FALLBACK_MODELS = ["llama3:latest", "mistral:7b", "llama3.2:1b"]

# OpenAI Configuration - GPT-4o mini for cost-effective classification
OPENAI_CONFIG = {
    "api_key": None,  # Will be loaded from environment variable OPENAI_API_KEY
    "model": "gpt-4o-mini",  # Cost-effective model for classification
    "max_tokens": 500,  # Increased to allow detailed reasoning before classification
    "temperature": 0.02,  # Ultra-low temperature for consistency
    "timeout": 30,  # 30 second timeout
    "max_retries": 3,  # Retry on failures
    "retry_delay": 2,  # Delay between retries in seconds
    "requests_per_minute": 100,  # Rate limiting
    "tokens_per_minute": 100000,  # Token rate limiting
    "budget_limit_usd": 10.0,  # Budget limit in USD
    "enable_cost_tracking": True,  # Track costs and usage
    "fallback_to_ollama": True  # Fallback to Ollama on failure/budget exceeded
}

# Provider Configuration - Controls which AI provider to use
PROVIDER_CONFIG = {
    "primary_provider": "openai",  # "openai" or "ollama" 
    "auto_fallback": True,  # Automatically fallback to secondary provider
    "fallback_provider": "ollama",  # Secondary provider
    "cost_alert_threshold": 0.8,  # Alert when 80% of budget used
    "prefer_cost_efficiency": True,  # Prefer lower cost options when possible
    "max_cost_per_question_usd": 0.01  # Maximum cost per question in USD
}

# Rule-Based Classification Configuration
RULE_BASED_CONFIG = {
    "enabled": True,  # Enable rule-based classification
    "priority": "before_ai",  # Apply rules before AI classification
    "log_matches": True,  # Log when rules match
    "track_savings": True,  # Track cost savings from rule matches
    "fallback_to_ai": True  # Use AI if no rules match
}

# File Paths - Organized folder structure
PATHS = {
    "input_excel": "input/InputExcel.xlsx",  # Original input Excel file
    "separated_excel": "output/SeparatedQuestions.xlsx",  # Separated by exam (from separate_by_exam.py)
    "output_excel": "result/ClassifiedQuestions.xlsx",  # Final classified output
    "tags_file": "tags/Tags_New.xlsx",  # Exam-specific taxonomy tags
    "backup_excel": "temp/SeparatedQuestions_backup.xlsx",  # Backup of separated file
    "progress_file": "temp/classification_progress.json",  # Processing progress state
    "error_log": "logs/processing_errors.log",  # Error logs
    "cost_file": "logs/api_costs.json",  # Cost tracking file
    "result_folder": "result"  # Folder for exam-specific result files
}

# Processing Configuration - Optimized for Excel processing
PROCESSING_CONFIG = {
    "batch_size": 1,  # Single question processing for accurate classification
    "max_concurrent": 1,  # Sequential processing for consistency
    "save_interval": 10,  # Save every 10 questions processed
    "backup_interval": 25,  # Create timestamped backup every 25 questions
    "resume_enabled": True,  # Can resume from interrupted processing
    "backup_enabled": True,  # Automatic backup creation
    "use_question_and_explanation": True,  # Combine Question + Explanation for AI input
    "validate_before_save": True  # Validate classifications before saving
}

# Excel Processing Configuration
EXCEL_CONFIG = {
    "required_columns": ['Row No', 'Subject', 'Topic', 'Subtopic', 'Questions',
                        'OptionA', 'OptionB', 'OptionC', 'OptionD', 'OptionE',
                        'Answer', 'Explanation'],
    "classification_columns": ['Subject', 'Topic', 'Subtopic'],
    "input_columns": ['Questions', 'Explanation'],
    "exam_tabs": ['TNPSC', 'Banking', 'SSC-Railways'],  # Expected tabs in separated Excel
    "backup_on_start": True,
    "validate_structure": True,
    "auto_create_missing_folders": True
}

# Prompt Configuration - Optimized for Chapter/Topic/Subtopic classification
PROMPT_CONFIG = {
    "max_taxonomy_items": 200,  # Maximum items to include in prompts
    "include_examples": True,  # Include classification examples
    "confidence_threshold": 0.7,  # Minimum confidence for accepting classifications
    "use_combined_context": True,  # Use Question + Explanation for better accuracy
    "include_classification_guide": True  # Include domain-specific classification guidance
}

# Validation Rules - STRICT MODE ONLY
VALIDATION_CONFIG = {
    "strict_matching": True,  # ALWAYS require exact matches in taxonomy
    "allow_partial_matches": False,  # NO partial matches - must be exact
    "min_question_length": 10,  # Skip questions shorter than this
    "max_question_length": 2000,  # Truncate questions longer than this
    "skip_empty_questions": True,
    "reject_invalid_responses": True,  # Reject any response not in taxonomy
    "max_validation_retries": 3,  # Number of retries when validation fails
    "enhanced_retry_prompts": True  # Add stricter instructions on retries
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

# Prompt Templates - Two-Stage Classification Approach

# Stage 1: Subject Detection Prompt
SUBJECT_DETECTION_PROMPT = """
You are an educational content classifier. Your task is to identify the PRIMARY SUBJECT AREA for this question.

QUESTION TO CLASSIFY (with explanation when available):
{combined_context}

AVAILABLE SUBJECTS (choose exactly one):
{subjects_list}

CLASSIFICATION GUIDE:
- Physics/Electronics/Electrical/Circuit questions → General Science
- Mathematics/Calculation/Arithmetic questions → Aptitude  
- Logic/Reasoning/Pattern/Analogy questions → Reasoning
- Grammar/Vocabulary/English language → English
- Historical events/periods/dynasties → ANCIENT HISTORY, MEDIEVAL HISTORY, MODERN INDIA
- Physical geography/mountains/rivers → WORLD PHYSICAL GEOGRAPHY, INDIAN PHYSICAL GEOGRAPHY
- Economics/Finance/GDP/Policy → ECONOMY
- Government/Politics/Constitution → POLITY
- Arts/Culture/Dance/Music → ART AND CULTURE
- Environment/Ecology/Pollution → ENVIRONMENT
- Computer/Software/IT → Computer Awareness
- Current affairs/Recent events → Current Events

IMPORTANT: 
1. Focus on the PRIMARY knowledge domain being tested
2. Use technical terms and concepts to guide classification
3. Consider BOTH question and explanation content

REQUIRED OUTPUT FORMAT (JSON only):
{{
    "subject": "EXACT_SUBJECT_NAME",
    "confidence": 0.85,
    "reasoning": "Brief explanation of why this subject"
}}

CRITICAL RULES:
1. Pick EXACTLY ONE subject from the list above
2. Use the EXACT subject name as shown
3. Return ONLY the JSON, no extra text
4. Base decision on question content, not answer options
"""

# Stage 2: Exact Triplet Selection Prompt  
TRIPLET_SELECTION_PROMPT = """
You are an educational content classifier. You have identified the subject as: {subject}

Now you must select the EXACT Chapter > Topic > Subtopic combination from the available options.

QUESTION TO CLASSIFY (with explanation when available):
{combined_context}

SUBJECT IDENTIFIED: {subject}

AVAILABLE EXACT TRIPLETS for {subject} (choose exactly one):
{available_triplets}

CRITICAL INSTRUCTIONS:
1. You MUST select EXACTLY ONE triplet from the list above
2. Copy the triplet EXACTLY as shown - do not change any wording
3. The triplet must match your understanding of the question content
4. Use both question and explanation to make the best choice

REQUIRED OUTPUT FORMAT (JSON only):
{{
    "chapter": "EXACT_CHAPTER_NAME",
    "topic": "EXACT_TOPIC_NAME",
    "subtopic": "EXACT_SUBTOPIC_NAME", 
    "full_triplet": "EXACT_FULL_TRIPLET_FROM_LIST",
    "confidence": 0.85,
    "reasoning": "Brief explanation of selection"
}}

WARNING: The triplet must be copied EXACTLY from the available options above. Any deviation will cause validation failure.

EXAMPLE:
If you select "General Science > Physics - Application > Electricity and Magnetism"
Then: 
- chapter: "General Science"
- topic: "Physics - Application"  
- subtopic: "Electricity and Magnetism"
- full_triplet: "General Science > Physics - Application > Electricity and Magnetism"
"""

def get_config():
    """Get complete configuration dictionary"""
    return {
        "ollama": OLLAMA_CONFIG,
        "openai": OPENAI_CONFIG,
        "provider": PROVIDER_CONFIG,
        "rule_based": RULE_BASED_CONFIG,
        "fallback_models": FALLBACK_MODELS,
        "paths": PATHS,
        "processing": PROCESSING_CONFIG,
        "excel": EXCEL_CONFIG,
        "prompt": PROMPT_CONFIG,
        "validation": VALIDATION_CONFIG,
        "logging": LOGGING_CONFIG,
        "performance": PERFORMANCE_CONFIG,
        "templates": {
            "subject_detection": SUBJECT_DETECTION_PROMPT,  # Stage 1: Subject identification
            "triplet_selection": TRIPLET_SELECTION_PROMPT,  # Stage 2: Exact triplet selection
            "two_stage": SUBJECT_DETECTION_PROMPT  # Default to two-stage approach
        }
    }

def validate_config():
    """Validate configuration settings for Excel-based processing"""
    errors = []
    
    # Check if input Excel files exist (allow either original or separated)
    has_input = os.path.exists(PATHS["input_excel"])
    has_separated = os.path.exists(PATHS["separated_excel"])
    
    # Also check for any Excel files in the input and output folders
    import glob
    input_folder_files = glob.glob("input/*.xlsx")
    output_folder_files = glob.glob("output/*.xlsx")
    
    has_any_input = has_input or bool(input_folder_files)
    has_any_separated = has_separated or bool(output_folder_files)

    if not has_any_input and not has_any_separated:
        errors.append(f"No Excel files found. Need either:")
        errors.append(f"  - Excel files in input/ folder")
        errors.append(f"  - Excel files in output/ folder")
    
    # Create required directories if they don't exist
    required_dirs = ["temp", "logs", "output", "result", "tags", "input"]
    for dir_name in required_dirs:
        os.makedirs(dir_name, exist_ok=True)

    # Also create parent directories for all path entries
    for path_key in ["output_excel", "backup_excel", "progress_file", "error_log", "cost_file"]:
        dir_path = os.path.dirname(PATHS[path_key])
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
    
    # Validate batch size
    if PROCESSING_CONFIG["batch_size"] < 1 or PROCESSING_CONFIG["batch_size"] > 10:
        errors.append("Batch size should be between 1 and 10 for Excel processing")
    
    # Validate confidence threshold
    if not 0 <= PROMPT_CONFIG["confidence_threshold"] <= 1:
        errors.append("Confidence threshold should be between 0 and 1")
    
    # Check Ollama host format
    if not OLLAMA_CONFIG["host"].startswith("http"):
        errors.append("Ollama host should start with http:// or https://")
    
    # Validate Excel configuration
    if len(EXCEL_CONFIG["required_columns"]) < 10:
        errors.append("Excel configuration missing required columns")
    
    # Validate taxonomy constants are available
    try:
        from taxonomy_constants import get_taxonomy_for_exam, TAXONOMY_STATS
        # Check each exam type has taxonomy
        for exam_type in EXCEL_CONFIG.get("exam_tabs", ["TNPSC", "Banking", "SSC-Railways"]):
            taxonomy = get_taxonomy_for_exam(exam_type)
            if not taxonomy:
                errors.append(f"Taxonomy not found for exam: {exam_type}")
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
        
    print(f"\nExcel Processing Configuration Summary:")
    print(f"  Model: {OLLAMA_CONFIG['model']}")
    print(f"  Input Excel: {PATHS['input_excel']}")
    print(f"  Batch Size: {PROCESSING_CONFIG['batch_size']}")
    print(f"  Save Interval: {PROCESSING_CONFIG['save_interval']}")
    print(f"  Confidence Threshold: {PROMPT_CONFIG['confidence_threshold']}")
    print(f"  Use Question + Explanation: {PROCESSING_CONFIG['use_question_and_explanation']}")
    print(f"  Required Columns: {len(EXCEL_CONFIG['required_columns'])}")
    print(f"  Classification Columns: {EXCEL_CONFIG['classification_columns']}")