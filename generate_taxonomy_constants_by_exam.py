#!/usr/bin/env python3
"""
Generate Taxonomy Constants by Exam - Read exam-specific taxonomies and generate Python constants

Reads tags/Tags_New.xlsx with 3 tabs (TNPSC, Banking, SSC-Railways)
Each tab has: Subject | Topic | Subtopic

Generates taxonomy_constants.py with exam-specific triplets and lookup dictionaries
"""

import pandas as pd
import os
import sys
from datetime import datetime
from typing import Dict, List, Set


class TaxonomyGenerator:
    """Generate taxonomy constants from exam-specific tags Excel file"""

    def __init__(self, tags_file: str = "tags/Tags_New.xlsx"):
        """
        Initialize taxonomy generator

        Args:
            tags_file: Path to tags Excel file
        """
        self.tags_file = tags_file
        self.exam_tabs = {
            'TNPSC': 'TNPSC',
            'Banking': 'BANKING',
            'SSCRailways': 'SSC_RAILWAYS'  # Actual tab name, sanitized variable name
        }

        # Storage for parsed data
        self.exam_taxonomies = {}

        # Statistics
        self.stats = {
            'total_triplets': 0,
            'by_exam': {}
        }

    def validate_tags_file(self) -> bool:
        """
        Validate tags file exists and has correct structure

        Returns:
            True if valid, False otherwise
        """
        if not os.path.exists(self.tags_file):
            print(f"Error: Tags file not found: {self.tags_file}")
            return False

        try:
            # Load Excel file to check tabs
            excel_file = pd.ExcelFile(self.tags_file)

            # Check if all required tabs exist
            required_tabs = list(self.exam_tabs.keys())
            missing_tabs = [tab for tab in required_tabs if tab not in excel_file.sheet_names]

            if missing_tabs:
                print(f"Error: Missing required tabs: {missing_tabs}")
                print(f"   Found tabs: {excel_file.sheet_names}")
                return False

            print(f"Found all required tabs: {required_tabs}")
            return True

        except Exception as e:
            print(f"Error validating tags file: {e}")
            return False

    def parse_taxonomy(self, tab_name: str) -> Dict:
        """
        Parse taxonomy from a specific tab

        Args:
            tab_name: Name of the tab to parse

        Returns:
            Dictionary with subjects, triplets, and lookup dict
        """
        try:
            # Read the tab
            df = pd.read_excel(self.tags_file, sheet_name=tab_name)

            # Strip whitespace from column names
            df.columns = df.columns.str.strip()

            # Validate columns
            required_columns = ['Subject', 'Topic', 'Subtopic']
            if not all(col in df.columns for col in required_columns):
                print(f"Error: Tab '{tab_name}' missing required columns")
                print(f"   Expected: {required_columns}")
                print(f"   Found: {list(df.columns)}")
                return None

            # Remove rows with any missing values
            df = df.dropna(subset=required_columns)

            # Get unique subjects
            subjects = sorted(df['Subject'].unique().tolist())

            # Build triplets and dictionary
            triplets = []
            triplet_dict = {}

            for _, row in df.iterrows():
                subject = str(row['Subject']).strip()
                topic = str(row['Topic']).strip()
                subtopic = str(row['Subtopic']).strip()

                # Normalize characters - fix encoding issues from Excel
                subject = subject.replace('�', '-').replace('–', '-').replace('—', '-')
                topic = topic.replace('�', '-').replace('–', '-').replace('—', '-')
                subtopic = subtopic.replace('�', '-').replace('–', '-').replace('—', '-')

                # Create triplet string
                triplet = f"{subject} > {topic} > {subtopic}"
                triplets.append(triplet)

                # Add to dictionary
                triplet_dict[triplet] = {
                    'subject': subject,
                    'topic': topic,
                    'subtopic': subtopic
                }

            # Remove duplicates while preserving order
            seen = set()
            unique_triplets = []
            unique_dict = {}

            for triplet in triplets:
                if triplet not in seen:
                    seen.add(triplet)
                    unique_triplets.append(triplet)
                    unique_dict[triplet] = triplet_dict[triplet]

            print(f"Parsed {tab_name}: {len(subjects)} subjects, {len(unique_triplets)} unique triplets")

            return {
                'subjects': subjects,
                'triplets': unique_triplets,
                'triplet_dict': unique_dict,
                'count': len(unique_triplets)
            }

        except Exception as e:
            print(f"Error parsing tab '{tab_name}': {e}")
            return None

    def parse_all_taxonomies(self) -> bool:
        """
        Parse taxonomies from all exam tabs

        Returns:
            True if successful, False otherwise
        """
        print("\nParsing taxonomies from all exam tabs...")

        for display_name, var_name in self.exam_tabs.items():
            taxonomy = self.parse_taxonomy(display_name)

            if taxonomy is None:
                return False

            self.exam_taxonomies[var_name] = taxonomy
            self.stats['by_exam'][var_name] = taxonomy['count']
            self.stats['total_triplets'] += taxonomy['count']

        return True

    def generate_constants_file(self, output_file: str = "taxonomy_constants.py") -> bool:
        """
        Generate Python constants file

        Args:
            output_file: Path to output Python file

        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"\nGenerating {output_file}...")

            lines = []

            # File header
            lines.append('#!/usr/bin/env python3')
            lines.append('"""')
            lines.append('Taxonomy Constants - Exam-Specific Taxonomies')
            lines.append('')
            lines.append(f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            lines.append(f'Source: {self.tags_file}')
            lines.append('')
            lines.append('Contains exam-specific Subject-Topic-Subtopic taxonomies:')
            for var_name, data in self.exam_taxonomies.items():
                lines.append(f'  - {var_name}: {data["count"]} unique triplets')
            lines.append('"""')
            lines.append('')
            lines.append('from typing import Dict, List')
            lines.append('')
            lines.append('')

            # Generate constants for each exam
            for var_name, data in self.exam_taxonomies.items():
                lines.append(f'# ===== {var_name} TAXONOMY =====')
                lines.append('')

                # Subjects list
                lines.append(f'{var_name}_SUBJECTS: List[str] = [')
                for subject in data['subjects']:
                    lines.append(f'    "{subject}",')
                lines.append(']')
                lines.append('')

                # Triplets list
                lines.append(f'{var_name}_TRIPLETS: List[str] = [')
                for triplet in data['triplets']:
                    # Escape quotes in triplet strings
                    escaped_triplet = triplet.replace('"', '\\"')
                    lines.append(f'    "{escaped_triplet}",')
                lines.append(']')
                lines.append('')

                # Triplet dictionary
                lines.append(f'{var_name}_TRIPLET_DICT: Dict[str, Dict[str, str]] = {{')
                for triplet, info in data['triplet_dict'].items():
                    escaped_triplet = triplet.replace('"', '\\"')
                    lines.append(f'    "{escaped_triplet}": {{')
                    lines.append(f'        "subject": "{info["subject"]}",')
                    lines.append(f'        "topic": "{info["topic"]}",')
                    lines.append(f'        "subtopic": "{info["subtopic"]}"')
                    lines.append('    },')
                lines.append('}')
                lines.append('')
                lines.append('')

            # Summary statistics
            lines.append('# ===== SUMMARY STATISTICS =====')
            lines.append('TAXONOMY_STATS = {')
            for var_name, count in self.stats['by_exam'].items():
                lines.append(f'    "{var_name}": {count},')
            lines.append('}')
            lines.append('')
            lines.append(f'TOTAL_TRIPLETS = {self.stats["total_triplets"]}')
            lines.append('')

            # Helper function to get taxonomy by exam
            lines.append('# ===== HELPER FUNCTIONS =====')
            lines.append('def get_taxonomy_for_exam(exam_type: str):')
            lines.append('    """Get taxonomy constants for a specific exam type"""')
            lines.append('    exam_map = {')
            lines.append('        "TNPSC": {')
            lines.append('            "subjects": TNPSC_SUBJECTS,')
            lines.append('            "triplets": TNPSC_TRIPLETS,')
            lines.append('            "triplet_dict": TNPSC_TRIPLET_DICT')
            lines.append('        },')
            lines.append('        "Banking": {')
            lines.append('            "subjects": BANKING_SUBJECTS,')
            lines.append('            "triplets": BANKING_TRIPLETS,')
            lines.append('            "triplet_dict": BANKING_TRIPLET_DICT')
            lines.append('        },')
            lines.append('        "SSC-Railways": {')
            lines.append('            "subjects": SSC_RAILWAYS_SUBJECTS,')
            lines.append('            "triplets": SSC_RAILWAYS_TRIPLETS,')
            lines.append('            "triplet_dict": SSC_RAILWAYS_TRIPLET_DICT')
            lines.append('        }')
            lines.append('    }')
            lines.append('    return exam_map.get(exam_type)')
            lines.append('')

            # Write to file
            content = '\n'.join(lines)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Generated {output_file}")
            print(f"   Total size: {len(content)} characters")

            return True

        except Exception as e:
            print(f"Error generating constants file: {e}")
            return False

    def generate_summary_report(self) -> str:
        """Generate summary report"""
        lines = []
        lines.append("=" * 60)
        lines.append("TAXONOMY GENERATION REPORT")
        lines.append("=" * 60)
        lines.append(f"Source file: {self.tags_file}")
        lines.append(f"Total unique triplets: {self.stats['total_triplets']}")
        lines.append("")
        lines.append("BREAKDOWN BY EXAM:")

        for var_name, count in self.stats['by_exam'].items():
            percentage = (count / self.stats['total_triplets'] * 100) if self.stats['total_triplets'] > 0 else 0
            lines.append(f"  {var_name:15s}: {count:5d} triplets ({percentage:5.1f}%)")

        lines.append("=" * 60)
        return "\n".join(lines)

    def run(self) -> bool:
        """
        Run complete generation process

        Returns:
            True if successful, False otherwise
        """
        # Validate tags file
        if not self.validate_tags_file():
            return False

        # Parse all taxonomies
        if not self.parse_all_taxonomies():
            return False

        # Generate constants file
        if not self.generate_constants_file():
            return False

        # Print summary
        print("\n" + self.generate_summary_report())

        return True


def main():
    """Main entry point"""
    print("TAXONOMY CONSTANTS GENERATOR - Exam-Specific")
    print("=" * 60)
    print("Reading exam-specific taxonomies from Tags_New.xlsx...")
    print("=" * 60)
    print()

    # Create generator instance
    generator = TaxonomyGenerator()

    # Run generation
    success = generator.run()

    if success:
        print("\nSUCCESS! Taxonomy constants generated")
        print("\nGenerated file: taxonomy_constants.py")
        print("\nYou can now use these constants in your classification scripts!")
        return 0
    else:
        print("\nFAILED! Check error messages above")
        return 1


if __name__ == "__main__":
    sys.exit(main())
