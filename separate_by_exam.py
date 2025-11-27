#!/usr/bin/env python3
"""
Separate Questions by Exam Type - Preprocessing script

Separates questions from input Excel into 3 tabs based on OptionE column:
1. TNPSC: Questions where OptionE = exactly "Answer not known"
2. Banking: Questions where OptionE has content but NOT "Answer not known"
3. SSC/Railways: Questions where OptionE is blank/empty/whitespace

Output: output/SeparatedQuestions.xlsx with 3 tabs
"""

import pandas as pd
import os
import sys
import logging
import argparse
from datetime import datetime
from typing import Tuple, Dict

# Ensure logs directory exists before setting up logging
os.makedirs('logs', exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/exam_separation.log')
    ]
)
logger = logging.getLogger(__name__)


class ExamSeparator:
    """Separates questions by exam type based on OptionE column"""

    def __init__(self, input_file: str = "input/InputExcel.xlsx",
                 output_file: str = "output/SeparatedQuestions.xlsx"):
        """
        Initialize exam separator

        Args:
            input_file: Path to input Excel file
            output_file: Path to output Excel file
        """
        self.input_file = input_file
        self.output_file = output_file

        # Expected columns
        self.expected_columns = [
            'Subject', 'Topic', 'Subtopic', 'Questions',
            'OptionA', 'OptionB', 'OptionC', 'OptionD', 'OptionE',
            'Answer', 'Explanation'
        ]

        # Tab names (Excel doesn't allow / in sheet names)
        self.tab_names = {
            'tnpsc': 'TNPSC',
            'banking': 'Banking',
            'ssc_railways': 'SSC-Railways'
        }

        # Statistics
        self.stats = {
            'total_rows': 0,
            'tnpsc_count': 0,
            'banking_count': 0,
            'ssc_railways_count': 0,
            'errors': []
        }

        self.df = None
        self.separated_dfs = {}

    def validate_input_file(self) -> bool:
        """
        Validate input file exists and has correct structure

        Returns:
            True if valid, False otherwise
        """
        if not os.path.exists(self.input_file):
            logger.error(f"Input file not found: {self.input_file}")
            return False

        try:
            # Load Excel file
            logger.info(f"Loading input file: {self.input_file}")
            self.df = pd.read_excel(self.input_file)

            # Check columns
            missing_columns = [col for col in self.expected_columns if col not in self.df.columns]
            if missing_columns:
                logger.error(f"Missing required columns: {missing_columns}")
                logger.error(f"Found columns: {list(self.df.columns)}")
                return False

            self.stats['total_rows'] = len(self.df)
            logger.info(f"Loaded {self.stats['total_rows']} rows")

            return True

        except Exception as e:
            logger.error(f"Failed to load input file: {e}")
            return False

    def is_option_e_blank(self, value) -> bool:
        """
        Check if OptionE is blank (null, NaN, empty string, or whitespace)

        Args:
            value: Value to check

        Returns:
            True if blank, False otherwise
        """
        if pd.isna(value):
            return True
        if isinstance(value, str):
            return value.strip() == ''
        return False

    def classify_row(self, row) -> str:
        """
        Classify a row into one of three exam types based on OptionE

        Args:
            row: DataFrame row

        Returns:
            'tnpsc', 'banking', or 'ssc_railways'
        """
        option_e = row['OptionE']

        # Rule 3: OptionE is blank → SSC/Railways
        if self.is_option_e_blank(option_e):
            return 'ssc_railways'

        # OptionE has content, check what it is
        option_e_str = str(option_e).strip()

        # Rule 1: OptionE is exactly "Answer not known" → TNPSC
        if option_e_str == "Answer not known":
            return 'tnpsc'

        # Rule 2: OptionE has content but NOT "Answer not known" → Banking
        return 'banking'

    def separate_questions(self) -> bool:
        """
        Separate questions into three DataFrames based on classification

        Returns:
            True if successful, False otherwise
        """
        try:
            logger.info("Starting question separation...")

            # Initialize empty DataFrames for each exam type
            self.separated_dfs = {
                'tnpsc': pd.DataFrame(columns=self.expected_columns),
                'banking': pd.DataFrame(columns=self.expected_columns),
                'ssc_railways': pd.DataFrame(columns=self.expected_columns)
            }

            # Classify each row
            for idx, row in self.df.iterrows():
                exam_type = self.classify_row(row)

                # Add row to appropriate DataFrame
                self.separated_dfs[exam_type] = pd.concat(
                    [self.separated_dfs[exam_type], row.to_frame().T],
                    ignore_index=True
                )

                # Update statistics
                self.stats[f'{exam_type}_count'] += 1

            # Log statistics
            logger.info(f"Separation complete:")
            logger.info(f"  TNPSC: {self.stats['tnpsc_count']} questions")
            logger.info(f"  Banking: {self.stats['banking_count']} questions")
            logger.info(f"  SSC-Railways: {self.stats['ssc_railways_count']} questions")

            # Verify all rows accounted for
            total_separated = (self.stats['tnpsc_count'] +
                             self.stats['banking_count'] +
                             self.stats['ssc_railways_count'])

            if total_separated != self.stats['total_rows']:
                logger.warning(f"Row count mismatch! Total: {self.stats['total_rows']}, "
                             f"Separated: {total_separated}")
                return False

            return True

        except Exception as e:
            logger.error(f"Failed to separate questions: {e}")
            self.stats['errors'].append(str(e))
            return False

    def save_output(self) -> bool:
        """
        Save separated DataFrames to Excel file with 3 tabs

        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure output directory exists
            os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

            logger.info(f"Saving output to: {self.output_file}")

            # Create Excel writer
            with pd.ExcelWriter(self.output_file, engine='openpyxl') as writer:
                # Write each DataFrame to a separate tab
                for exam_type, tab_name in self.tab_names.items():
                    df = self.separated_dfs[exam_type].copy()


                    df.to_excel(writer, sheet_name=tab_name, index=False)
                    logger.info(f"  Written tab '{tab_name}': {len(df)} rows")

            logger.info(f"Output saved successfully!")
            return True

        except Exception as e:
            logger.error(f"Failed to save output: {e}")
            self.stats['errors'].append(str(e))
            return False

    def generate_report(self) -> str:
        """
        Generate summary report

        Returns:
            Formatted report string
        """
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append("EXAM SEPARATION REPORT")
        report_lines.append("=" * 60)
        report_lines.append(f"Input file: {self.input_file}")
        report_lines.append(f"Output file: {self.output_file}")
        report_lines.append(f"Total questions processed: {self.stats['total_rows']}")
        report_lines.append("")
        report_lines.append("DISTRIBUTION:")
        report_lines.append(f"  TNPSC:        {self.stats['tnpsc_count']:5d} questions "
                          f"({self.stats['tnpsc_count']/self.stats['total_rows']*100:.1f}%)")
        report_lines.append(f"  Banking:      {self.stats['banking_count']:5d} questions "
                          f"({self.stats['banking_count']/self.stats['total_rows']*100:.1f}%)")
        report_lines.append(f"  SSC-Railways: {self.stats['ssc_railways_count']:5d} questions "
                          f"({self.stats['ssc_railways_count']/self.stats['total_rows']*100:.1f}%)")
        report_lines.append("")
        report_lines.append("CLASSIFICATION RULES APPLIED:")
        report_lines.append("  1. OptionE = 'Answer not known' → TNPSC")
        report_lines.append("  2. OptionE has other content → Banking")
        report_lines.append("  3. OptionE is blank/empty → SSC-Railways")
        report_lines.append("=" * 60)

        return "\n".join(report_lines)

    def run(self) -> bool:
        """
        Run complete separation process

        Returns:
            True if successful, False otherwise
        """
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)

        # Validate input
        if not self.validate_input_file():
            return False

        # Separate questions
        if not self.separate_questions():
            return False

        # Save output
        if not self.save_output():
            return False

        # Generate report
        print("\n" + self.generate_report())

        return True


def main():
    """Main entry point"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Separate questions by exam type')
    parser.add_argument('--input', type=str, 
                       help='Input Excel file path (default: input/InputExcel.xlsx)')
    parser.add_argument('--output', type=str, 
                       help='Output Excel file path (default: output/SeparatedQuestions.xlsx)')
    
    args = parser.parse_args()
    
    print("📊 EXAM SEPARATOR - Preprocessing Script")
    print("=" * 60)
    print("Separating questions by exam type based on OptionE column...")
    print("=" * 60)
    print()

    start_time = datetime.now()

    # Create separator instance with custom paths if provided
    input_file = args.input if args.input else "input/InputExcel.xlsx"
    output_file = args.output if args.output else "output/SeparatedQuestions.xlsx"
    
    # Check if we have a batch file in input folder
    if not args.input:
        import glob
        batch_files = glob.glob("input/questions_*.xlsx")
        if batch_files:
            # Use the most recent batch file
            batch_files.sort()
            input_file = batch_files[-1]
            print(f"📁 Using batch file: {input_file}")
    
    separator = ExamSeparator(input_file, output_file)

    # Run separation
    success = separator.run()

    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()

    if success:
        print(f"\n✅ SUCCESS! Processing completed in {processing_time:.2f} seconds")
        print(f"\n📁 Output saved to: {separator.output_file}")
        print("\nNext steps:")
        print("  1. Review the separated questions in output/SeparatedQuestions.xlsx")
        print("  2. Run AI classification on individual tabs as needed")
        return 0
    else:
        print(f"\n❌ FAILED! Check logs/exam_separation.log for details")
        if separator.stats['errors']:
            print("\nErrors encountered:")
            for error in separator.stats['errors']:
                print(f"  - {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
