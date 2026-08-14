# Phase 7 — Day 5 — CI/CD Notes

## 1. What Is CI/CD?

CI/CD is a development practice used to automate testing and deployment.

```text
CI
↓
Continuous Integration
↓
Automated checks and tests

CD
↓
Continuous Deployment
↓
Automated deployment
```

The basic workflow is:

```text
git push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Tests
    ↓
PASS
    ↓
Deployment
```

---

## 2. Continuous Integration

CI answers:

> Does the new code pass our automated checks?

Example:

```text
git push
    ↓
GitHub Actions
    ↓
pytest
    ↓
PASS / FAIL
```

If the tests fail, the workflow stops.

---

## 3. Continuous Deployment

CD answers:

> Can the validated code be deployed?

The basic flow is:

```text
Tests
 ↓
PASS
 ↓
Deploy
 ↓
Production
```

---

## 4. GitHub Actions

GitHub Actions is used to automate tasks inside a GitHub repository.

Our workflow performs:

```text
Checkout code
      ↓
Set up Python
      ↓
Install dependencies
      ↓
Run tests
      ↓
Deploy to Render
```

The workflow runs when code is pushed to the `main` branch.

---

## 5. GitHub Actions Runner

The workflow runs on a temporary GitHub-hosted machine.

Our workflow uses:

```text
ubuntu-latest
```

This is different from the local Windows development environment.

---

## 6. Python Version

The GitHub Actions workflow explicitly uses:

```text
Python 3.12
```

This makes the CI environment predictable.

The local development environment may use a different Python version.

---

## 7. Dependencies

Dependencies are installed from:

```text
requirements.txt
```

Example command:

```text
pip install -r requirements.txt
```

This allows the GitHub Actions runner to install the packages required by the project.

---

## 8. pytest

`pytest` is used for automated testing.

Local command:

```powershell
python -m pytest
```

The project successfully produced:

```text
2 passed
```

The tests verify that the Flask application endpoints behave as expected.

---

## 9. Why Use `python -m pytest` Locally?

Running:

```powershell
pytest
```

caused:

```text
ModuleNotFoundError: No module named 'app'
```

even though `app.py` existed in the project directory.

Running:

```powershell
python -m pytest
```

successfully collected and executed the tests:

```text
collected 2 items

tests\test_app.py ..

2 passed
```

This was an important practical lesson about Python module resolution.

---

## 10. CI Test Failure

The deployment step should come after the test step.

Correct:

```text
Install dependencies
      ↓
Run tests
      ↓
PASS
      ↓
Deploy
```

If:

```text
pytest
 ↓
FAIL
```

the workflow stops and the deployment step does not continue.

This makes testing a quality gate.

---

## 11. Render Deployment

Render is used to host the Flask application.

The deployment flow is:

```text
GitHub Actions
      ↓
Render deployment trigger
      ↓
Render
      ↓
Build
      ↓
Start application
      ↓
Live API
```

The deployment trigger is stored as a GitHub Secret.

---

## 12. GitHub Secrets

Sensitive values should not be stored directly inside the repository.

Our deployment hook is stored as:

```text
RENDER_DEPLOY_HOOK
```

The workflow accesses it using:

```text
${{ secrets.RENDER_DEPLOY_HOOK }}
```

The real secret value should never be written into the workflow file.

---

## 13. curl

The deployment workflow uses `curl` to send an HTTP request to the Render deployment trigger.

Conceptually:

```text
GitHub Actions
      ↓
HTTP request
      ↓
Render deployment trigger
      ↓
Deployment
```

---

## 14. Production Server

Flask's development server is useful locally:

```text
python app.py
```

Production uses a WSGI server such as:

```text
Gunicorn
```

Conceptually:

```text
Flask
 ↓
WSGI
 ↓
Gunicorn
 ↓
Production
```

---

## 15. Environment Variables

Production configuration should be stored outside the source code.

Examples:

```text
SECRET_KEY
DATABASE_URL
API_KEY
```

The application can read configuration through environment variables.

For example:

```python
import os

DATABASE_URL = os.getenv("DATABASE_URL")
```

---

## 16. `.env`

Local development can use:

```text
.env
```

for environment-specific configuration.

The `.env` file should not be committed to Git.

Instead, an example file can document the required variables:

```text
.env.example
```

---

## 17. Production Debug Mode

Development may use:

```text
DEBUG=True
```

Production should not expose the Flask debugger.

Production configuration should therefore use:

```text
DEBUG=False
```

---

## 18. CI/CD Security

Never commit:

```text
Passwords
API keys
Database credentials
Deployment secrets
Production secrets
```

Use:

```text
GitHub Secrets
Environment Variables
Render Environment Variables
```

instead.

---

## 19. Complete Workflow

```text
Developer
    ↓
Code change
    ↓
git add .
    ↓
git commit
    ↓
git push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Checkout
    ↓
Python setup
    ↓
Install dependencies
    ↓
pytest
    ↓
PASS
    ↓
Render deployment
    ↓
Gunicorn
    ↓
Flask
    ↓
Live API
```

---

## 20. Failed Workflow

If tests fail:

```text
Developer
    ↓
git push
    ↓
GitHub Actions
    ↓
pytest
    ↓
FAIL
    ↓
STOP
```

The deployment step does not run after a failed test step.

---

## 21. Important Concepts Learned

### CI

Automated validation of code changes.

### CD

Automated deployment of validated code.

### GitHub Actions

Automation platform integrated with GitHub.

### pytest

Python testing framework used for automated tests.

### GitHub Secrets

Secure storage for sensitive CI/CD values.

### Render

Cloud hosting/deployment platform used for the Flask API.

### Gunicorn

Production WSGI server for running Flask applications.

---

## 22. Main Lesson

The most important idea from Day 5 is:

```text
Do not think:

Code → Deploy
```

Think:

```text
Code
 ↓
Test
 ↓
Validate
 ↓
Deploy
 ↓
Monitor
```

This is the basic production mindset introduced by CI/CD.

---

## 23. Phase 7 Final Connection

```text
Day 1
Git + GitHub
     ↓
Day 2
Render + Gunicorn
     ↓
Day 3
PostgreSQL
     ↓
Day 4
Environment + Production Configuration
     ↓
Day 5
CI/CD
```

Phase 7 completes the transition from:

```text
Local Flask Application
```

to:

```text
Production-oriented Flask Backend
```
