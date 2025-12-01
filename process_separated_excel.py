#!/usr/bin/env python3
"""
Process Separated Excel - Main script for exam-specific classification

Processes output/SeparatedQuestions.xlsx (3 tabs: TNPSC, Banking, SSC-Railways)
Each tab is classified independently using its exam-specific taxonomy.

Workflow:
1. Load SeparatedQuestions.xlsx with 3 tabs
2. For each tab, use exam-specific classifier
3. Save progress every 10 questions
4. Output: ClassifiedQuestions.xlsx with all 3 tabs classified
"""

import os
import sys
import logging
import signal
import time
from datetime import datetime
from typing import Dict, List

# Import modules
from config import get_config, validate_config
from multi_tab_excel_processor import MultiTabExcelProcessor
from exam_specific_classifier import create_exam_classifier
from cost_tracker import CostTracker
from file_name_utils import generate_result_filename

# Try to import Ollama client
try:
    from ollama_client import OllamaClient
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False
    OllamaClient = None


class SeparatedExcelProcessor:
    """
    Main processor for separated Excel file with exam-specific classification
    """

    def __init__(self):
        """Initialize the processor"""
        self.config = get_config()

        # Setup logging
        self.setup_logging()
        self.logger = logging.getLogger(__name__)

        # Components
        self.excel_processor = None
        self.classifiers = {}  # {exam_type: classifier}
        self.cost_tracker = None
        self.ollama_client = None

        # State management
        self.is_running = True
        self.start_time = datetime.now()

        # Overall statistics
        self.overall_stats = {
            "session_start": self.start_time,
            "total_questions": 0,
            "processed_questions": 0,
            "successful_classifications": 0,
            "failed_classifications": 0,
            "by_tab": {}
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
        self.logger.info(f"\nReceived signal {signum}. Shutting down gracefully...")
        self.is_running = False

        # Save progress before exit
        if self.excel_processor:
            self.logger.info("Saving progress before shutdown...")
            self.excel_processor.save_progress()

        # Print final statistics
        self.print_final_statistics()
        sys.exit(0)

    def initialize_components(self) -> bool:
        """
        Initialize all required components

        Returns:
            True if successful, False otherwise
        """
        try:
            # Initialize Excel processor
            self.logger.info("Initializing Excel processor...")
            
            # Find the single Excel file in output folder
            import os, glob
            output_folder = os.path.dirname(self.config["paths"]["separated_excel"])
            excel_files = glob.glob(os.path.join(output_folder, "*.xlsx"))
            
            if not excel_files:
                self.logger.error(f"No Excel files found in {output_folder}")
                return False
            
            input_file = excel_files[0]  # Use the single Excel file
            self.logger.info(f"Found separated file: {os.path.basename(input_file)}")
            
            # Generate dynamic output filename based on input file
            dynamic_filename = generate_result_filename(os.path.basename(input_file))
            output_file = os.path.join(self.config["paths"]["result_folder"], dynamic_filename)
            
            self.logger.info(f"Using dynamic result filename: {dynamic_filename}")

            self.excel_processor = MultiTabExcelProcessor(input_file, output_file)

            if not self.excel_processor.load_excel_file():
                self.logger.error("Failed to load Excel file")
                return False

            if not self.excel_processor.create_backup():
                self.logger.error("Failed to create backup")
                return False

            # Initialize cost tracker
            self.logger.info("Initializing cost tracker...")
            budget = self.config["openai"]["budget_limit_usd"]
            cost_file = self.config["paths"]["cost_file"]
            self.cost_tracker = CostTracker(budget, cost_file)

            # Initialize Ollama client if available
            if OLLAMA_AVAILABLE:
                try:
                    ollama_config = self.config["ollama"]
                    self.ollama_client = OllamaClient(ollama_config)
                    self.logger.info("Ollama client initialized")
                except Exception as e:
                    self.logger.warning(f"Ollama client unavailable: {e}")
                    self.ollama_client = None

            # Initialize classifiers for each exam type
            self.logger.info("Initializing exam-specific classifiers...")
            for tab_name in self.excel_processor.get_tab_list():
                self.logger.info(f"  Creating classifier for {tab_name}...")
                classifier = create_exam_classifier(tab_name, self.config, self.ollama_client)
                self.classifiers[tab_name] = classifier

            self.logger.info("All components initialized successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to initialize components: {e}")
            return False

    def process_tab(self, tab_name: str) -> Dict:
        """
        Process all questions in a specific tab

        Args:
            tab_name: Name of the tab to process

        Returns:
            Dictionary with processing statistics
        """
        self.logger.info(f"\n{'='*60}")
        self.logger.info(f"Processing tab: {tab_name}")
        self.logger.info(f"{'='*60}")

        tab_stats = {
            'tab_name': tab_name,
            'total': 0,
            'processed': 0,
            'successful': 0,
            'failed': 0,
            'start_time': datetime.now()
        }

        try:
            # Get classifier for this exam
            classifier = self.classifiers[tab_name]

            # Get unprocessed rows
            unprocessed_rows = self.excel_processor.get_unprocessed_rows(tab_name)
            tab_stats['total'] = len(unprocessed_rows)

            self.logger.info(f"Found {tab_stats['total']} questions to classify in {tab_name}")

            if tab_stats['total'] == 0:
                self.logger.info(f"No questions need classification in {tab_name}")
                return tab_stats

            # Process each question
            save_interval = self.config["processing"]["save_interval"]
            backup_interval = self.config["processing"]["backup_interval"]

            for i, row_data in enumerate(unprocessed_rows, 1):
                if not self.is_running:
                    self.logger.info("Processing interrupted by user")
                    break

                self.logger.info(f"\n[{tab_name}] Question {i}/{tab_stats['total']} (Row: {row_data['row_number']})")

                # Classify question
                result = classifier.classify_question(
                    row_data['question'],
                    row_data['explanation']
                )

                if result:
                    # Update Excel with classification
                    success = self.excel_processor.update_row_classification(
                        tab_name,
                        row_data['index'],
                        result['subject'],
                        result['topic'],
                        result['subtopic']
                    )

                    if success:
                        tab_stats['successful'] += 1
                        tab_stats['processed'] += 1
                    else:
                        tab_stats['failed'] += 1
                        self.logger.error(f"Failed to update row {row_data['row_number']}")
                else:
                    tab_stats['failed'] += 1
                    self.logger.error(f"Classification failed for row {row_data['row_number']}")

                # Save progress periodically
                if i % save_interval == 0:
                    self.logger.info(f"Saving progress... ({i}/{tab_stats['total']})")
                    self.excel_processor.save_progress()

                # Create backup periodically
                if i % backup_interval == 0:
                    self.logger.info(f"Creating backup... ({i}/{tab_stats['total']})")
                    self.excel_processor.save_progress(backup=True)

            # Final save for this tab
            self.logger.info(f"Saving final progress for {tab_name}...")
            self.excel_processor.save_progress()

            tab_stats['end_time'] = datetime.now()
            elapsed = (tab_stats['end_time'] - tab_stats['start_time']).total_seconds()
            tab_stats['elapsed_seconds'] = elapsed

            # Print tab summary
            self.logger.info(f"\n{tab_name} Summary:")
            self.logger.info(f"  Total: {tab_stats['total']}")
            self.logger.info(f"  Successful: {tab_stats['successful']}")
            self.logger.info(f"  Failed: {tab_stats['failed']}")
            self.logger.info(f"  Time: {elapsed:.1f}s")

            return tab_stats

        except Exception as e:
            self.logger.error(f"Error processing tab {tab_name}: {e}")
            return tab_stats

    def process_all_tabs(self) -> bool:
        """
        Process all tabs in the Excel file

        Returns:
            True if successful, False otherwise
        """
        try:
            tab_list = self.excel_processor.get_tab_list()

            self.logger.info(f"\nProcessing {len(tab_list)} tabs: {tab_list}")

            for tab_name in tab_list:
                if not self.is_running:
                    break

                tab_stats = self.process_tab(tab_name)
                self.overall_stats['by_tab'][tab_name] = tab_stats
                self.overall_stats['total_questions'] += tab_stats['total']
                self.overall_stats['successful_classifications'] += tab_stats['successful']
                self.overall_stats['failed_classifications'] += tab_stats['failed']

            return True

        except Exception as e:
            self.logger.error(f"Error processing tabs: {e}")
            return False

    def print_final_statistics(self):
        """Print comprehensive final statistics"""
        print("\n" + "="*60)
        print("CLASSIFICATION COMPLETE - FINAL STATISTICS")
        print("="*60)

        # Overall statistics
        total = self.overall_stats['total_questions']
        successful = self.overall_stats['successful_classifications']
        failed = self.overall_stats['failed_classifications']
        success_rate = (successful / total * 100) if total > 0 else 0

        print(f"\nOverall:")
        print(f"  Total questions: {total}")
        print(f"  Successful: {successful} ({success_rate:.1f}%)")
        print(f"  Failed: {failed}")

        # By tab
        print(f"\nBy Exam:")
        for tab_name, tab_stats in self.overall_stats['by_tab'].items():
            print(f"  {tab_name}:")
            print(f"    Total: {tab_stats['total']}")
            print(f"    Successful: {tab_stats['successful']}")
            print(f"    Failed: {tab_stats['failed']}")
            if 'elapsed_seconds' in tab_stats:
                print(f"    Time: {tab_stats['elapsed_seconds']:.1f}s")

        # Cost information
        if self.cost_tracker:
            print(f"\nCost Information:")
            cost_usd = self.cost_tracker.get_total_cost_usd()
            cost_inr = self.cost_tracker.get_total_cost_inr()
            print(f"  Total cost: ${cost_usd:.4f} (Rs. {cost_inr:.2f})")

            session = self.cost_tracker.get_session_summary()
            print(f"  API requests: {session['requests']}")
            print(f"  Total tokens: {session['input_tokens'] + session['output_tokens']:,}")

        # Timing
        end_time = datetime.now()
        elapsed = (end_time - self.start_time).total_seconds()
        print(f"\nTiming:")
        print(f"  Start: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  End: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Total time: {elapsed:.1f}s ({elapsed/60:.1f} minutes)")

        # Output file
        print(f"\nOutput:")
        print(f"  File: {self.config['paths']['output_excel']}")

        print("="*60)

    def run(self) -> bool:
        """
        Run the complete classification process

        Returns:
            True if successful, False otherwise
        """
        self.logger.info("Starting separated Excel classification process...")

        # Validate configuration
        config_errors = validate_config()
        if config_errors:
            self.logger.error("Configuration errors:")
            for error in config_errors:
                self.logger.error(f"  - {error}")
            return False

        # Initialize components
        if not self.initialize_components():
            return False

        # Process all tabs
        if not self.process_all_tabs():
            return False

        # Print final statistics
        self.print_final_statistics()

        return True


def main():
    """Main entry point"""
    print("="*60)
    print("EXAM-SPECIFIC QUESTION CLASSIFICATION")
    print("="*60)
    print("Processing SeparatedQuestions.xlsx with exam-specific taxonomies...")
    print("="*60)
    print()

    start_time = datetime.now()

    # Create processor
    processor = SeparatedExcelProcessor()

    # Run processing
    success = processor.run()

    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()

    if success:
        print(f"\nSUCCESS! Classification completed in {processing_time:.1f}s")
        print(f"\nOutput saved to: {processor.config['paths']['output_excel']}")
        return 0
    else:
        print(f"\nFAILED! Check logs/processing_errors.log for details")
        return 1


if __name__ == "__main__":
    sys.exit(main())
