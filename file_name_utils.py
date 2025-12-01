#!/usr/bin/env python3
"""
File Name Utilities

Utilities for parsing and generating file names based on question ranges.
Supports dynamic naming for batch processing of questions.
"""

import re
import os
from typing import Tuple, Optional


def parse_question_range(filename: str) -> Optional[Tuple[int, int]]:
    """
    Extract question range numbers from file names
    
    Supports multiple file naming formats:
    - questions_1_1000.xlsx -> (1, 1000)
    - (1-1000)Output.xlsx -> (1, 1000) 
    - 1-1000.xlsx -> (1, 1000)
    
    Args:
        filename: Name of the file (with or without path)
    
    Returns:
        Tuple of (start, end) numbers or None if not found
    """
    # Remove path and get just the filename
    base_name = os.path.basename(filename)
    
    # Pattern 1: questions_X_Y.xlsx (input batch files)
    pattern1 = r'questions_(\d+)_(\d+)\.xlsx'
    match = re.search(pattern1, base_name, re.IGNORECASE)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    
    # Pattern 2: (X-Y)Output.xlsx (separated output files)
    pattern2 = r'\((\d+)-(\d+)\)Output\.xlsx'
    match = re.search(pattern2, base_name, re.IGNORECASE)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    
    # Pattern 3: X-Y.xlsx (final result files)
    pattern3 = r'^(\d+)-(\d+)\.xlsx$'
    match = re.search(pattern3, base_name, re.IGNORECASE)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    
    # Pattern 4: SeparatedQuestions.xlsx or similar (fallback to default range)
    if 'separated' in base_name.lower() or 'classified' in base_name.lower():
        return None  # No specific range detected
    
    return None


def generate_output_filename(input_filename: str) -> str:
    """
    Generate output filename for exam separation
    
    Args:
        input_filename: Input file name (e.g., questions_1_1000.xlsx)
    
    Returns:
        Output filename (e.g., (1-1000)Output.xlsx)
    """
    question_range = parse_question_range(input_filename)
    
    if question_range:
        start, end = question_range
        return f"({start}-{end})Output.xlsx"
    else:
        # Fallback to default name if range can't be determined
        return "SeparatedQuestions.xlsx"


def generate_result_filename(separated_filename: str) -> str:
    """
    Generate result filename for final classification output
    
    Args:
        separated_filename: Separated file name (e.g., (1-1000)Output.xlsx)
    
    Returns:
        Result filename (e.g., 1-1000.xlsx)
    """
    question_range = parse_question_range(separated_filename)
    
    if question_range:
        start, end = question_range
        return f"{start}-{end}.xlsx"
    else:
        # Fallback to default name if range can't be determined
        return "ClassifiedQuestions.xlsx"


def get_batch_info_from_filename(filename: str) -> dict:
    """
    Get comprehensive batch information from filename
    
    Args:
        filename: Any supported filename format
    
    Returns:
        Dictionary with batch information
    """
    question_range = parse_question_range(filename)
    base_name = os.path.basename(filename)
    
    info = {
        'original_filename': base_name,
        'has_range': question_range is not None,
        'start_question': None,
        'end_question': None,
        'total_questions': None,
        'batch_id': None,
        'suggested_output': None,
        'suggested_result': None
    }
    
    if question_range:
        start, end = question_range
        info.update({
            'start_question': start,
            'end_question': end,
            'total_questions': end - start + 1,
            'batch_id': f"{start}-{end}",
            'suggested_output': generate_output_filename(filename),
            'suggested_result': generate_result_filename(filename)
        })
    
    return info


def find_input_files_with_ranges(directory: str = "input") -> list:
    """
    Find all input files with question ranges in a directory
    
    Args:
        directory: Directory to search for input files
    
    Returns:
        List of dictionaries with file information and ranges
    """
    input_files = []
    
    if not os.path.exists(directory):
        return input_files
    
    for filename in os.listdir(directory):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(directory, filename)
            batch_info = get_batch_info_from_filename(filename)
            
            if batch_info['has_range']:
                batch_info['full_path'] = file_path
                input_files.append(batch_info)
    
    # Sort by start question number
    input_files.sort(key=lambda x: x['start_question'] or 0)
    return input_files


def validate_filename_format(filename: str) -> dict:
    """
    Validate if filename follows expected format and provide suggestions
    
    Args:
        filename: Filename to validate
    
    Returns:
        Validation result with suggestions
    """
    result = {
        'is_valid': False,
        'format_type': None,
        'issues': [],
        'suggestions': []
    }
    
    base_name = os.path.basename(filename)
    question_range = parse_question_range(filename)
    
    if question_range:
        result['is_valid'] = True
        start, end = question_range
        
        # Determine format type
        if 'questions_' in base_name:
            result['format_type'] = 'input_batch'
        elif '(' in base_name and ')Output' in base_name:
            result['format_type'] = 'separated_output'
        elif re.match(r'^\d+-\d+\.xlsx$', base_name):
            result['format_type'] = 'final_result'
        
        # Validate range logic
        if start >= end:
            result['issues'].append(f"Start question ({start}) should be less than end question ({end})")
        
        if end - start + 1 > 10000:
            result['issues'].append(f"Large batch size ({end - start + 1} questions) may cause performance issues")
    
    else:
        result['issues'].append("Could not extract question range from filename")
        result['suggestions'].append("Use format: questions_START_END.xlsx (e.g., questions_1_1000.xlsx)")
        result['suggestions'].append("Or: (START-END)Output.xlsx for separated files")
        result['suggestions'].append("Or: START-END.xlsx for final results")
    
    return result


if __name__ == "__main__":
    # Test the utility functions
    test_files = [
        "questions_1_1000.xlsx",
        "questions_1001_2000.xlsx",
        "(1-1000)Output.xlsx",
        "(2001-3000)Output.xlsx", 
        "1-1000.xlsx",
        "5001-6000.xlsx",
        "SeparatedQuestions.xlsx",
        "ClassifiedQuestions.xlsx"
    ]
    
    print("🧪 Testing File Name Utilities")
    print("=" * 50)
    
    for filename in test_files:
        print(f"\n📄 File: {filename}")
        
        # Test range parsing
        range_result = parse_question_range(filename)
        print(f"   Range: {range_result}")
        
        # Test output filename generation
        if 'questions_' in filename:
            output_name = generate_output_filename(filename)
            print(f"   Output: {output_name}")
        
        # Test result filename generation
        if 'Output' in filename or 'questions_' in filename:
            result_name = generate_result_filename(filename)
            print(f"   Result: {result_name}")
        
        # Test batch info
        batch_info = get_batch_info_from_filename(filename)
        if batch_info['has_range']:
            print(f"   Batch: {batch_info['batch_id']} ({batch_info['total_questions']} questions)")
        
        # Test validation
        validation = validate_filename_format(filename)
        print(f"   Valid: {validation['is_valid']} ({validation['format_type']})")
    
    print(f"\n✅ File name utilities tested successfully!")