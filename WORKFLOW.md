# Exam-Specific Question Classification Workflow

## Overview

This system classifies competitive exam questions into Chapter-Topic-Subtopic taxonomies using exam-specific AI classification. Each exam (TNPSC, Banking, SSC-Railways) has its own separate taxonomy.

## New Folder Structure

```
htmltagging2/
├── input/              → Only InputExcel.xlsx
├── output/             → SeparatedQuestions.xlsx & ClassifiedQuestions.xlsx
├── temp/               → Progress backups during processing
├── logs/               → processing_errors.log & api_costs.json
├── result/             → Exam-specific result files
└── tags/               → Tags_New.xlsx (exam-specific taxonomies)
```

## Complete Workflow

### Step 1: Prepare Input
Place your input Excel file in `input/InputExcel.xlsx` with columns:
- S No, Chapter, Topic, Subtopic, Questions, OptionA-E, Answer, Explanation

### Step 2: Separate by Exam Type
```bash
python separate_by_exam.py
```

**What it does:**
- Reads `input/InputExcel.xlsx`
- Separates questions into 3 tabs based on OptionE column:
  - **TNPSC**: OptionE = "Answer not known"
  - **Banking**: OptionE has content (but NOT "Answer not known")
  - **SSC-Railways**: OptionE is blank/empty
- Renumbers S No in each tab starting from 1
- Outputs `output/SeparatedQuestions.xlsx` with 3 tabs

**Example output:**
```
TNPSC:        63 questions
Banking:      49 questions
SSC-Railways: 138 questions
Total:        250 questions
```

### Step 3: Generate Taxonomy Constants (One-time setup)
```bash
python generate_taxonomy_constants_by_exam.py
```

**What it does:**
- Reads `tags/Tags_New.xlsx` (3 tabs: TNPSC, Banking, SSCRailways)
- Each tab has: Subject | Topic | Subtopic
- Generates `taxonomy_constants.py` with exam-specific triplets
- Creates lookup dictionaries for fast classification

**Taxonomy Statistics:**
- TNPSC: 623 triplets (8 subjects)
- Banking: 232 triplets (3 subjects)
- SSC-Railways: 669 triplets (6 subjects)
- Total: 1,524 unique triplets

### Step 4: Classify Questions
```bash
python process_separated_excel.py
```

**What it does:**
- Loads `output/SeparatedQuestions.xlsx`
- For each tab, uses exam-specific classifier
- **Single-stage classification**: AI directly selects best triplet from exam-specific options
- Maps Subject → Chapter in output
- Saves progress every 10 questions
- Creates backups every 25 questions
- Tracks API costs and token usage
- Outputs `output/ClassifiedQuestions.xlsx` with all 3 tabs classified

**Processing Details:**
- Each tab processed independently
- No cross-contamination between exams
- Resume capability if interrupted
- Real-time cost tracking
- Detailed error logging

### Step 5: Split by Exam (Optional)
```bash
python split_excel_by_exam.py
```

**What it does:**
- Reads `output/ClassifiedQuestions.xlsx`
- Creates exam-specific files in `result/` folder
- Useful for distributing questions by exam type

## Key Features

### 1. Exam-Specific Taxonomies
- ✅ TNPSC uses only TNPSC taxonomy
- ✅ Banking uses only Banking taxonomy
- ✅ SSC-Railways uses only SSC-Railways taxonomy
- ✅ No mixing between exams

### 2. Single-Stage Classification
- ✅ One API call per question (cost-effective)
- ✅ Directly selects complete triplet
- ✅ Faster than two-stage approach

### 3. Column Mapping
- ✅ Taxonomy has: **Subject** | Topic | Subtopic
- ✅ Output has: **Chapter** | Topic | Subtopic
- ✅ Subject → Chapter mapping is automatic

### 4. Progress & Recovery
- ✅ Auto-save every 10 questions
- ✅ Backup every 25 questions (in `temp/` folder)
- ✅ Resume from interruption
- ✅ Graceful shutdown (Ctrl+C)

### 5. Cost Management
- ✅ Real-time cost tracking
- ✅ Budget limits
- ✅ Automatic fallback to Ollama if budget exceeded
- ✅ Detailed cost reports in `logs/api_costs.json`

## Cost Estimates

Using OpenAI GPT-4o mini:
- ~$0.054 per 1,000 questions (~₹54)
- ~$0.0054 per 100 questions (~₹5.40)
- Single-stage = 50% cheaper than two-stage

**Example:**
- 250 questions ≈ $0.0135 (₹1.15)
- 1,000 questions ≈ $0.054 (₹54)
- Default budget: $10 (can process ~18,500 questions)

## File Descriptions

### Core Scripts
- `separate_by_exam.py` - Separates input by exam type (step 1)
- `generate_taxonomy_constants_by_exam.py` - Generates taxonomy (one-time)
- `process_separated_excel.py` - Main classification script (step 2)
- `split_excel_by_exam.py` - Splits result by exam (optional)

### Support Modules
- `exam_specific_classifier.py` - Single-stage exam-specific classifier
- `multi_tab_excel_processor.py` - Handles multi-tab Excel files
- `taxonomy_constants.py` - Generated exam-specific taxonomies
- `cost_tracker.py` - Tracks OpenAI API costs
- `openai_client.py` - OpenAI API wrapper
- `ollama_client.py` - Ollama fallback client
- `config.py` - Configuration settings

### Legacy Files (Not Used)
- `question_classifier.py` - Old two-stage classifier
- `exam_taxonomy_mapper.py` - Old unified taxonomy mapper
- `excel_processor.py` - Old single-tab processor

## Configuration

Edit `config.py` to customize:
- OpenAI budget limits
- Save intervals
- Model selection (GPT-4o mini by default)
- Timeout settings
- Fallback behavior

## Troubleshooting

### Issue: "Tags file not found"
**Solution:** Ensure `tags/Tags_New.xlsx` exists with tabs: TNPSC, Banking, SSCRailways

### Issue: "Budget exceeded"
**Solution:**
1. Check `logs/api_costs.json` for usage
2. Increase budget in `config.py` or `.env`
3. System will auto-fallback to Ollama (free)

### Issue: "Classification failed"
**Solution:**
1. Check `logs/processing_errors.log`
2. Verify OpenAI API key in `.env`
3. Check internet connection
4. Ensure Ollama is running for fallback

### Issue: "Tab not found"
**Solution:** Run `separate_by_exam.py` first to create SeparatedQuestions.xlsx

## Quick Start

```bash
# 1. Separate by exam
python separate_by_exam.py

# 2. Generate taxonomies (one-time)
python generate_taxonomy_constants_by_exam.py

# 3. Classify questions
python process_separated_excel.py

# 4. (Optional) Split results
python split_excel_by_exam.py
```

## Environment Variables

Create `.env` file:
```
OPENAI_API_KEY=sk-proj-...
OPENAI_BUDGET_LIMIT=10.0
OPENAI_MODEL=gpt-4o-mini
PRIMARY_PROVIDER=openai
```

## Output Format

**ClassifiedQuestions.xlsx** contains 3 tabs:
- TNPSC (with Chapter/Topic/Subtopic filled)
- Banking (with Chapter/Topic/Subtopic filled)
- SSC-Railways (with Chapter/Topic/Subtopic filled)

Each row has:
- S No (renumbered per tab)
- Chapter (mapped from Subject)
- Topic
- Subtopic
- Questions
- OptionA-E
- Answer
- Explanation

## Support

For issues or questions:
1. Check `logs/processing_errors.log`
2. Review `logs/api_costs.json` for cost tracking
3. Verify input file structure matches expected columns
