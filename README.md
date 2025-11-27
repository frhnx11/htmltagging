# Question Classification System

AI-powered question classification system with dual provider support (OpenAI + Ollama fallback).

## 🚀 Quick Start

### 1. Setup
```bash
# Install dependencies
pip install openai python-dotenv pandas openpyxl beautifulsoup4 requests

# Set your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### 2. Prepare Input
- Place your Excel file with questions in: `input/InputExcel.xlsx`
- Required columns: S No, QuestionTypeCode, Exam, Chapter, Topic, Subtopic, Question, OptionA-F, Answer, Explanation

### 3. Run Classification
```bash
python process_input_excel.py
```

### 4. Get Results
- Classified questions: `output/ClassifiedQuestions.xlsx`
- Cost tracking: `output/api_costs.json`
- Processing logs: `output/processing_errors.log`

## 📁 Folder Structure

```
htmltagging2/
├── input/
│   └── InputExcel.xlsx          # Your questions (input)
├── output/
│   ├── ClassifiedQuestions.xlsx # Classified results (output)
│   ├── api_costs.json          # Cost tracking
│   └── *.log                   # Processing logs
├── .env                        # API keys (keep secure)
└── *.py                        # System files
```

## 💰 Cost Information

**OpenAI GPT-4o mini pricing:**
- ~₹54 for 1000 questions
- ~₹5.40 for 100 questions  
- Real-time cost tracking included

**Budget protection:**
- Default limit: $10 USD
- Automatic alerts at 80% usage
- Auto-fallback to free Ollama when budget exceeded

## 🔄 Split by Exam

After classification, split into separate exam files:

```bash
python split_excel_by_exam.py
```

Creates separate tabs for each exam in: `output/exam_files/ExamQuestions_ByTabs.xlsx`

## ⚙️ Configuration

Edit `config.py` to adjust:
- Budget limits
- AI model selection  
- Provider preferences
- Processing settings

## 🛠️ Troubleshooting

**OpenAI Issues:**
- Check API key in `.env` file
- Verify account has credits
- Install: `pip install openai`

**Ollama Fallback:**
- Optional: Install Ollama locally
- System works with OpenAI only

**File Issues:**
- Ensure `input/` folder exists
- Check Excel file format and columns
- Verify write permissions to `output/` folder