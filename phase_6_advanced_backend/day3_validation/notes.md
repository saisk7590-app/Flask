# Phase 6 – Day 3
# API Validation

## 🎯 Objective

Learn how to validate incoming API requests before storing data in the database.

By the end of this lesson, you will be able to:

- Validate client requests
- Prevent invalid data
- Return proper error messages
- Separate validation logic from routes
- Build cleaner and more reliable APIs

---

# What is API Validation?

API Validation is the process of checking whether the data sent by the client is correct before processing it.

Instead of accepting every request, the API first verifies that the data follows the required rules.

Example:

Client Request

```json
{
    "name": "Sai",
    "age": 21,
    "course": "Python"
}
```

The API checks:

- Is name provided?
- Is age a number?
- Is age greater than 0?
- Is course provided?

If everything is valid, the data is stored.

Otherwise, the API returns an error.

---

# Why is Validation Important?

Without validation:

- Invalid data enters the database.
- Application becomes unreliable.
- Reports become inaccurate.
- Users receive confusing responses.

With validation:

- Database remains clean.
- API becomes secure.
- Client receives meaningful errors.
- Business rules are enforced.

---

# Real-World Analogy

Imagine a college admission office.

Before accepting a student's application, the staff checks:

- Name is filled.
- Age is valid.
- Course is selected.

If anything is missing, the application is rejected.

API validation works in the same way.

---

# Validation Flow

```
Client Request
        │
        ▼
Flask Route
        │
        ▼
Read JSON
        │
        ▼
Validation
        │
   ┌────┴────┐
   │         │
 Valid    Invalid
   │         │
   ▼         ▼
Database   Return Error
```

---

# Types of Validation

## 1. Required Field Validation

Checks whether mandatory fields exist.

Example:

```json
{
    "age": 20
}
```

Response:

```json
{
    "errors": [
        "Name is required."
    ]
}
```

---

## 2. Data Type Validation

Checks whether the value has the correct data type.

Correct:

```json
{
    "age": 20
}
```

Incorrect:

```json
{
    "age": "Twenty"
}
```

---

## 3. Range Validation

Checks whether a value falls within an acceptable range.

Example:

```json
{
    "age": -5
}
```

Response:

```
Age must be greater than 0.
```

---

## 4. Length Validation

Checks the length of text.

Example:

```
Name = "A"
```

Minimum length:

```
3 characters
```

---

## 5. Business Rule Validation

Rules specific to the application.

Student API:

- Name required
- Age must be positive
- Course required

Expense Tracker:

- Amount must be greater than 0

Registration:

- Password minimum 8 characters

---

# Project Structure

```
day3_validation/

│
├── app.py
├── database.py
├── schema.sql
├── students.db
├── requests.http
├── notes.md
├── requirements.txt
│
├── validators/
│   ├── __init__.py
│   └── student_validator.py
│
└── utils/
    └── __init__.py
```

---

# Why Create a Validators Folder?

Instead of writing validation inside every route:

```python
if not name:
    ...

if age <= 0:
    ...
```

We create:

```python
validate_student(data)
```

Benefits:

- Reusable
- Cleaner routes
- Easier maintenance
- Better organization

---

# Database Design

Table:

```
students
```

Columns:

| Column | Type |
|----------|------|
| id | INTEGER |
| name | TEXT |
| age | INTEGER |
| course | TEXT |

SQL:

```sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
);
```

---

# database.py

Responsibilities:

- Connect to SQLite
- Create tables
- Insert students

Functions:

## get_connection()

Creates a SQLite connection.

```python
connection = sqlite3.connect("students.db")
```

---

## initialize_database()

Reads:

```
schema.sql
```

Creates tables if they do not already exist.

---

## add_student()

Inserts a new student into the database.

```python
INSERT INTO students(name, age, course)
VALUES (?, ?, ?)
```

Uses parameterized queries to prevent SQL injection.

---

# student_validator.py

Main function:

```python
validate_student(data)
```

Returns:

```
[]
```

if everything is valid.

Otherwise:

