# Phase 6 – Day 2
# Environment Variables & Configuration

## 🎯 Objective

Learn how professional Flask applications manage configuration securely using environment variables instead of hardcoding sensitive information.

---

# What are Environment Variables?

Environment variables are configuration values stored outside the application code.

Instead of writing:

```python
SECRET_KEY = "mysecret123"
```

We write:

```python
SECRET_KEY = os.getenv("SECRET_KEY")
```

The value is read from the operating system or a `.env` file.

---

# Why Use Environment Variables?

Hardcoding secrets inside source code is a security risk.

Example:

```python
SECRET_KEY = "mysecret123"
DATABASE_PASSWORD = "admin123"
API_KEY = "abcxyz"
```

If this code is pushed to GitHub, anyone can view these secrets.

Environment variables keep sensitive information outside the codebase.

---

# Benefits

- Better security
- Cleaner configuration
- Different settings for development and production
- Easy deployment
- Secrets remain private

---

# Real-World Analogy

Imagine the key to your house.

❌ Writing it on the front door is like hardcoding secrets.

✅ Keeping it safely in your pocket is like using environment variables.

---

# .env File

A `.env` file stores environment variables for local development.

Example:

```env
SECRET_KEY=my_super_secret_key
DATABASE_PATH=students.db
DEBUG=True
APP_NAME=Student API
```

Each line follows the format:

```
KEY=VALUE
```

---

# .env.example

This file contains sample values instead of real secrets.

Example:

```env
SECRET_KEY=your_secret_key
DATABASE_PATH=your_database.db
DEBUG=True
APP_NAME=Your Application
```

Purpose:

- Shows which variables are required
- Safe to upload to GitHub
- Other developers can copy it to create their own `.env`

---

# .gitignore

The `.gitignore` file tells Git which files should not be tracked.

Example:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

Why?

- Prevents uploading secrets
- Keeps repositories clean
- Avoids unnecessary files

---

# python-dotenv

Python cannot automatically read a `.env` file.

The `python-dotenv` package loads the values from `.env` into the environment.

Install:

```powershell
pip install python-dotenv
```

Update dependencies:

```powershell
pip freeze > requirements.txt
```

---

# Loading Environment Variables

Example:

```python
import os

from dotenv import load_dotenv

load_dotenv()
```

`load_dotenv()` reads the `.env` file and makes the variables available to `os.getenv()`.

---

# Reading Variables

Example:

```python
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_PATH = os.getenv("DATABASE_PATH")
APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG")
```

---

# Default Values

Sometimes a variable may be missing.

Instead of:

```python
APP_NAME = os.getenv("APP_NAME")
```

Use:

```python
APP_NAME = os.getenv("APP_NAME", "Student API")
```

If the variable does not exist, `"Student API"` will be used.

---

# Boolean Conversion

`os.getenv()` always returns strings.

Example:

```env
DEBUG=True
```

Python reads:

```python
"True"
```

Not:

```python
True
```

Professional conversion:

```python
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
```

This converts the string into a real Boolean.

---

# Required Variables

Some variables are mandatory.

Example:

```python
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is missing.")
```

Benefits:

- Detects configuration errors early
- Prevents unexpected runtime failures

---

# Professional settings.py

```python
import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is missing.")

DATABASE_PATH = os.getenv("DATABASE_PATH", "students.db")

APP_NAME = os.getenv("APP_NAME", "Student API")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"
```

---

# app.py Example

```python
from flask import Flask

from config.settings import (
    APP_NAME,
    DATABASE_PATH,
    DEBUG,
    SECRET_KEY,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def home():
    return {
        "application": APP_NAME,
        "database": DATABASE_PATH,
        "debug": DEBUG,
    }


if __name__ == "__main__":
    app.run(debug=True)
```

**Note:** Never return `SECRET_KEY` in a real application. It was only done during learning to verify that it loaded correctly.

---

# Configuration Flow

```
.env File
        │
        ▼
load_dotenv()
        │
        ▼
Environment Variables
        │
        ▼
os.getenv()
        │
        ▼
Validation
        │
        ▼
Default Values
        │
        ▼
Type Conversion
        │
        ▼
Flask Application
```

---

# Development vs Production

## Development

```env
DEBUG=True
DATABASE_PATH=students.db
```

## Production

```env
DEBUG=False
DATABASE_URL=postgres://...
SECRET_KEY=VeryLongRandomSecret
```

Same application.

Different configuration.

---

# Common Environment Variables

| Variable | Purpose |
|-----------|---------|
| SECRET_KEY | Flask security |
| DATABASE_PATH | SQLite database path |
| DATABASE_URL | PostgreSQL/MySQL connection |
| DEBUG | Enable or disable debug mode |
| APP_NAME | Application name |
| API_KEY | External API authentication |
| JWT_SECRET | JWT token signing key |
| HOST | Server host |
| PORT | Server port |

---

# Best Practices

✅ Never hardcode secrets.

✅ Store secrets in `.env`.

✅ Add `.env` to `.gitignore`.

✅ Commit `.env.example`.

✅ Keep all configuration inside `config/settings.py`.

✅ Use meaningful environment variable names.

✅ Validate required variables.

✅ Provide default values for optional variables.

✅ Convert environment variables to the correct data type.

---

# Interview Questions

## What is an environment variable?

A configuration value stored outside the application code.

---

## Why should secrets not be hardcoded?

Because they can be exposed if the source code is shared or pushed to a public repository.

---

## What is the purpose of `.env`?

To store environment variables for local development.

---

## Why use `.env.example`?

To show other developers which environment variables are required without exposing actual secrets.

---

## Why use `python-dotenv`?

Because Python does not automatically read `.env` files.

---

## Why use default values with `os.getenv()`?

To ensure optional configuration values always have a fallback.

---

## Why convert `DEBUG` to a Boolean?

Because `os.getenv()` returns strings, not Boolean values.

---

## Why validate `SECRET_KEY`?

To fail fast if a required configuration value is missing.

---

# Key Takeaways

- Environment variables keep secrets out of source code.
- `.env` is used for local development.
- `.env.example` documents required configuration.
- `.gitignore` prevents secrets from being committed.
- `python-dotenv` loads environment variables.
- `os.getenv()` reads environment variables.
- Use default values where appropriate.
- Convert values to the correct data type.
- Validate required variables during startup.
- Centralize configuration in `config/settings.py`.
- Professional applications separate code from configuration.