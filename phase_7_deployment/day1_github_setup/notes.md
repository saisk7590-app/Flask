# Day 1 — GitHub & Deployment Preparation

## 🎯 Goal

Prepare a Flask backend project for deployment by learning Git, GitHub, project configuration, and production preparation.

---

# 1. What is Deployment?

Deployment means making an application available on a server so that users or other applications can access it through the internet.

### Local Environment

```text
Developer Computer
       ↓
     Flask
       ↓
   localhost
```

Example:

```text
http://127.0.0.1:5000
```

### Production Environment

```text
Internet
    ↓
Cloud Server
    ↓
Flask Application
    ↓
Database
```

Example:

```text
https://your-api.onrender.com
```

---

# 2. Local vs Production

## Development Environment

Used while building and testing the application.

Typical characteristics:

* Runs on the developer's computer
* Uses localhost
* Debugging is enabled
* Development database may be used
* Code changes are tested locally

## Production Environment

Used when the application is available to real users.

Typical characteristics:

* Runs on a cloud/server
* Accessible through the internet
* Debug mode should be disabled
* Production database is used
* Secrets are stored using environment variables
* Application should use a production WSGI server such as Gunicorn

---

# 3. What is Git?

Git is a distributed version control system.

It tracks changes made to source code.

Instead of manually keeping multiple copies of a project, Git allows us to maintain a history of changes.

Example:

```text
Project
   ↓
Git Repository
   ↓
Commit 1
   ↓
Commit 2
   ↓
Commit 3
```

A commit represents a saved version of the project.

---

# 4. What is GitHub?

GitHub is an online platform for hosting Git repositories.

Basic workflow:

```text
Local Project
      ↓
     Git
      ↓
Git Repository
      ↓
    GitHub
```

GitHub provides:

* Remote code storage
* Collaboration
* Pull requests
* Issues
* Code review
* GitHub Actions
* CI/CD integration

---

# 5. Git vs GitHub

| Git                    | GitHub                                   |
| ---------------------- | ---------------------------------------- |
| Version control system | Online Git hosting platform              |
| Runs locally           | Runs online                              |
| Tracks code changes    | Stores and shares repositories           |
| Creates commits        | Hosts repositories                       |
| Works without GitHub   | Usually used with Git for remote storage |

---

# 6. Important Git Commands

### Initialize repository

```bash
git init
```

### Check repository status

```bash
git status
```

### Add files

```bash
git add .
```

### Create a commit

```bash
git commit -m "Prepare Flask API for deployment"
```

### Add remote repository

```bash
git remote add origin <repository-url>
```

### Push code

```bash
git push -u origin main
```

---

# 7. What is requirements.txt?

`requirements.txt` contains the Python packages required by the project.

Example:

```text
Flask
gunicorn
```

A deployment server can install these dependencies using:

```bash
pip install -r requirements.txt
```

This allows the production environment to install the packages required by the application.

---

# 8. What is .gitignore?

`.gitignore` tells Git which files and folders should not be tracked.

Common examples:

```text
__pycache__/
*.pyc
venv/
.venv/
.env
*.db
```

Sensitive files such as `.env` should not be pushed to GitHub.

---

# 9. Environment Variables

Environment variables allow configuration and secrets to be stored outside the source code.

Bad:

```python
SECRET_KEY = "my-secret-key"
```

Better:

```python
import os

SECRET_KEY = os.getenv("SECRET_KEY")
```

Environment variables will be covered in detail on Day 4.

---

# 10. README.md

A README explains what a project does and how to use it.

A backend README commonly contains:

* Project description
* Technologies used
* Installation instructions
* How to run the application
* API endpoints
* Configuration information
* Deployment information

---

# 11. Production Preparation

Before deployment, the project should:

* Have a clean structure
* Have a `requirements.txt`
* Have a `.gitignore`
* Have a README
* Avoid hardcoded secrets
* Run successfully locally
* Be stored in Git
* Be pushed to GitHub

---

# 12. Day 1 Workflow

```text
Flask Project
     ↓
Test Locally
     ↓
Clean Project
     ↓
requirements.txt
     ↓
.gitignore
     ↓
README.md
     ↓
git init
     ↓
git add
     ↓
git commit
     ↓
GitHub
     ↓
Ready for Deployment
```

---

# 🧠 Key Takeaways

* Git tracks changes to code.
* GitHub hosts Git repositories online.
* `requirements.txt` defines Python dependencies.
* `.gitignore` prevents unnecessary or sensitive files from being tracked.
* README documents the project.
* Local development and production environments are different.
* Production applications should not expose secrets.
* A clean GitHub repository is the first step toward deployment.
