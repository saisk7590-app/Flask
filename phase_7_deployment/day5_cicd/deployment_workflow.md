# Phase 7 — Day 5 — CI/CD Deployment Workflow

## 1. Purpose

This document describes the CI/CD workflow used by the Day 5 Flask practice project.

The objective is to automate:

```text
Code Push
    ↓
Automated Tests
    ↓
Successful Validation
    ↓
Render Deployment
```

---

## 2. Architecture

```text
Developer
    │
    │ git push
    ↓
GitHub
    │
    ↓
GitHub Actions
    │
    ├── Checkout Code
    │
    ├── Setup Python
    │
    ├── Install Dependencies
    │
    ├── Run pytest
    │
    └── Deploy to Render
             │
             ↓
          Render
             │
             ↓
          Gunicorn
             │
             ↓
        Flask API
```

---

## 3. Workflow Trigger

The workflow is triggered when code is pushed to the `main` branch.

Conceptually:

```yaml
on:
  push:
    branches:
      - main
```

This means a push to `main` starts the GitHub Actions workflow.

---

## 4. Checkout

GitHub Actions first checks out the repository:

```yaml
- name: Checkout code
  uses: actions/checkout@v4
```

This makes the repository files available to the GitHub Actions runner.

---

## 5. Python Setup

The workflow prepares Python:

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: "3.12"
```

The CI environment therefore uses Python 3.12.

---

## 6. Dependency Installation

The workflow installs the project's dependencies:

```yaml
- name: Install dependencies
  run: pip install -r requirements.txt
```

The dependencies are defined in:

```text
requirements.txt
```

---

## 7. Automated Tests

The next step runs the automated tests:

```yaml
- name: Run tests
  run: pytest
```

The tests are located in:

```text
tests/
```

The local test command that was successfully used during development was:

```powershell
python -m pytest
```

The test suite successfully returned:

```text
2 passed
```

---

## 8. Test as a Deployment Gate

The workflow follows:

```text
Install Dependencies
        ↓
Run Tests
        ↓
     PASS?
      /  \
    NO    YES
    ↓      ↓
  STOP   DEPLOY
```

If the test step fails, GitHub Actions stops the job.

Therefore, the deployment step is reached only after the test step succeeds.

---

## 9. Render Deployment

After successful tests, the workflow triggers the Render deployment.

Conceptually:

```yaml
- name: Deploy to Render
  run: |
    curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK }}"
```

The deployment hook is not stored directly in the repository.

---

## 10. GitHub Secret

The workflow expects a repository secret named:

```text
RENDER_DEPLOY_HOOK
```

The secret contains the Render deployment trigger.

The workflow accesses it through:

```text
${{ secrets.RENDER_DEPLOY_HOOK }}
```

This keeps the actual deployment hook out of the source code.

---

## 11. Why the Secret Is Required

A deployment hook is a sensitive value because it can be used to trigger a deployment.

Therefore, this should **not** be committed:

```text
https://api.render.com/deploy/...
```

Instead:

```text
GitHub Repository
       ↓
GitHub Secret
       ↓
GitHub Actions
       ↓
Render deployment trigger
```

---

## 12. Complete Workflow Example

A simplified version of the workflow is:

```yaml
name: Flask API CI/CD

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest

      - name: Deploy to Render
        run: |
          curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK }}"
```

---

## 13. Successful Workflow

When the developer pushes valid code:

```text
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
✅ PASS
    ↓
Render deployment trigger
    ↓
Render
    ↓
Application deployed
```

---

## 14. Failed Workflow

When automated tests fail:

```text
git push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
pytest
    ↓
❌ FAIL
    ↓
Workflow stops
```

The deployment step is not executed after the failed test step.

---

## 15. Render Production Flow

After Render receives the deployment trigger:

```text
Render
   ↓
Build application
   ↓
Install dependencies
   ↓
Start production server
   ↓
Gunicorn
   ↓
Flask application
   ↓
Live API
```

The exact build and start commands are configured in the Render service.

---

## 16. Production Testing

After deployment, the live API should be tested.

For example:

```text
GET /health
```

Expected response:

```json
{
    "status": "healthy"
}
```

Production verification can be performed using:

```text
Browser
Postman
curl
```

---

## 17. Deployment Logs

After deployment, Render logs can be checked for information such as:

```text
Build started
Build completed
Starting application
Starting Gunicorn
Worker started
Request received
```

Errors in production should be investigated using the deployment and application logs.

---

## 18. Deployment Strategy

This project uses a CI-controlled deployment approach:

```text
git push
    ↓
GitHub Actions
    ↓
Tests
    ↓
PASS
    ↓
Render deployment trigger
```

This demonstrates the principle of:

> Validate the code before triggering deployment.

---

## 19. Important Security Rules

Never commit:

```text
.env
Passwords
Database credentials
API keys
Deployment hook values
Production secrets
```

Use:

```text
.env.example
GitHub Secrets
Render Environment Variables
```

for configuration and sensitive values.

---

## 20. Final Workflow

```text
                    DEVELOPER
                        │
                     git push
                        │
                        ↓
                     GITHUB
                        │
                        ↓
                GITHUB ACTIONS
                        │
                        ↓
                Install Dependencies
                        │
                        ↓
                     pytest
                        │
                   ┌────┴────┐
                   │         │
                 FAIL       PASS
                   │         │
                   ↓         ↓
                  STOP     DEPLOY
                             │
                             ↓
                           RENDER
                             │
                          Gunicorn
                             │
                             ↓
                           Flask
                             │
                             ↓
                        LIVE API
```

---

## 21. Day 5 Result

The Day 5 project demonstrates the core CI/CD lifecycle:

```text
Develop
   ↓
Commit
   ↓
Push
   ↓
Test
   ↓
Validate
   ↓
Deploy
   ↓
Verify
```

This completes the CI/CD portion of Phase 7 — Deployment & Production.
