# Phase 6 – Day 4
# Error Handling

## 🎯 Objective

Learn how to build reliable Flask APIs that handle errors gracefully without crashing.

By the end of this lesson you can:

- Use try / except / finally
- Create custom exceptions
- Handle database errors
- Return consistent JSON responses
- Register Flask error handlers
- Add basic logging

---

# What is Error Handling?

Error handling is the process of detecting, managing, and responding to runtime errors so that the application continues running instead of crashing.

Example:

User requests an expense that does not exist.

Instead of crashing:

```
TypeError
```

The API returns:

```json
{
    "success": false,
    "error": {
        "code": "EXPENSE_NOT_FOUND",
        "message": "Expense not found."
    }
}
```

---

# Why Error Handling?

Without error handling:

- Application crashes
- Users see Python tracebacks
- Sensitive information may be exposed
- Poor user experience

With error handling:

- Stable application
- Consistent responses
- Easier debugging
- Better security

---

# Real-World Analogy

Imagine a bank ATM.

Without error handling:

```
Transaction Failed
Machine Stops
```

With error handling:

```
Transaction Failed

Please try again later.
```

The machine continues working for other users.

Backend APIs work the same way.

---

# Exception Flow

```
Client Request

↓

Flask Route

↓

Business Logic

↓

Database

↓

Exception?

↓

Yes

↓

Custom Exception

↓

Error Handler

↓

JSON Response
```

---

# try / except / finally

## try

Contains code that may fail.

```python
try:
    value = int("abc")
```

---

## except

Runs if an exception occurs.

```python
except ValueError:
    print("Invalid number")
```

---

## finally

Always executes.

Usually used to close:

- Database connections
- Files
- Network connections

```python
finally:
    connection.close()
```

---

# Why finally?

Even if an error occurs:

```
Database Connection
```

must still close.

This prevents:

- Locked database
- Resource leaks
- Performance issues

---

# Custom Exceptions

Instead of:

```python
raise Exception("Not Found")
```

Create:

```python
class ExpenseNotFoundError(Exception):
    pass
```

Then:

```python
raise ExpenseNotFoundError(
    "Expense not found."
)
```

Benefits:

- Meaningful names
- Cleaner code
- Easier debugging

---

# Custom Exceptions Used

## ExpenseNotFoundError

Raised when an expense does not exist.

Returns:

404 Not Found

---

## ValidationError

Raised when request data is invalid.

Returns:

400 Bad Request

---

## DatabaseError

Raised when SQLite operations fail.

Returns:

500 Internal Server Error

---

# Flask Error Handlers

Example:

```python
@app.errorhandler(ValidationError)
```

Whenever:

```python
raise ValidationError(...)
```

Flask automatically calls the handler.

---

# Response Utility

Instead of writing:

```python
return {
    "success": False,
    "error": {
        "code": "...",
        "message": "..."
    }
}
```

everywhere,

we created:

```python
error_response()
```

Benefits:

- Reusable
- Consistent
- Cleaner code

---

# Logging

Instead of:

```python
print("Expense added")
```

Use:

```python
logging.info("Expense added")
```

Logging Levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

# Database Safety

Database operations are wrapped inside:

```python
try:
```

If SQLite fails:

```python
except sqlite3.Error
```

Raise:

```python
DatabaseError
```

This keeps the application from crashing.

---

# HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# Project Structure

```
day4_error_handling/

├── app.py
├── database.py
├── schema.sql
├── expenses.db
├── requests.http
├── notes.md
├── requirements.txt
│
├── errors/
│   ├── __init__.py
│   └── custom_errors.py
│
├── handlers/
│   ├── __init__.py
│   └── error_handler.py
│
└── utils/
    ├── __init__.py
    └── response.py
```

---

# Best Practices

- Never expose Python tracebacks to users.
- Catch specific exceptions whenever possible.
- Use custom exceptions for business logic.
- Close database connections using finally.
- Return consistent JSON responses.
- Use logging instead of print().
- Keep error handling separate from route logic.
- Use proper HTTP status codes.

---

# Interview Questions

### What is error handling?

Error handling is the process of detecting and responding to runtime errors without crashing the application.

---

### Why use try/except?

To catch exceptions and handle them gracefully.

---

### Why use finally?

To ensure cleanup code always executes, even if an error occurs.

---

### What is a custom exception?

A user-defined exception that represents an application-specific error.

---

### Why use Flask error handlers?

To centralize error handling and provide consistent responses.

---

### Why use logging instead of print()?

Logging supports severity levels, structured output, and is suitable for production debugging.

---

### Difference between ValidationError and DatabaseError?

ValidationError:
- Caused by invalid client input.
- Returns 400.

DatabaseError:
- Caused by database failures.
- Returns 500.

---

# Key Takeaways

- Error handling makes APIs reliable.
- try / except prevents application crashes.
- finally ensures resource cleanup.
- Custom exceptions improve readability.
- Flask error handlers centralize error management.
- Logging is essential for debugging.
- Consistent JSON responses simplify frontend integration.
- Professional applications separate routing, database logic, utilities, and error handling.