# Advanced EQ Assessment System

A professional, Django-based web application to assess Emotional Intelligence (EQ) using rule-based scenarios and NLP-powered sentiment analysis.

## Features
- **Dynamic Scenarios**: Generates context-aware situations based on user profession and age.
- **NLP Analysis**: Uses fine-tuned models (distilbert-base-uncased) to ensure high-accuracy sentiment analysis of user responses.
- **Visual Reports**: Provides radar charts and detailed breakdowns of EQ dimensions.
- **Clean Architecture**: Built with strict OOP principles and separation of concerns.

## Tech Stack
- **Backend**: Python 3.9+, Django
- **AI/ML**: Hugging Face Transformers
- **Frontend**: HTML5, CSS3 (Glassmorphism), Chart.js

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Database**
   ```bash
   python manage.py migrate
   ```

3. **Run Server**
   ```bash
   python manage.py runserver
   ```
   Access at `http://127.0.0.1:8000`.

## Project Structure
- `assessment/logic.py`: Core `AdvancedEQAssessmentModel` class.
- `assessment/views.py`: Request handling and flow control.
- `assessment/models.py`: Database schema for results.
- `templates/`: Frontend HTML templates.
