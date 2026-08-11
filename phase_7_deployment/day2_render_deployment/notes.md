# Day 2 — Deploy Flask API on Render

## 🎯 Goal

Deploy a Flask REST API to the internet using Render and a production WSGI server.

By the end of Day 2, the API should be accessible through a public URL.

---

# 1. What is Cloud Hosting?

Cloud hosting means running an application on a remote server connected to the internet.

### Local Development

```text
Your Computer
     ↓
   Python
     ↓
   Flask
     ↓
 localhost
```

Example:

```text
http://127.0.0.1:5000
```

Only the local development environment can normally access this address.

### Cloud Deployment

```text
Internet
    ↓
Cloud Server
    ↓
Flask Application
    ↓
Public URL
```

Example:

```text
https://your-api.onrender.com
```

---

# 2. What is Render?

Render is a cloud platform that can host web applications and backend services.

For this project, Render will:

1. Connect to our GitHub repository.
2. Download the project.
3. Install the dependencies.
4. Start the Flask application.
5. Provide a public URL.
6. Redeploy when new code is pushed.

Basic workflow:

```text
Local Project
      ↓
    Git
      ↓
   GitHub
      ↓
   Render
      ↓
   Build
      ↓
   Deploy
      ↓
 Live API
```

---

# 3. Web Service

A Render Web Service is used to run an application that receives HTTP requests.

Our Flask API will run as a Web Service.

Example:

```text
Client
  ↓
HTTP Request
  ↓
Render Web Service
  ↓
Flask
  ↓
Response
```

---

# 4. Development Server vs Production Server

During development, Flask can be started using:

```bash
python app.py
```

This uses Flask's development server.

The development server is intended for local development and testing.

For production, we use a WSGI server such as Gunicorn.

```text
Development

python app.py
      ↓
Flask Development Server
```

```text
Production

Gunicorn
   ↓
Flask Application
```

---

# 5. What is WSGI?

WSGI stands for:

**Web Server Gateway Interface**

It defines how a Python web application communicates with a web server.

The basic relationship is:

```text
HTTP Request
      ↓
   Gunicorn
      ↓
     WSGI
      ↓
    Flask
      ↓
HTTP Response
```

Flask provides a WSGI application.

Example:

```python
from flask import Flask

app = Flask(__name__)
```

Gunicorn can load this application using:

```bash
gunicorn app:app
```

The first `app` means the Python module:

```text
app.py
```

The second `app` means the Flask application object:

```python
app = Flask(__name__)
```

---

# 6. What is Gunicorn?

Gunicorn is a Python WSGI HTTP server commonly used to run Python web applications in production.

Instead of:

```bash
python app.py
```

production can use:

```bash
gunicorn app:app
```

The command follows:

```text
gunicorn <module>:<application>
```

For:

```text
app.py
```

containing:

```python
app = Flask(__name__)
```

the command is:

```bash
gunicorn app:app
```

---

# 7. Build Command

A build command installs the dependencies required by the application.

For Python applications, a common command is:

```bash
pip install -r requirements.txt
```

The deployment process is therefore:

```text
GitHub Repository
       ↓
Clone Project
       ↓
Install requirements
       ↓
Start Application
```

---

# 8. Start Command

The start command tells Render how to run the application.

For our Flask API:

```bash
gunicorn app:app
```

This starts the Flask application using Gunicorn.

---

# 9. Deployment Logs

Deployment logs show what happens while Render builds and starts the application.

Logs can help identify:

* Missing packages
* Python errors
* Incorrect start commands
* Port problems
* Import errors
* Configuration problems

Example workflow:

```text
Deployment Failed
       ↓
Read Logs
       ↓
Find Error
       ↓
Fix Code
       ↓
Commit
       ↓
Push
       ↓
Render Deploys Again
```

---

# 10. Task API

For the Day 2 mini project, we will create a simple Task API.

## GET /tasks

Returns the available tasks.

Example:

```http
GET /tasks
```

Response:

```json
[
  {
    "id": 1,
    "title": "Learn Flask",
    "completed": false
  }
]
```

---

## POST /tasks

Creates a new task.

Example request:

```json
{
  "title": "Deploy Flask API"
}
```

Example response:

```json
{
  "id": 2,
  "title": "Deploy Flask API",
  "completed": false
}
```

---

# 11. Local Testing

Before deployment, always test locally.

Start the application:

```bash
python app.py
```

Then test:

```text
GET http://127.0.0.1:5000/tasks
```

After confirming the API works, push the code to GitHub.

---

# 12. Deployment Workflow

```text
Flask API
    ↓
Test Locally
    ↓
requirements.txt
    ↓
Git Commit
    ↓
GitHub
    ↓
Connect Repository to Render
    ↓
Configure Build Command
    ↓
Configure Start Command
    ↓
Deploy
    ↓
Deployment Logs
    ↓
Public URL
    ↓
Test Live API
```

---

# 🧠 Key Takeaways

* Cloud hosting makes an application accessible over the internet.
* Render can host Flask Web Services.
* Flask's development server is for development.
* Gunicorn is used to run Flask in production.
* WSGI connects the Python web application to the server.
* `requirements.txt` provides the required dependencies.
* Render uses build and start commands during deployment.
* Deployment logs help diagnose production problems.
* Always test the API locally before deployment.
