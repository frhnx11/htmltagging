#!/usr/bin/env python3
"""
Extract questions from HTML file and save to Excel
"""

from bs4 import BeautifulSoup
import pandas as pd
import re
import sys
import os

def clean_text(text):
    """Clean HTML text by removing extra spaces and special characters"""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters like Â
    text = text.replace('Â', '')
    text = text.replace('\xa0', ' ')
    
    # Clean up common HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    return text

def extract_questions_from_html(html_file_path):
    """Extract questions and options from HTML file"""
    
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all question blocks
    question_blocks = soup.find_all('p', class_='pull-left clearfix')
    
    questions_data = []
    serial_no = 1
    
    for block in question_blocks:
        # Check if this is a question block (starts with Q.)
        block_text = block.get_text()
        if not block_text.strip().startswith('Q.'):
            continue
        
        # Extract question number and text
        question_text = clean_text(block_text)
        
        # Remove the question number (Q.1), Q.2), etc.) from the beginning
        question_text = re.sub(r'^Q\.\d+\)\s*', '', question_text)
        
        # Find the next sibling elements to get options
        options = []
        current = block.find_next_sibling()
        
        while current and current.name == 'p' and 'answer' in current.get('class', []):
            option_text = clean_text(current.get_text())
            if option_text:
                options.append(option_text)
            current = current.find_next_sibling()
        
        # Join all options with comma
        options_text = ', '.join(options)
        
        # Add to data
        questions_data.append({
            'S No': serial_no,
            'Question': question_text,
            'Options': options_text
        })
        
        serial_no += 1
    
    return questions_data

def save_to_excel(questions_data, output_file):
    """Save questions data to Excel file"""
    df = pd.DataFrame(questions_data)
    
    # Save to Excel with proper formatting
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Questions', index=False)
        
        # Auto-adjust column widths
        worksheet = writer.sheets['Questions']
        
        # Set column widths
        worksheet.column_dimensions['A'].width = 8  # S No
        worksheet.column_dimensions['B'].width = 80  # Question
        worksheet.column_dimensions['C'].width = 100  # Options
        
        # Wrap text for better readability
        from openpyxl.styles import Alignment
        for row in worksheet.iter_rows(min_row=2):
            row[1].alignment = Alignment(wrap_text=True, vertical='top')
            row[2].alignment = Alignment(wrap_text=True, vertical='top')
    
    print(f"Excel file saved: {output_file}")

def main():
    # Input and output file paths
    input_html = 'input/Page_912.html'
    output_excel = 'output/questions_output.xlsx'
    
    # Check if input file exists
    if not os.path.exists(input_html):
        print(f"Error: Input file not found: {input_html}")
        sys.exit(1)
    
    print(f"Processing HTML file: {input_html}")
    
    # Extract questions
    questions_data = extract_questions_from_html(input_html)
    
    print(f"Found {len(questions_data)} questions")
    
    # Save to Excel
    save_to_excel(questions_data, output_excel)
    
    # Display first few questions as sample
    if questions_data:
        print("\nSample of extracted questions:")
        for i, q in enumerate(questions_data[:3]):
            print(f"\nS No: {q['S No']}")
            print(f"Question: {q['Question'][:100]}...")
            print(f"Options: {q['Options'][:100]}...")

if __name__ == "__main__":
    main()