#!/usr/bin/env python3
"""
Multi-Tab Excel Processor - Handle Excel files with multiple tabs for exam-specific classification

Provides utilities for processing Excel files with separate tabs (TNPSC, Banking, SSC-Railways)
Each tab is processed independently with its own taxonomy.
"""

import pandas as pd
import os
import logging
import shutil
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import numpy as np


class MultiTabExcelProcessor:
    """
    Excel processor for multi-tab classification workflow

    Handles reading Excel with multiple exam-specific tabs, tracking progress per tab,
    and saving classifications back to the same structure.
    """

    def __init__(self, input_file_path: str, output_file_path: str = None):
        """
        Initialize multi-tab Excel processor

        Args:
            input_file_path: Path to the input Excel file with multiple tabs
            output_file_path: Path to the output Excel file (optional)
        """
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path or input_file_path.replace('SeparatedQuestions', 'ClassifiedQuestions')

        # Ensure output directory exists
        os.makedirs(os.path.dirname(self.output_file_path), exist_ok=True)

        # Ensure temp directory exists for backups and progress
        os.makedirs('temp', exist_ok=True)

        self.backup_file_path = 'temp/SeparatedQuestions_backup.xlsx'
        self.progress_file_path = 'temp/classification_progress.json'

        # Setup logging
        self.logger = logging.getLogger(__name__)

        # Data storage - dictionary of DataFrames by tab name
        self.tabs = {}  # {tab_name: DataFrame}
        self.original_tabs = {}  # Backup

        # Expected columns
        self.required_columns = [
            'Subject', 'Topic', 'Subtopic', 'Questions',
            'OptionA', 'OptionB', 'OptionC', 'OptionD', 'OptionE',
            'Answer', 'Explanation'
        ]

        # Classification columns (to be filled by AI)
        self.classification_columns = ['Subject', 'Topic', 'Subtopic']

        # Progress tracking per tab
        self.stats_by_tab = {}

        # Overall statistics
        self.overall_stats = {
            'total_questions': 0,
            'processed_questions': 0,
            'successful_classifications': 0,
            'failed_classifications': 0,
            'start_time': None,
            'last_saved': None
        }

    def load_excel_file(self) -> bool:
        """
        Load the Excel file with multiple tabs and validate structure

        Returns:
            True if loaded successfully, False otherwise
        """
        try:
            if not os.path.exists(self.input_file_path):
                self.logger.error(f"Input Excel file not found: {self.input_file_path}")
                return False

            # Load Excel file with all tabs
            self.logger.info(f"Loading Excel file: {self.input_file_path}")
            excel_file = pd.ExcelFile(self.input_file_path)

            # Load each tab
            for sheet_name in excel_file.sheet_names:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                self.tabs[sheet_name] = df
                self.original_tabs[sheet_name] = df.copy()

                self.logger.info(f"  Loaded tab '{sheet_name}': {len(df)} rows")

            # Validate all tabs
            for tab_name, df in self.tabs.items():
                if not self.validate_tab_structure(tab_name, df):
                    return False

            # Analyze processing state for all tabs
            self.analyze_all_tabs()

            return True

        except Exception as e:
            self.logger.error(f"Failed to load Excel file: {e}")
            return False

    def validate_tab_structure(self, tab_name: str, df: pd.DataFrame) -> bool:
        """
        Validate that a tab has expected structure

        Args:
            tab_name: Name of the tab
            df: DataFrame for the tab

        Returns:
            True if structure is valid, False otherwise
        """
        missing_columns = [col for col in self.required_columns if col not in df.columns]

        if missing_columns:
            self.logger.error(f"Tab '{tab_name}' missing required columns: {missing_columns}")
            self.logger.error(f"Found columns: {list(df.columns)}")
            return False

        self.logger.info(f"  Tab '{tab_name}' structure validation passed")
        return True

    def analyze_all_tabs(self):
        """Analyze current state of processing for all tabs"""

        self.overall_stats['start_time'] = datetime.now().isoformat()
        self.overall_stats['total_questions'] = 0
        self.overall_stats['processed_questions'] = 0

        for tab_name, df in self.tabs.items():
            # Count rows that need processing (empty Subject/Topic/Subtopic)
            needs_processing_mask = (
                pd.isna(df['Subject']) |
                pd.isna(df['Topic']) |
                pd.isna(df['Subtopic']) |
                (df['Subject'].astype(str).str.strip() == '') |
                (df['Topic'].astype(str).str.strip() == '') |
                (df['Subtopic'].astype(str).str.strip() == '')
            )

            rows_needing_processing = needs_processing_mask.sum()
            already_processed = len(df) - rows_needing_processing

            # Update tab-specific statistics
            self.stats_by_tab[tab_name] = {
                'total_questions': len(df),
                'processed_questions': already_processed,
                'rows_needing_processing': rows_needing_processing,
                'successful_classifications': 0,
                'failed_classifications': 0
            }

            # Update overall statistics
            self.overall_stats['total_questions'] += len(df)
            self.overall_stats['processed_questions'] += already_processed

            self.logger.info(f"  Tab '{tab_name}': {already_processed}/{len(df)} processed, "
                           f"{rows_needing_processing} need processing")

    def create_backup(self) -> bool:
        """
        Create backup of original Excel file

        Returns:
            True if backup created successfully, False otherwise
        """
        try:
            if os.path.exists(self.backup_file_path):
                self.logger.info(f"Backup file already exists: {self.backup_file_path}")
                return True

            shutil.copy2(self.input_file_path, self.backup_file_path)
            self.logger.info(f"Created backup: {self.backup_file_path}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to create backup: {e}")
            return False

    def get_unprocessed_rows(self, tab_name: str) -> List[Dict]:
        """
        Get list of rows that need processing for a specific tab

        Args:
            tab_name: Name of the tab to process

        Returns:
            List of dictionaries with row data for unprocessed questions
        """
        df = self.tabs[tab_name]

        # Identify rows needing processing
        needs_processing_mask = (
            pd.isna(df['Subject']) |
            pd.isna(df['Topic']) |
            pd.isna(df['Subtopic']) |
            (df['Subject'].astype(str).str.strip() == '') |
            (df['Topic'].astype(str).str.strip() == '') |
            (df['Subtopic'].astype(str).str.strip() == '')
        )

        unprocessed_rows = []

        for idx, row in df[needs_processing_mask].iterrows():
            # Combine Question and Explanation for AI input
            question_text = str(row['Questions']).strip()
            explanation_text = str(row['Explanation']).strip() if pd.notna(row['Explanation']) else ""

            # Create combined text for AI classification
            combined_text = question_text
            if explanation_text and explanation_text.lower() != 'nan':
                combined_text += f"\n\nExplanation: {explanation_text}"

            unprocessed_rows.append({
                'tab_name': tab_name,
                'index': idx,
                'row_number': idx + 1,  # Excel row number (1-based)
                'question': question_text,
                'explanation': explanation_text,
                'combined_text': combined_text,
                'current_subject': row.get('Subject', ''),
                'current_topic': row.get('Topic', ''),
                'current_subtopic': row.get('Subtopic', '')
            })

        return unprocessed_rows

    def get_all_unprocessed_rows(self) -> Dict[str, List[Dict]]:
        """
        Get unprocessed rows for all tabs

        Returns:
            Dictionary mapping tab names to lists of unprocessed rows
        """
        all_unprocessed = {}

        for tab_name in self.tabs.keys():
            unprocessed = self.get_unprocessed_rows(tab_name)
            if unprocessed:
                all_unprocessed[tab_name] = unprocessed
                self.logger.info(f"Tab '{tab_name}': {len(unprocessed)} rows need processing")

        return all_unprocessed

    def update_row_classification(self, tab_name: str, row_index: int,
                                  chapter: str, topic: str, subtopic: str) -> bool:
        """
        Update a specific row with classification results

        Args:
            tab_name: Name of the tab
            row_index: DataFrame index of the row to update
            subject: Subject classification
            topic: Topic classification
            subtopic: Subtopic classification

        Returns:
            True if updated successfully, False otherwise
        """
        try:
            # Update the DataFrame
            df = self.tabs[tab_name]

            # Convert to string to avoid dtype warnings
            df.at[row_index, 'Subject'] = str(chapter)
            df.at[row_index, 'Topic'] = str(topic)
            df.at[row_index, 'Subtopic'] = str(subtopic)

            # Update statistics
            self.stats_by_tab[tab_name]['processed_questions'] += 1
            self.stats_by_tab[tab_name]['successful_classifications'] += 1
            self.overall_stats['processed_questions'] += 1
            self.overall_stats['successful_classifications'] += 1

            self.logger.debug(f"Updated {tab_name} row {row_index + 1}: {chapter} > {topic} > {subtopic}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to update {tab_name} row {row_index}: {e}")
            self.stats_by_tab[tab_name]['failed_classifications'] += 1
            self.overall_stats['failed_classifications'] += 1
            return False

    def save_progress(self, backup: bool = False) -> bool:
        """
        Save current progress to Excel file

        Args:
            backup: If True, save to a timestamped backup file

        Returns:
            True if saved successfully, False otherwise
        """
        try:
            if backup:
                # Save to timestamped backup in temp folder
                os.makedirs('temp', exist_ok=True)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                backup_path = f'temp/ClassifiedQuestions_progress_{timestamp}.xlsx'

                with pd.ExcelWriter(backup_path, engine='openpyxl') as writer:
                    for tab_name, df in self.tabs.items():
                        df.to_excel(writer, sheet_name=tab_name, index=False)

                self.logger.info(f"Progress backup saved: {backup_path}")
            else:
                # Save to output file
                with pd.ExcelWriter(self.output_file_path, engine='openpyxl') as writer:
                    for tab_name, df in self.tabs.items():
                        df.to_excel(writer, sheet_name=tab_name, index=False)

                self.logger.info(f"Classifications saved to: {self.output_file_path}")

            # Update last saved time
            self.overall_stats['last_saved'] = datetime.now().isoformat()
            return True

        except Exception as e:
            self.logger.error(f"Failed to save progress: {e}")
            return False

    def get_processing_statistics(self) -> Dict:
        """Get comprehensive processing statistics"""

        # Calculate derived statistics
        processed = self.overall_stats['processed_questions']
        total = self.overall_stats['total_questions']

        if total > 0:
            completion_percentage = (processed / total) * 100
        else:
            completion_percentage = 0

        # Calculate processing rate
        start_time = self.overall_stats.get('start_time')
        if start_time:
            start_dt = datetime.fromisoformat(start_time)
            elapsed_minutes = (datetime.now() - start_dt).total_seconds() / 60
            if elapsed_minutes > 0:
                questions_per_minute = processed / elapsed_minutes
            else:
                questions_per_minute = 0
        else:
            elapsed_minutes = 0
            questions_per_minute = 0

        return {
            **self.overall_stats,
            'completion_percentage': round(completion_percentage, 2),
            'elapsed_minutes': round(elapsed_minutes, 2),
            'questions_per_minute': round(questions_per_minute, 2),
            'remaining_questions': total - processed,
            'by_tab': self.stats_by_tab
        }

    def get_tab_list(self) -> List[str]:
        """Get list of all tab names"""
        return list(self.tabs.keys())


