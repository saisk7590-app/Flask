# Day 1 — Deployment Preparation Checklist

## 🎯 Goal

Prepare the Flask backend project for GitHub and deployment.

---

# 1. Project Preparation

* [ ] Select the Flask project to deploy
* [ ] Confirm the project runs locally
* [ ] Check the project folder structure
* [ ] Remove unnecessary files
* [ ] Confirm the Flask application starts successfully

---

# 2. Python Dependencies

* [ ] Create `requirements.txt`
* [ ] Add Flask
* [ ] Add Gunicorn
* [ ] Verify required packages
* [ ] Test installing dependencies using:

```bash
pip install -r requirements.txt
```

---

# 3. Git Configuration

* [ ] Create `.gitignore`
* [ ] Ignore `__pycache__/`
* [ ] Ignore virtual environments
* [ ] Ignore `.env`
* [ ] Ignore database files if they are local-only
* [ ] Check that sensitive files are not tracked

---

# 4. README Documentation

* [ ] Add project name
* [ ] Add project description
* [ ] Add technologies used
* [ ] Add installation instructions
* [ ] Add how to run the application
* [ ] Add API endpoints
* [ ] Add basic project information

---

# 5. Local Testing

* [ ] Activate virtual environment
* [ ] Install requirements
* [ ] Start Flask application
* [ ] Test API endpoints
* [ ] Confirm there are no errors
* [ ] Confirm the application works before pushing

Example:

```bash
python app.py
```

---

# 6. Git Repository

Initialize Git:

```bash
git init
```

Check repository status:

```bash
git status
```

Add project files:

```bash
git add .
```

Create the first commit:

```bash
git commit -m "Prepare Flask API for deployment"
```

---

# 7. GitHub Repository

* [ ] Create a GitHub repository
* [ ] Choose a suitable repository name
* [ ] Add the GitHub remote
* [ ] Verify the remote URL

Example:

```bash
git remote add origin <repository-url>
```

---

# 8. Push Project to GitHub

Push the project:

```bash
git push -u origin main
```

* [ ] Confirm push succeeds
* [ ] Open the GitHub repository
* [ ] Confirm project files are visible
* [ ] Confirm `.env` is not visible
* [ ] Confirm virtual environment is not visible
* [ ] Confirm README is displayed correctly

---

# 9. Final Verification

The repository should contain:

```text
project/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

And should NOT contain:

```text
.env
venv/
.venv/
__pycache__/
*.db
```

---

# ✅ Day 1 Completion Criteria

Day 1 is complete when:

* [ ] Flask API runs locally
* [ ] Dependencies are documented
* [ ] `.gitignore` is configured
* [ ] README is available
* [ ] Git repository is initialized
* [ ] Initial commit is created
* [ ] GitHub repository is created
* [ ] Code is pushed to GitHub
* [ ] No secrets are exposed
* [ ] Repository is ready for deployment

---

# 🚀 Next Step

After completing this checklist:

```text
Day 1
GitHub & Deployment Preparation
        ↓
Day 2
Render Deployment
        ↓
Gunicorn + WSGI
        ↓
Live Flask API
```
