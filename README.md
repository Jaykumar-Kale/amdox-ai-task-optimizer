# Amdox AI-Powered Task Optimizer

 **Live Application:**  
https://amdox-ai-task-optimizer.streamlit.app/

---

## Project Overview

The **Amdox AI-Powered Task Optimizer** is an intelligent web application that analyzes employee emotions from textual input and recommends suitable tasks based on their emotional state.

The system aims to improve **employee well-being, productivity, and early stress detection** in organizations by leveraging **advanced Natural Language Processing (NLP)** techniques.

This project was developed as part of the **Amdox Data Science Internship Program**, focusing on applying AI to real-world workplace problems.

---

## Problem Statement

In modern workplaces, employee stress, burnout, and disengagement often go unnoticed until productivity declines. Traditional management systems lack real-time emotional insights.

This project addresses the problem by:
- Detecting employee emotions from text
- Recommending tasks aligned with emotional state
- Raising alerts for stress and burnout
- Supporting empathetic and data-driven decision-making

---

## Key Features

### Emotion Detection from Text
- Analyzes free-form employee messages
- Detects emotions such as **Happy, Calm, Angry, Sad, and Stress**
- Uses a **pretrained transformer-based NLP model**

### Intelligent Task Recommendation
- Maps emotions to appropriate workplace actions:
  - **Happy** → Creative or leadership tasks
  - **Calm** → Planning or analytical work
  - **Angry** → Solo tasks and cooldown time
  - **Sad** → Light tasks or team discussions

### Stress & Burnout Alert
- Identifies stress-related emotions
- Displays an **HR alert** for early intervention

### Interactive User Interface
- Clean and modern UI built with Streamlit
- Example input buttons for quick testing
- Real-time emotion analysis with loading indicators

### Privacy-Friendly Design
- No data storage
- Text is processed only during runtime

---

## Technology Stack

| Category | Tools / Libraries |
|--------|------------------|
| Programming Language | Python |
| Frontend | Streamlit |
| NLP Model | Hugging Face Transformers |
| ML Framework | PyTorch |
| Model Used | `j-hartmann/emotion-english-distilroberta-base` |
| Deployment | Streamlit Cloud |

---

## System Architecture (High-Level)

1. User enters an employee message
2. Text is processed by a pretrained transformer model
3. Emotion is detected from the text
4. Emotion is mapped to a task recommendation
5. Stress-related emotions trigger an HR alert
6. Results are displayed in real time

---

## Example Inputs & Outputs

| Input Text | Detected Emotion | Action |
|-----------|----------------|--------|
| I feel calm and focused today | CALM | Planning tasks |
| I feel frustrated with unrealistic deadlines | ANGRY | Solo tasks |
| I am anxious and mentally exhausted | STRESS | HR Alert |
| I am excited and motivated | HAPPY | Creative tasks |

---

## Live Demo

Access the deployed application here:  
 https://amdox-ai-task-optimizer.streamlit.app/

---

## Installation & Local Setup

```bash
# Clone the repository
git clone https://github.com/Jaykumar-Kale/amdox-ai-task-optimizer.git
cd amdox-ai-task-optimizer

# Create virtual environment
py -3.12 -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
