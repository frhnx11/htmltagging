#!/usr/bin/env python3
"""
Batch Question Extractor

Extracts specific batches of questions from the main CSV file (1.8M questions)
and converts them to the required Excel format for AI classification.

Features:
- Extract specific row ranges (e.g., 1-1000, 1001-2000)
- Clean format with only essential columns
- No S No column - completely removed
- Subject/Topic/Subtopic naming convention
- Dynamic output file naming
"""

import pandas as pd
import os
import sys
import argparse
import logging
from datetime import datetime
from typing import Tuple, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BatchQuestionExtractor:
    """
    Extracts batches of questions from main CSV and converts to Excel format
    """

    def __init__(self, input_csv_path: str = "mainexcel/mate.csv", 
                 output_folder: str = "input"):
        """
        Initialize the batch extractor

        Args:
            input_csv_path: Path to the main CSV file with all questions
            output_folder: Folder to save extracted Excel files
        """
        self.input_csv_path = input_csv_path
        self.output_folder = output_folder
        
        # Column mapping from CSV to Excel
        self.column_mapping = {
            'Questions': 'Questions',
            'OptionA': 'OptionA',
            'OptionB': 'OptionB', 
            'OptionC': 'OptionC',
            'OptionD': 'OptionD',
            'OptionE': 'OptionE',
            'Answer': 'Answer',
            'Explanation': 'Explanation'
        }
        
        # Final output columns (no S No!)
        self.output_columns = [
            'Subject',      # Empty - to be filled by AI
            'Topic',        # Empty - to be filled by AI
            'Subtopic',     # Empty - to be filled by AI
            'Questions',
            'OptionA',
            'OptionB',
            'OptionC', 
            'OptionD',
            'OptionE',
            'Answer',
            'Explanation'
        ]

        # Create output folder if it doesn't exist
        os.makedirs(self.output_folder, exist_ok=True)
        
        # Initialize encoding to be detected during validation
        self.encoding = 'utf-8'

    def validate_input_file(self) -> bool:
        """
        Validate that the input CSV file exists and has correct structure

        Returns:
            True if valid, False otherwise
        """
        if not os.path.exists(self.input_csv_path):
            logger.error(f"Input CSV file not found: {self.input_csv_path}")
            return False

        try:
            # Read just the header to check columns - try different encodings
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            header = None
            
            for encoding in encodings:
                try:
                    header = pd.read_csv(self.input_csv_path, nrows=0, encoding=encoding)
                    self.encoding = encoding
                    break
                except UnicodeDecodeError:
                    continue
                    
            if header is None:
                logger.error("Could not read CSV with any standard encoding")
                return False
                
            required_columns = list(self.column_mapping.keys())
            
            missing_columns = [col for col in required_columns if col not in header.columns]
            if missing_columns:
                logger.error(f"Missing required columns in CSV: {missing_columns}")
                return False
                
            logger.info(f"Input CSV validated successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error reading CSV file: {e}")
            return False

    def get_total_rows(self) -> int:
        """
        Get total number of rows in the CSV (excluding header)

        Returns:
            Total row count
        """
        try:
            # Count lines in file - try different encodings
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            total_lines = 0
            
            for encoding in encodings:
                try:
                    with open(self.input_csv_path, 'r', encoding=encoding) as f:
                        total_lines = sum(1 for _ in f)
                    break
                except UnicodeDecodeError:
                    continue
            
            if total_lines == 0:
                logger.error("Could not count rows with any standard encoding")
                return 0
                
            # Subtract 1 for header
            return total_lines - 1
        except Exception as e:
            logger.error(f"Error counting rows: {e}")
            return 0

    def extract_batch(self, start_row: int, end_row: int) -> Tuple[pd.DataFrame, str]:
        """
        Extract a batch of questions from the CSV

        Args:
            start_row: Starting row number (1-based)
            end_row: Ending row number (1-based, inclusive)

        Returns:
            Tuple of (DataFrame with extracted questions, output filename)
        """
        logger.info(f"Extracting rows {start_row} to {end_row} from {self.input_csv_path}")
        
        # Convert to 0-based indexing for pandas
        skip_rows = start_row - 1 if start_row > 1 else 0
        num_rows = end_row - start_row + 1
        
        try:
            # Try different encodings for extraction
            encodings = ['latin-1', 'cp1252', 'iso-8859-1', 'utf-8']
            df = None
            
            for encoding in encodings:
                try:
                    logger.info(f"Trying encoding: {encoding}")
                    df = pd.read_csv(
                        self.input_csv_path,
                        skiprows=range(1, skip_rows + 1),  # Skip header + rows before start
                        nrows=num_rows,
                        usecols=list(self.column_mapping.keys()),
                        encoding=encoding
                    )
                    logger.info(f"Successfully used encoding: {encoding}")
                    break
                except UnicodeDecodeError:
                    continue
                    
            if df is None:
                raise Exception("Could not read CSV with any standard encoding")
            
            logger.info(f"Successfully extracted {len(df)} rows")
            
            # Generate output filename
            output_filename = f"questions_{start_row}_{end_row}.xlsx"
            
            return df, output_filename
            
        except Exception as e:
            logger.error(f"Error extracting batch: {e}")
            raise

    def convert_to_excel_format(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Convert the extracted CSV data to required Excel format

        Args:
            df: DataFrame with extracted CSV data

        Returns:
            DataFrame in Excel format
        """
        logger.info("Converting to Excel format...")
        
        # Create new DataFrame with required columns
        excel_df = pd.DataFrame()
        
        # Add empty classification columns
        excel_df['Subject'] = ''
        excel_df['Topic'] = ''
        excel_df['Subtopic'] = ''
        
        # Map existing columns
        for csv_col, excel_col in self.column_mapping.items():
            if csv_col in df.columns:
                excel_df[excel_col] = df[csv_col]
            else:
                logger.warning(f"Column {csv_col} not found in extracted data")
                excel_df[excel_col] = ''

        # Clean up data
        excel_df = excel_df.fillna('')  # Replace NaN with empty strings
        
        # Ensure all required columns are present
        for col in self.output_columns:
            if col not in excel_df.columns:
                excel_df[col] = ''
                
        # Reorder columns to match expected format
        excel_df = excel_df[self.output_columns]
        
        logger.info(f"Converted to Excel format: {len(excel_df)} rows, {len(excel_df.columns)} columns")
        return excel_df

    def analyze_option_e(self, df: pd.DataFrame) -> dict:
        """
        Analyze OptionE values to understand exam type distribution

        Args:
            df: DataFrame with questions

        Returns:
            Dictionary with OptionE analysis
        """
        option_e_analysis = {
            'total_questions': len(df),
            'answer_not_known': 0,
            'has_content': 0,
            'blank_empty': 0,
            'unique_values': []
        }
        
        if 'OptionE' in df.columns:
            option_e_values = df['OptionE'].fillna('')
            
            for value in option_e_values:
                value_str = str(value).strip()
                
                if value_str.lower() == 'answer not known':
                    option_e_analysis['answer_not_known'] += 1
                elif value_str and value_str != 'nan':
                    option_e_analysis['has_content'] += 1
                else:
                    option_e_analysis['blank_empty'] += 1
            
            # Get unique values (limited to first 10 for display)
            unique_vals = df['OptionE'].fillna('').unique()[:10]
            option_e_analysis['unique_values'] = [str(val) for val in unique_vals]
        
        return option_e_analysis

    def save_excel_file(self, df: pd.DataFrame, filename: str) -> str:
        """
        Save DataFrame to Excel file

        Args:
            df: DataFrame to save
            filename: Name of the output file

        Returns:
            Full path to saved file
        """
        output_path = os.path.join(self.output_folder, filename)
        
        try:
            df.to_excel(output_path, index=False, engine='openpyxl')
            logger.info(f"Successfully saved Excel file: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error saving Excel file: {e}")
            raise

    def extract_and_convert(self, start_row: int, end_row: int) -> str:
        """
        Main method to extract batch and convert to Excel format

        Args:
            start_row: Starting row number (1-based)
            end_row: Ending row number (1-based, inclusive)

        Returns:
            Path to the saved Excel file
        """
        # Validate inputs
        if start_row < 1 or end_row < start_row:
            raise ValueError("Invalid row range. start_row must be >= 1 and end_row >= start_row")

        total_rows = self.get_total_rows()
        if end_row > total_rows:
            logger.warning(f"Requested end_row ({end_row}) exceeds total rows ({total_rows}). Adjusting to {total_rows}")
            end_row = total_rows

        # Extract batch
        df, filename = self.extract_batch(start_row, end_row)
        
        # Analyze OptionE distribution
        option_e_analysis = self.analyze_option_e(df)
        logger.info(f"OptionE analysis: {option_e_analysis}")
        
        # Convert to Excel format
        excel_df = self.convert_to_excel_format(df)
        
        # Save to Excel
        output_path = self.save_excel_file(excel_df, filename)
        
        return output_path


def main():
    """Main function for command-line usage"""
    parser = argparse.ArgumentParser(description='Extract batches of questions from main CSV')
    parser.add_argument('--start', type=int, required=True, help='Starting row number (1-based)')
    parser.add_argument('--end', type=int, required=True, help='Ending row number (1-based, inclusive)')
    parser.add_argument('--input', type=str, default='mainexcel/mate.csv', help='Input CSV file path')
    parser.add_argument('--output', type=str, default='input', help='Output folder path')
    
    args = parser.parse_args()
    
    try:
        # Create extractor
        extractor = BatchQuestionExtractor(args.input, args.output)
        
        # Validate input
        if not extractor.validate_input_file():
            sys.exit(1)
            
        # Show total available rows
        total_rows = extractor.get_total_rows()
        logger.info(f"Total questions available: {total_rows:,}")
        
        # Extract and convert
        output_path = extractor.extract_and_convert(args.start, args.end)
        
        print(f"\n🎉 SUCCESS!")
        print(f"📊 Extracted rows {args.start:,} to {args.end:,}")
        print(f"💾 Saved to: {output_path}")
        print(f"🚀 Ready for processing!")
        
        # Show next steps
        print(f"\nNext steps:")
        print(f"1. Run: python separate_by_exam.py")
        print(f"2. Run: python process_separated_excel.py")
        
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()