#  Kurdish Student E-Learning Buddy Backend

An AI-powered e-learning backend built with Django REST Framework and the Google Gemini API (`gemini-3.6-flash`).
## ✨ Features

- **🚀 Automated Flashcard Generation**: Simply paste your study text, and the AI generates key questions and answers.
- **🌍 Multi-language Support**: Fully supports **English** and **Kurdish** text processing.
- **⚡ RESTful API**: Built on Django REST Framework for seamless integration with web and mobile frontends.
- **🤖 Powered by Gemini**: Utilizes Google's latest generative models for high-quality content extraction.

## 🛠️ Tech Stack

- **Backend**: [Django](https://www.djangoproject.com/) & [Django REST Framework](https://www.django-rest-framework.org/)
- **AI Engine**: [Google Generative AI (Gemini)](https://ai.google.dev/)
- **Environment Management**: `python-dotenv`
- **Database**: SQLite (Default)

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A Google AI (Gemini) API Key. Get one at [Google AI Studio](https://aistudio.google.com/).

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd new_project_learning
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

## 📡 API Usage

### Study Materials

- **GET** `/learning/materials/`: List all your study materials.
- **POST** `/learning/materials/`: Create new material and auto-generate flashcards.
  - Body: `{"title": "Biology Notes", "source_text": "Photosynthesis is the process..."}`
- **GET** `/learning/materials/{id}/`: Retrieve specific material and its flashcards.
- **POST** `/learning/materials/{id}/regenerate/`: Delete existing flashcards and generate new ones for the same material.

---