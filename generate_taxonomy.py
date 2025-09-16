#!/usr/bin/env python3
"""
Generate Taxonomy Files from Subject-Topic-Subtopic.xlsx
Creates all necessary taxonomy files in the taxonomy/ folder
"""

import json
import csv
import os
import pandas as pd
from datetime import datetime
from collections import defaultdict

def generate_taxonomy_from_excel(excel_file="Subject-Topic-Subtopic.xlsx", exclude_miscellaneous=True):
    """Generate taxonomy files from Excel file"""
    
    # Create taxonomy directory
    os.makedirs("taxonomy", exist_ok=True)
    
    print(f"📚 Reading Excel file: {excel_file}")
    df = pd.read_excel(excel_file)
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Expected columns: SUBJECT, TOPIC, SUB TOPIC
    if not all(col in df.columns for col in ['SUBJECT', 'TOPIC', 'SUB TOPIC']):
        raise ValueError("Excel file must have columns: SUBJECT, TOPIC, SUB TOPIC")
    
    # Rename columns for consistency
    df = df.rename(columns={'SUBJECT': 'Subject', 'TOPIC': 'Topic', 'SUB TOPIC': 'Subtopic'})
    
    # Clean the data
    df['Subject'] = df['Subject'].fillna('').str.strip()
    df['Topic'] = df['Topic'].fillna('').str.strip()
    df['Subtopic'] = df['Subtopic'].fillna('').str.strip()
    
    # Remove empty rows
    df = df[df['Subject'] != '']
    
    # Filter out miscellaneous if requested
    if exclude_miscellaneous:
        print("🔍 Filtering out miscellaneous entries...")
        before_count = len(df)
        df = df[~df['Subject'].str.lower().eq('miscellaneous')]
        df = df[~df['Topic'].str.lower().eq('miscellaneous')]
        df = df[~df['Subtopic'].str.lower().eq('miscellaneous')]
        after_count = len(df)
        print(f"   Removed {before_count - after_count} miscellaneous entries")
    
    # Generate different taxonomy formats
    print("\n📝 Generating taxonomy files...")
    
    # 1. Flattened JSON format
    flattened_data = []
    for idx, row in df.iterrows():
        flattened_data.append({
            "Subject": row['Subject'],
            "Topic": row['Topic'],
            "Subtopic": row['Subtopic'],
            "Full_Path": f"{row['Subject']} > {row['Topic']} > {row['Subtopic']}"
        })
    
    with open('taxonomy/taxonomy_flattened.json', 'w', encoding='utf-8') as f:
        json.dump(flattened_data, f, indent=2, ensure_ascii=False)
    print("✅ Created taxonomy_flattened.json")
    
    # 2. Hierarchical format
    hierarchy = defaultdict(lambda: defaultdict(list))
    for _, row in df.iterrows():
        if row['Subtopic'] not in hierarchy[row['Subject']][row['Topic']]:
            hierarchy[row['Subject']][row['Topic']].append(row['Subtopic'])
    
    # Get unique subjects
    subjects = sorted(df['Subject'].unique().tolist())
    
    # 3. Complete JSON format
    complete_data = {
        "metadata": {
            "total_subjects": len(subjects),
            "total_combinations": len(df),
            "description": "Educational taxonomy for question classification",
            "generated_from": excel_file,
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "miscellaneous_excluded": exclude_miscellaneous
        },
        "subjects": subjects,
        "hierarchy": dict(hierarchy)
    }
    
    with open('taxonomy/taxonomy_complete.json', 'w', encoding='utf-8') as f:
        json.dump(complete_data, f, indent=2, ensure_ascii=False)
    print("✅ Created taxonomy_complete.json")
    
    # 4. Alternative hierarchical format
    hierarchical_data = {
        "subjects": []
    }
    
    for subject in subjects:
        subject_data = {
            "name": subject,
            "topics": []
        }
        
        for topic in sorted(hierarchy[subject].keys()):
            topic_data = {
                "name": topic,
                "subtopics": sorted(hierarchy[subject][topic])
            }
            subject_data["topics"].append(topic_data)
        
        hierarchical_data["subjects"].append(subject_data)
    
    with open('taxonomy/taxonomy_hierarchical.json', 'w', encoding='utf-8') as f:
        json.dump(hierarchical_data, f, indent=2, ensure_ascii=False)
    print("✅ Created taxonomy_hierarchical.json")
    
    # 5. CSV format
    with open('taxonomy/taxonomy_flattened.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Subject', 'Topic', 'Subtopic', 'Full_Path'])
        writer.writeheader()
        writer.writerows(flattened_data)
    print("✅ Created taxonomy_flattened.csv")
    
    # 6. Summary text file
    summary_lines = [
        "TAXONOMY SUMMARY",
        "=" * 50,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Source: {excel_file}",
        f"Miscellaneous Excluded: {'Yes' if exclude_miscellaneous else 'No'}",
        "",
        f"Total Subjects: {len(subjects)}",
        f"Total Combinations: {len(df)}",
        "",
        "SUBJECTS:",
        "-" * 20
    ]
    
    for i, subject in enumerate(subjects, 1):
        subject_count = len(df[df['Subject'] == subject])
        summary_lines.append(f"{i}. {subject} ({subject_count} combinations)")
    
    summary_lines.extend([
        "",
        "STATISTICS BY SUBJECT:",
        "-" * 20
    ])
    
    for subject in subjects:
        subject_df = df[df['Subject'] == subject]
        topic_count = subject_df['Topic'].nunique()
        summary_lines.append(f"{subject}: {topic_count} topics, {len(subject_df)} total combinations")
    
    with open('taxonomy/taxonomy_summary.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary_lines))
    print("✅ Created taxonomy_summary.txt")
    
    # Print summary
    print("\n📊 TAXONOMY GENERATION COMPLETE")
    print("=" * 50)
    print(f"Total Subjects: {len(subjects)}")
    print(f"Total Combinations: {len(df)}")
    print(f"Files created in taxonomy/ folder:")
    print("  - taxonomy_flattened.json")
    print("  - taxonomy_complete.json")
    print("  - taxonomy_hierarchical.json")
    print("  - taxonomy_flattened.csv")
    print("  - taxonomy_summary.txt")
    
    return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate taxonomy files from Excel")
    parser.add_argument("--excel", default="Subject-Topic-Subtopic.xlsx", help="Excel file path")
    parser.add_argument("--include-miscellaneous", action="store_true", help="Include miscellaneous entries")
    
    args = parser.parse_args()
    
    try:
        generate_taxonomy_from_excel(
            excel_file=args.excel,
            exclude_miscellaneous=not args.include_miscellaneous
        )
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)