# Convenience functions for quick operations
def quick_load_multi_tab_excel(file_path: str) -> Optional[MultiTabExcelProcessor]:
    """Quick function to load and validate multi-tab Excel file"""
    processor = MultiTabExcelProcessor(file_path)
    if processor.load_excel_file() and processor.create_backup():
        return processor
    return None


def get_multi_tab_summary(file_path: str) -> Dict:
    """Quick function to get multi-tab Excel file summary"""
    try:
        excel_file = pd.ExcelFile(file_path)
        summary = {
            'tabs': {},
            'total_rows': 0,
            'total_processed': 0,
            'total_unprocessed': 0
        }

        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)

            # Count processed vs unprocessed
            needs_processing = (
                pd.isna(df['Subject']) |
                pd.isna(df['Topic']) |
                pd.isna(df['Subtopic']) |
                (df['Subject'].astype(str).str.strip() == '') |
                (df['Topic'].astype(str).str.strip() == '') |
                (df['Subtopic'].astype(str).str.strip() == '')
            ).sum()

            tab_summary = {
                'total_rows': len(df),
                'processed_rows': len(df) - needs_processing,
                'unprocessed_rows': needs_processing
            }

            summary['tabs'][sheet_name] = tab_summary
            summary['total_rows'] += len(df)
            summary['total_processed'] += (len(df) - needs_processing)
            summary['total_unprocessed'] += needs_processing

        return summary

    except Exception as e:
        return {'error': str(e)}