```python
[
    "Name is required.",
    "Age must be greater than 0."
]
```

---

# Validation Rules

## Name

Rules:

- Required
- Minimum 3 characters

Example:

```
"A"
```

Invalid.

Example:

```
"Sai"
```

Valid.

---

## Age

Rules:

- Required
- Integer
- Greater than 0

Invalid:

```
-5

0

"Twenty"
```

Valid:

```
18

21

30
```

---

## Course

Rule:

Required.

Invalid:

```
""
```

Valid:

```
Python
```

---

# Why Use data.get()?

Instead of:

```python
data["name"]
```

Use:

```python
data.get("name")
```

Reason:

If the key is missing:

```
KeyError
```

will occur.

Using `get()` returns:

```
None
```

without crashing.

---

# Why Use strip()?

Suppose the user enters:

```
"     "
```

Without:

```python
strip()
```

Length:

```
5
```

Looks valid.

After:

```python
strip()
```

Result:

```
""
```

Correctly rejected.

---

# Why Return a List of Errors?

Instead of:

```
Name is required.
```

Return:

```python
[
    "Name is required.",
    "Course is required."
]
```

Benefits:

- Client fixes all problems at once.
- Fewer API requests.
- Better user experience.

---

# app.py Flow

```
Client

↓

POST /students

↓

request.get_json()

↓

validate_student()

↓

Errors?

↓

Yes

↓

Return 400

↓

No

↓

add_student()

↓

Return 201
```

---

# HTTP Status Codes Used

## 201 Created

Returned when a student is successfully added.

Example:

```json
{
    "success": true,
    "message": "Student added successfully."
}
```

---

## 400 Bad Request

Returned when validation fails.

Example:

```json
{
    "success": false,
    "errors": [
        "Name is required."
    ]
}
```

---

# Sample Valid Request

```json
{
    "name": "Sai",
    "age": 22,
    "course": "Python"
}
```

Response:

```json
{
    "success": true,
    "message": "Student added successfully."
}
```

---

# Sample Invalid Request

```json
{
    "name": "",
    "age": -10,
    "course": ""
}
```

Response:

```json
{
    "success": false,
    "errors": [
        "Name is required.",
        "Age must be greater than 0.",
        "Course is required."
    ]
}
```

---

# Professional Benefits

Keeping validation separate provides:

- Better readability
- Reusable code
- Easier testing
- Cleaner routes
- Easier maintenance
- Scalable applications

---

# Best Practices

- Validate every client request.
- Never trust user input.
- Keep validation separate from routes.
- Return meaningful error messages.
- Return all validation errors together.
- Use parameterized SQL queries.
- Validate before inserting into the database.
- Use proper HTTP status codes.
- Follow Separation of Concerns.

---

# Interview Questions

## What is API Validation?

API Validation is the process of checking incoming request data before processing or storing it.

---

## Why is validation important?

It prevents invalid data from entering the database and improves application reliability.

---

## Why use `data.get()` instead of `data["name"]`?

Because `get()` safely returns `None` when the key does not exist instead of raising a `KeyError`.

---

## Why separate validation into another file?

To improve code organization, reusability, and maintainability.

---

## Why return `400 Bad Request`?

Because the client sent invalid input.

---

## Why return `201 Created`?

Because a new resource was successfully created.

---

## Why use parameterized SQL queries?

To prevent SQL Injection attacks and safely insert user data.

---

## What is Separation of Concerns?

It is the practice of giving each part of the application a single responsibility.

Example:

- app.py → Routes
- database.py → Database operations
- student_validator.py → Validation

---

# Key Takeaways

- API validation checks data before processing.
- Validation keeps databases clean.
- Validators should be separated from routes.
- Required fields, data types, length, range, and business rules are common validation types.
- `data.get()` prevents application crashes.
- `strip()` removes unnecessary spaces.
- Returning all validation errors improves user experience.
- Use `400 Bad Request` for invalid requests.
- Use `201 Created` for successful resource creation.
- Professional applications separate routing, validation, and database logic.
- API validation is a fundamental practice for building secure and reliable backend applications.