# Phase 6 – Day 1
# Professional Project Structure + Flask Blueprints

## Objective

Learn how professional Flask applications are organized by separating responsibilities into different modules and using Flask Blueprints.

---

# Why Project Structure Matters

Small Flask applications can be written in a single `app.py` file.

Example:

app.py

As the application grows, keeping everything in one file becomes difficult.

Problems:

- Difficult to read
- Difficult to maintain
- Difficult to debug
- Hard for multiple developers to work together
- Repeated code

Professional applications organize code into multiple folders.

---

# Separation of Concerns (SoC)

Definition:

Each part of the application should have one clear responsibility.

Instead of one file doing everything, responsibilities are divided into layers.

Example:

Request
    ↓
Route
    ↓
Service
    ↓
Database
    ↓
Service
    ↓
Response

---

# Professional Folder Structure

```
day1_project_structure/

│
├── app/
│
├── routes/
│
├── services/
│
├── models/
│
├── database/
│
├── utils/
│
├── helpers/
│
├── config/
│
└── __init__.py

main.py

requirements.txt

notes.md
```

---

# Folder Responsibilities

## routes/

Responsible for handling HTTP requests.

Example:

- GET /students
- POST /students
- DELETE /students

Routes should:

- Receive requests
- Call services
- Return responses

Routes should NOT contain business logic.

---

## services/

Contains business logic.

Examples:

- Get students
- Add student
- Calculate average
- Verify password
- Generate JWT

Routes call services instead of performing the work themselves.

---

## models/

Represents application data.

Example:

Student

- id
- name
- age
- course

Expense

- title
- amount

Later, SQLAlchemy models will live here.

---

## database/

Contains database-related code.

Example:

- Database connection
- Database helper functions

Advantages:

- Centralized connection
- Easier maintenance
- Easy database replacement

---

## config/

Stores application configuration.

Examples:

- SECRET_KEY
- JWT Secret
- Database Path
- DEBUG Mode

---

## utils/

Contains reusable helper functions.

Examples:

- Date formatting
- UUID generation
- Common calculations

---

## helpers/

Contains reusable logic shared across multiple modules.

Examples:

- JWT helper
- Password helper
- Response formatter

---

# Flask Blueprints

Blueprints organize related routes into separate files.

Without Blueprints:

app.py

- Login
- Register
- Students
- Expenses
- Reports

Everything is mixed together.

With Blueprints:

routes/

auth_routes.py

student_routes.py

expense_routes.py

Each Blueprint manages one feature.

---

# Blueprint Benefits

- Better organization
- Easier maintenance
- Modular code
- Easy testing
- Better scalability
- Multiple developers can work simultaneously

---

# Service Layer

The Service Layer contains business logic.

Instead of:

Route

↓

Connect Database

↓

Process Data

↓

Return Response

We use:

Route

↓

Service

↓

Return Response

Example:

Route:

students = get_all_students()

Service:

Connect Database

↓

Fetch Data

↓

Return Students

---

# Model

A Model represents application data.

Example:

Student

id

name

course

Models help organize data.

Later they will represent database tables.

---

# Request Flow

Browser/Postman

↓

main.py

↓

Blueprint (Route)

↓

Service

↓

Model

↓

Database

↓

Service

↓

Route

↓

JSON Response

---

# Project Flow

Client

↓

Route

↓

Service

↓

Database

↓

Service

↓

Route

↓

Response

---

# Advantages of This Structure

- Clean code
- Easier debugging
- Easy maintenance
- Reusable logic
- Better scalability
- Professional architecture

---

# Interview Questions

## What is Separation of Concerns?

Separating an application into different layers where each layer has one responsibility.

---

## What is a Flask Blueprint?

A Blueprint is a modular collection of related routes that can be registered with a Flask application.

---

## Why use a Service Layer?

To separate business logic from request handling.

---

## Why create a models folder?

To define application data structures.

---

## Why shouldn't business logic be inside routes?

Because routes should only handle HTTP requests and responses. Business logic belongs in the service layer.

---

# Key Takeaways

✓ Professional project organization

✓ Separation of Concerns

✓ Flask Blueprints

✓ Service Layer

✓ Models

✓ Modular architecture

✓ Scalable backend design