# Module testing
if __name__ == "__main__":
    print("MULTI-TAB EXCEL PROCESSOR TESTING")
    print("=" * 50)

    # Test file path
    test_file = "output/SeparatedQuestions.xlsx"

    # Quick summary
    print("Quick Multi-Tab Excel Summary:")
    summary = get_multi_tab_summary(test_file)

    if 'error' in summary:
        print(f"  Error: {summary['error']}")
    else:
        print(f"  Total rows: {summary['total_rows']}")
        print(f"  Total processed: {summary['total_processed']}")
        print(f"  Total unprocessed: {summary['total_unprocessed']}")
        print("\n  By Tab:")
        for tab_name, tab_summary in summary['tabs'].items():
            print(f"    {tab_name}:")
            print(f"      Total: {tab_summary['total_rows']}")
            print(f"      Processed: {tab_summary['processed_rows']}")
            print(f"      Unprocessed: {tab_summary['unprocessed_rows']}")

    print("\nFull Processor Test:")

    # Create processor instance
    processor = MultiTabExcelProcessor(test_file)

    # Test loading
    if processor.load_excel_file():
        print("Excel file loaded successfully")

        # Test backup creation
        if processor.create_backup():
            print("Backup created successfully")

        # Get statistics
        stats = processor.get_processing_statistics()
        print(f"\nProcessing Statistics:")
        print(f"  Total questions: {stats['total_questions']}")
        print(f"  Already processed: {stats['processed_questions']}")
        print(f"  Need processing: {stats['remaining_questions']}")
        print(f"  Completion: {stats['completion_percentage']:.1f}%")

        print(f"\nBy Tab:")
        for tab_name, tab_stats in stats['by_tab'].items():
            print(f"  {tab_name}: {tab_stats['processed_questions']}/{tab_stats['total_questions']}")

        print("\nMulti-tab Excel processor testing completed!")
    else:
        print("Failed to load Excel file")
