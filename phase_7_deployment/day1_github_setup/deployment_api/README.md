# Deployment Ready Flask API

A simple Flask REST API prepared for deployment as part of Phase 7 — Deployment & Production.

## 📌 Project Overview

This project is a small Flask API used to practice preparing a backend application for production deployment.

The project demonstrates:

* Flask application setup
* API health checking
* Python dependency management
* Git version control
* GitHub repository management
* Deployment preparation

## 🛠️ Technologies

* Python
* Flask
* Git
* GitHub

## 📁 Project Structure

```text
deployment_api/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd deployment_api
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask development server:

```powershell
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

## 🩺 API Health Check

### GET `/health`

Checks whether the API is running.

Example:

```text
GET http://127.0.0.1:5000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

## 🔐 Security

This project does not store secrets directly in the source code.

Sensitive configuration such as secret keys and database credentials should be provided through environment variables in production.

The `.env` file should never be committed to GitHub.

## 🚀 Deployment

This project is being prepared for deployment as part of the Flask Deployment & Production learning phase.

The deployment workflow will eventually be:

```text
Flask Application
       ↓
Git
       ↓
GitHub
       ↓
Render
       ↓
Production Server
       ↓
Public API
```

## 📚 Learning Context

This project belongs to:

```text
Phase 7 — Deployment & Production
Day 1 — GitHub & Deployment Preparation
```

The purpose is educational and focuses on understanding how a Flask application is prepared for production.
