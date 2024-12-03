# NutriBook Messenger Integration

An integration project between **NutriBook** and various messaging platforms (e.g., WhatsApp, Gmail) to send reminders and notifications to patients.

---

## Features

---

## Project Structure
```plaintext
backend/
│
├── api/
│
├── storage/
│   └── data.json                   # (Placeholder) Storage for calendar and patient data
│
├── .env                            # Environment variables (e.g., API keys, secrets)
├── .gitignore                      # Excludes sensitive and unnecessary files from Git
├── app.py                          # Main Flask application entry point
```

---

## Setup

1. Clone the repository
```bash
git clone <repository-url>
cd backend
```

2. Install dependencies
Make sure you have Python 3.11 installed. Install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

3. Configure environment variables
Create a .env file in the root directory with the required API keys and settings:

```plaintext
FLASK_ENV=development
```

4. Run the application
Start the Flask application:

```bash
python app.py
```
The app will run on http://localhost:5000.

API Endpoints
|Endpoint|Method|Description|
|---|---|---|
