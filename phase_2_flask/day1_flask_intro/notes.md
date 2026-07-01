# Day 1 — Flask Setup & First Server

## Goal

Learn how to create and run a Flask application and build simple routes.

---

## What is Flask?

Flask is a Python framework used to build:

* Backend servers
* APIs
* Web applications

Flask helps Python receive requests and send responses.

---

## Install Flask

```bash
pip install flask
```

Verify installation:

```bash
pip show flask
```

---

## Create Flask App

```python
from flask import Flask

app = Flask(__name__)
```

`app` is the Flask application object.

Think:

```text
app = Backend Server
```

---

## Create Route

```python
@app.route("/")
def home():
    return "Hello Flask!"
```

Route means:

```text
When user visits "/"
Run home()
```

---

## Run Server

```python
app.run()
```

Starts the Flask development server.

---

## Complete Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my API"

@app.route("/about")
def about():
    return "I am learning Flask"

@app.route("/contact")
def contact():
    return "Contact: sai@example.com"

app.run()
```

---

## URLs

Home:

```text
http://127.0.0.1:5000/
```

About:

```text
http://127.0.0.1:5000/about
```

Contact:

```text
http://127.0.0.1:5000/contact
```

---

## Backend Flow

```text
Browser
   ↓
Request
   ↓
Route
   ↓
Function
   ↓
Response
   ↓
Browser
```

---

## Key Concepts

### Flask

Framework for building backend applications.

### Route

URL path handled by Flask.

Example:

```python
@app.route("/")
```

### Function

Code executed when a route is visited.

Example:

```python
def home():
```

### Response

Data returned to the client.

Example:

```python
return "Hello"
```

---

## Important Syntax

Create app:

```python
app = Flask(__name__)
```

Create route:

```python
@app.route("/")
```

Return response:

```python
return "Hello"
```

Run server:

```python
app.run()
```

---

## Common Mistakes

### Forgetting return

Wrong:

```python
def home():
    print("Hello")
```

Correct:

```python
def home():
    return "Hello"
```

### Indentation Error

Wrong:

```python
def home():
return "Hello"
```

Correct:

```python
def home():
    return "Hello"
```

### Forgetting app.run()

Without it, the server will not start.

---

## Mini Project

Personal Introduction API

Endpoints:

```text
/
/about
/contact
```

Returns simple text responses.

---

## Day 1 Summary

Flask Server
→ Route
→ Function
→ Response

Important Commands:

```bash
pip install flask
python app.py
```

Important Code:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

app.run()
```

Status: ✅ Day 1 Complete
