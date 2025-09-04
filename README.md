# HTML to Excel Question Extractor

A Python script that extracts questions from HTML files and converts them into a well-formatted Excel spreadsheet.

## Features

- Extracts questions from HTML files with specific formatting
- Separates questions and options into different columns
- Cleans HTML tags and special characters
- Outputs clean, readable text in Excel format
- Auto-adjusts column widths for better readability

## Requirements

- Python 3.x
- BeautifulSoup4
- pandas
- openpyxl

## Installation

1. Clone the repository
2. Install required packages:
```bash
pip install beautifulsoup4 pandas openpyxl
```

## Usage

1. Place your HTML file in the `input/` folder
2. Run the script:
```bash
python extract_questions.py
```
3. Find the output Excel file in the `output/` folder

## Output Format

The Excel file contains three columns:
- **S No**: Serial number (1, 2, 3...)
- **Question**: The question text including any statements (I, II, III, etc.)
- **Options**: All options combined (e.g., "a) Option1, b) Option2, c) Option3...")

## File Structure

```
htmltotagging/
├── extract_questions.py    # Main script
├── input/                 # Place HTML files here
├── output/                # Excel files will be saved here
└── README.md             # This file
```