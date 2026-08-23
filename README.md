# Python Roadmap to AI Engineer

This repository provides a structured, hands-on learning path to become an AI Engineer using Python. Each module builds upon previous concepts, culminating in practical AI/ML applications.

## 📚 Learning Path Overview

### Phase 1: Python Foundation (Complete) ✅
```plaintext
- Variables & Data Types
- Control Flow (if/else, loops)
- Data Structures (Lists, Dictionaries)
- Functions & File Operations (JSON)
- Web API Consumption
```
*Files in `src/` cover these topics*

### Phase 2: Core Python for AI 🔧
```plaintext
- Object-Oriented Programming (OOP)
- Error Handling & Logging
- Advanced Python Features
- Data Manipulation (NumPy, Pandas)
- Data Visualization (Matplotlib, Seaborn)
```
*New files to be added*

### Phase 3: AI/ML Fundamentals 🤖
```plaintext
- Machine Learning with scikit-learn
- Natural Language Processing (NLTK, spaCy)
- Computer Vision Basics (OpenCV)
- Deep Learning Foundations (TensorFlow/PyTorch)
```
*New files to be added*

### Phase 4: AI Engineering Practice 🚀
```plaintext
- LLM APIs & Prompt Engineering
- Model Deployment (Flask/FastAPI)
- MLOps Basics (Version Control, Testing)
- Capstone Projects
```
*New files to be added*

## 🎯 Key Skills You'll Gain
1. **Python Mastery** - From basics to advanced concepts
2. **Data Handling** - Clean, manipulate, and visualize data
3. **AI/ML Implementation** - Build models from scratch and using libraries
4. **LLM Integration** - Work with modern language models
5. **Deployment Skills** - Deploy models as APIs
6. **Project Portfolio** - 5+ hands-on projects for your resume

## 🛠️ Getting Started
1. Install Python 3.8+
2. Clone this repository
3. Follow the phases in order
4. Complete the exercises in each file
5. Build the capstone projects

## 📁 File Structure
```
src/
├── Variables.py              # Phase 1: Variables & Input
├── Listdictionary.py         # Phase 1: Lists & Dictionaries  
├── Controlflow.py            # Phase 1: Control Flow
├── pythonloops.py            # Phase 1: Loops
├── FuctionsFile operations.py # Phase 1: Functions & Files
├── webapidatafetchingautomation.py # Phase 1: Web APIs
├── oop_fundamentals.py       # Phase 2: Object-Oriented Programming
├── data_manipulation.py      # Phase 2: NumPy & Pandas
├── data_visualization.py     # Phase 2: Plotting & Visualization
├── ml_fundamentals.py        # Phase 3: Machine Learning Basics
├── llm_integration.py        # Phase 4: LLM APIs & Prompt Engineering
└── model_deployment.py       # Phase 4: Deploying ML Models
```

## 🏆 Capstone Projects
By completing this roadmap, you'll build:
1. **Expense Tracker** (Phase 1) - Personal finance CLI app
2. **Data Analysis Dashboard** (Phase 2) - Visualize datasets
3. **Email Spam Classifier** (Phase 3) - ML model for text classification
4. **Chatbot with Memory** (Phase 4) - Conversational AI with context
5. **Image Recognition API** (Phase 4) - Deploy CV model as REST service

## 📈 Suggested Timeline
- **Phase 1**: 1-2 weeks (Review existing files)
- **Phase 2**: 3-4 weeks (New files + practice)
- **Phase 3**: 4-5 weeks (ML concepts + projects)
- **Phase 4**: 3-4 weeks (LLMs + deployment + capstone)

**Total**: 11-15 weeks part-time (10-15 hours/week)

## 🔗 Resources & References
- Official Python Documentation
- NumPy, Pandas, Matplotlib docs
- scikit-learn user guide
- Hugging Face Course (NLP)
- FastAPI/TensorFlow documentation
- Git & GitHub tutorials

---
*Start with Phase 1 by exploring the existing `src/` files, then progress through each phase systematically!*

## 🎯 Python Coding Standards
Consistent code style makes this repo easier to learn from and maintain. Follow these guidelines:

### Naming Conventions
- **Variables**: `snake_case` (e.g., `user_name`, `total_hours`)
- **Functions**: `snake_case` with descriptive names (e.g., `calculate_total()`, `fetch_api_data()`)
- **Classes**: `PascalCase` (e.g., `class BankAccount:`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES = 3`)

### Code Formatting
- **Indentation**: 4 spaces per indent level (never tabs)
- **Line length**: Keep lines under 88 characters when possible
- **Blank lines**: Two blank lines before top-level function/class definitions, one blank line between methods in a class
- **Imports**: Standard library first, third-party second, local imports last
  ```python
  import json        # stdlib
  import pandas as pd # third-party
  from src.variables import load_data # local
  ```

### Comments & Documentation
- **Docstrings**: Use triple-quoted docstrings for all functions/classes following NumPy format
- **Inline comments**: Explain *why*, not *what* (the code already shows what)
- **TODO/FIXME**: Use `TODO()` for future work, `FIXME()` for bugs needing attention
  ```python
  # TODO: Add error handling for network failures
  # FIXME: This causes crash when input is negative
  ```

### Error Handling
- Use `try/except` blocks for operations that can fail
- Catch specific exceptions, not bare `except:`
- Log meaningful error messages (covered in later phases)

### Code Quality
- Keep functions focused on one task (Single Responsibility Principle)
- Return values instead of printing inside functions when possible
- Use type hints for function parameters/returns (Phase 3+)

## 🏩 Git Best Practices

Maintain a clean and trackable repository with these Git habits:

### Commit Messages
- Use imperative tense: "Fix bug", not "Fixed bug"
- Include scope (e.g., "src/Controlflow.py") and purpose
- Keep it concise: max 50 chars for basic commits

### Committing Habits
- Commit small changes frequently
- Never commit debug prints/temporary code
- Use branch for experiments before merging to main

### Repository Hygiene
- Add `.gitignore` for: __pycache__, .env, logs, .pytest_cache
- Never commit secrets (e.g., API keys)
- Run "git lint" checks periodically

### Branching Strategy
- Main branch for stable code
- Feature branches for new work (delete after merge)
- Use meaningful branch names: `feat-login-form", not "fix1"

### Push Discipline
- Commit changes to main weekly minimum
- Push before restarting development session
- Use "git push --force-with-license" when needed

```
# .gitignore template
__pycache__/
.env
*.log
.pytest_cache/
```