# 📝 Phase 4 — Day 5 Notes
# Flask + SQLite Integration

---

# 🎯 Day Goal

Replace Python list storage with a real SQLite database in a Flask application.

By the end of today, you can build a complete REST API backed by a database.

---

# Topics Covered

- sqlite3 module
- Flask + SQLite integration
- Database connection
- JSON requests
- JSON responses
- GET API
- POST API
- PUT API
- DELETE API
- HTTP status codes
- row_factory
- lastrowid

---

# Why Connect Flask to a Database?

Earlier, data was stored in Python lists.

Example:

```python
students = []
```

Problem:

- Data disappears when the application stops.
- Cannot share data between sessions.
- Not suitable for real applications.

Using SQLite:

- Data is stored permanently.
- Data persists after restarting the application.
- Multiple requests can access the same database.

---

# get_connection()

```python
def get_connection():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    return connection
```

Purpose:

- Open a database connection.
- Return rows that behave like dictionaries.
- Reuse the same connection code across all routes.

---

# row_factory

Without `row_factory`:

```python
student[0]
student[1]
```

With `sqlite3.Row`:

```python
student["name"]
student["course"]
```

This makes converting database rows to JSON much easier.

---

# CRUD Endpoints

## GET /

Checks whether the API is running.

Response:

```
Student API is running!
```

---

## GET /students

SQL:

```sql
SELECT *
FROM students
ORDER BY id;
```

Returns every student in JSON format.

Status Code:

200 OK

---

## GET /students/<id>

SQL:

```sql
SELECT *
FROM students
WHERE id = ?;
```

Returns one student.

If not found:

```json
{
    "message": "Student not found"
}
```

Status Code:

404 Not Found

---

## POST /students

Reads JSON:

```json
{
    "name":"Ramesh",
    "age":24,
    "course":"Django"
}
```

SQL:

```sql
INSERT INTO students
(name, age, course)
VALUES (?, ?, ?);
```

Returns:

201 Created

---

## cursor.lastrowid

After INSERT:

```python
new_id = cursor.lastrowid
```

Returns the automatically generated ID of the newly inserted record.

---

## PUT /students/<id>

SQL:

```sql
UPDATE students
SET
    name = ?,
    age = ?,
    course = ?
WHERE id = ?;
```

Updates an existing student.

Returns:

200 OK

If no student exists:

404 Not Found

---

## DELETE /students/<id>

SQL:

```sql
DELETE FROM students
WHERE id = ?;
```

Deletes a student.

Returns:

200 OK

If the student does not exist:

404 Not Found

---

# HTTP Status Codes Used

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Resource Created |
| 404 | Resource Not Found |

---

# SQL Statements Learned

```sql
CREATE TABLE
```

Creates a table.

---

```sql
INSERT INTO
```

Adds new records.

---

```sql
SELECT
```

Retrieves records.

---

```sql
UPDATE
```

Modifies existing records.

---

```sql
DELETE
```

Removes records.

---

# SQLite Functions Used

```python
sqlite3.connect()
```

Opens a database connection.

---

```python
cursor.execute()
```

Executes one SQL query.

---

```python
cursor.executemany()
```

Executes the same query multiple times.

---

```python
cursor.fetchone()
```

Returns a single record.

---

```python
cursor.fetchall()
```

Returns all matching records.

---

```python
connection.commit()
```

Saves changes permanently.

---

```python
connection.close()
```

Closes the database connection.

---

```python
cursor.rowcount
```

Returns the number of affected rows after UPDATE or DELETE.

---

```python
cursor.lastrowid
```

Returns the ID of the last inserted row.

---

# Projects Built

- Student Database Setup
- Student Registration System
- Student Search System
- Student Management System
- Student REST API with SQLite

---

# Best Practices Learned

- Use parameterized queries (`?`) to prevent SQL injection.
- Always call `commit()` after INSERT, UPDATE, or DELETE.
- Always close database connections.
- Return appropriate HTTP status codes.
- Use helper functions such as `get_connection()` to avoid code duplication.

---

# Phase 4 Skills Mastered

- Database Fundamentals
- Tables, Rows, Columns
- Primary Keys
- SQLite
- SQL CRUD Operations
- Flask + SQLite Integration
- Persistent Data Storage
- REST APIs with a Database

---

# Day 5 Completion Checklist

- [x] Connected Flask to SQLite.
- [x] Created reusable database connection helper.
- [x] Implemented GET /students.
- [x] Implemented GET /students/<id>.
- [x] Implemented POST /students.
- [x] Implemented PUT /students/<id>.
- [x] Implemented DELETE /students/<id>.
- [x] Tested all endpoints.
- [x] Returned proper HTTP status codes.
- [x] Built a complete CRUD REST API using SQLite.

---

# 🚀 Phase 4 Completed

You can now build a complete backend CRUD API using Flask and SQLite.

The next phase is **Phase 5 — Authentication System**, where you'll learn user registration, login, password hashing, JWT authentication, and protected routes.