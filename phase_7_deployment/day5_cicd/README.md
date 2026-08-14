# Phase 7 — Day 5 — CI/CD

## Overview

This project demonstrates a basic Continuous Integration and Continuous Deployment (CI/CD) workflow for a Flask API.

The goal is to connect:

```text
Git
 ↓
GitHub
 ↓
GitHub Actions
 ↓
Automated Tests
 ↓
Render
 ↓
Live Flask API
```

The project is a practice implementation created as part of Phase 7 — Deployment & Production.

---

## Project Structure

```text
day5_cicd/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── tests/
│   └── test_app.py
│
├── app.py
├── requirements.txt
├── deployment_workflow.md
├── notes.md
└── README.md
```

---

## Flask API

The application contains two endpoints.

### Health Check

```text
GET /health
```

Response:

```json
{
    "status": "healthy"
}
```

### Home

```text
GET /
```

Response:

```json
{
    "message": "Flask API is running"
}
```

---

## Running Locally

Activate the virtual environment:

```powershell
.\..\..\venv\Scripts\Activate.ps1
```

Run the Flask application:

```powershell
python app.py
```

The API can then be accessed locally through the Flask development server.

---

## Running Tests

Tests are written using `pytest`.

Run:

```powershell
python -m pytest
```

The project was successfully tested with:

```text
2 passed
```

`python -m pytest` is used because it correctly resolves the project root when running the tests from this directory.

---

## CI/CD Workflow

The GitHub Actions workflow performs the following steps:

```text
Push to main
    ↓
Checkout repository
    ↓
Set up Python 3.12
    ↓
Install dependencies
    ↓
Run pytest
    ↓
Tests pass
    ↓
Trigger Render deployment
```

The Render deployment hook is stored securely as a GitHub Actions repository secret.

The secret name used by the workflow is:

```text
RENDER_DEPLOY_HOOK
```

The actual secret value is never stored in the repository.

---

## Production Deployment

The Flask API is deployed on Render.

Render runs the application using a production WSGI server such as Gunicorn.

The overall production flow is:

```text
GitHub
   ↓
GitHub Actions
   ↓
pytest
   ↓
Render
   ↓
Gunicorn
   ↓
Flask API
```

---

## Security

Sensitive values should not be committed to GitHub.

Examples include:

```text
.env
DATABASE_URL
SECRET_KEY
API keys
Deployment hooks
```

Sensitive CI/CD values are stored using GitHub Secrets.

The Render deployment hook is therefore referenced in the workflow through:

```text
${{ secrets.RENDER_DEPLOY_HOOK }}
```

rather than storing the actual deployment URL in the YAML file.

---

## Technologies Used

* Python
* Flask
* pytest
* Git
* GitHub
* GitHub Actions
* Render
* Gunicorn
* PowerShell

---

## Phase 7 Connection

This project represents the final CI/CD stage of Phase 7:

```text
Phase 7
Deployment & Production
        ↓
Day 1 — GitHub
        ↓
Day 2 — Render
        ↓
Day 3 — PostgreSQL
        ↓
Day 4 — Production Configuration & Testing
        ↓
Day 5 — CI/CD
```

---

## Learning Outcome

After completing this project, the main workflow understood is:

```text
Developer
    ↓
Code Change
    ↓
git commit
    ↓
git push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Automated Tests
    ↓
PASS
    ↓
Render Deployment
    ↓
Live API
```

This completes the core CI/CD concepts covered in Phase 7.
