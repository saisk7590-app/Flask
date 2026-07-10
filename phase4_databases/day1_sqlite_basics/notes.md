# 📝 Phase 4 — Day 1 Notes

# Database Fundamentals + SQLite

---

# 🎯 Day Goal

Learn:

* What is a Database?
* Why Databases are used
* File Storage vs Database Storage
* What is SQLite?
* Database Terminology
* Create the first SQLite database
* Create the first table
* View the table structure

---

# 1. What is Data?

Data is simply information.

Examples:

* Student Details
* Employee Records
* Bank Accounts
* Products
* Orders
* Messages

Applications exist to store, retrieve, update, and manage data.

---

# 2. What is a Database?

A **Database** is an organized collection of data stored electronically.

It allows us to:

* Store data permanently
* Search data quickly
* Update records
* Delete records
* Organize information efficiently

Example:

A College Database stores:

* Students
* Teachers
* Courses
* Fees
* Attendance

---

# 3. Why Databases are Used

Without databases:

* Data is difficult to organize.
* Searching becomes slow.
* Updating records is difficult.
* Large amounts of data become hard to manage.

Databases solve these problems by providing fast, organized, and reliable storage.

---

# 4. File Storage vs Database Storage

## File Storage

Example:

students.json

Advantages:

* Easy to create
* Good for very small projects

Disadvantages:

* Slow searching
* Difficult updates
* No relationships
* Hard to manage large data

---

## Database Storage

Example:

students.db

Advantages:

* Fast searching
* Easy updates
* Easy deletion
* Structured storage
* Better performance
* Supports relationships
* Scales much better

---

# Comparison

| Feature           | File Storage | Database |
| ----------------- | ------------ | -------- |
| Permanent Storage | ✅            | ✅        |
| Fast Search       | ❌            | ✅        |
| Easy Updates      | ❌            | ✅        |
| Large Data        | ❌            | ✅        |
| Relationships     | ❌            | ✅        |

---

# 5. What is SQLite?

SQLite is a lightweight relational database.

Characteristics:

* Built into Python (`sqlite3`)
* No separate installation required
* No database server required
* Stores everything inside a single `.db` file

Example:

students.db

SQLite is perfect for:

* Learning SQL
* Personal Projects
* Small Applications
* Local Development

---

# 6. Database Terminology

## Database

A container that stores one or more tables.

Example:

students.db

---

## Table

A table stores one type of information.

Examples:

* students
* teachers
* courses

---

## Row

A single record inside a table.

Example:

| id | name | age | course |
| -- | ---- | --- | ------ |
| 1  | Sai  | 21  | Python |

This complete record is one row.

---

## Column

A column represents one field of information.

Example:

* id
* name
* age
* course

Each column stores one specific type of data.

---

## Primary Key

A Primary Key uniquely identifies every row.

Properties:

* Unique
* Cannot be NULL
* One Primary Key per table

Example:

| id | name |
| -- | ---- |
| 1  | Sai  |
| 2  | Sai  |

Even if names are the same, `id` uniquely identifies each record.

---

# 7. SQL

SQL stands for:

**Structured Query Language**

SQL is the language used to communicate with relational databases.

Examples of SQL commands:

* CREATE
* INSERT
* SELECT
* UPDATE
* DELETE

---

# 8. CREATE TABLE

SQL used:

```sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
);
```

Explanation:

* `CREATE TABLE` → Creates a new table.
* `IF NOT EXISTS` → Prevents an error if the table already exists.
* `students` → Table name.
* `id INTEGER PRIMARY KEY` → Unique numeric identifier.
* `name TEXT` → Stores text.
* `age INTEGER` → Stores whole numbers.
* `course TEXT` → Stores text.

---

# 9. Python sqlite3 Module

Import SQLite:

```python
import sqlite3
```

Connect to database:

```python
connection = sqlite3.connect("students.db")
```

If the database does not exist:

* SQLite creates it automatically.

If it already exists:

* SQLite opens it.

---

# 10. Cursor

Create a cursor:

```python
cursor = connection.cursor()
```

A **Cursor** is the communication bridge between Python and SQLite.

Responsibilities:

* Executes SQL queries.
* Retrieves results from the database.

---

# 11. Reading SQL from schema.sql

Open SQL file:

```python
with open("schema.sql", "r") as file:
    sql_script = file.read()
```

Execute SQL:

```python
cursor.executescript(sql_script)
```

This runs all SQL statements stored in the file.

---

# 12. Commit Changes

```python
connection.commit()
```

Purpose:

Saves changes permanently to the database.

Best Practice:

Always commit after making changes to the database.

---

# 13. Close Connection

```python
connection.close()
```

Always close the database connection after finishing your work.

Benefits:

* Releases resources.
* Prevents connection leaks.
* Good programming practice.

---

# 14. Viewing Table Structure

SQL:

```sql
PRAGMA table_info(students);
```

Purpose:

Displays the structure of the `students` table.

Shows:

* Column names
* Data types
* Primary Key
* Default values
* NOT NULL information

---

# 15. fetchall()

Python:

```python
columns = cursor.fetchall()
```

Purpose:

Retrieves all rows returned by the SQL query.

Returns a Python list of tuples.

---

# 16. Why Did We Get This Error?

Error:

```text
sqlite3.OperationalError:
table students already exists
```

Reason:

The `students` table had already been created.

SQLite cannot create the same table twice.

Solution:

Use:

```sql
CREATE TABLE IF NOT EXISTS students
```

This tells SQLite:

> Create the table only if it does not already exist.

---

# 17. Project Structure

```
phase4_databases/
│
└── day1_sqlite_basics/
    ├── app.py
    ├── database.py
    ├── schema.sql
    ├── students.db
    └── notes.md
```

---

# 18. Workflow

```
Python Program
        │
        ▼
sqlite3 Module
        │
        ▼
Connection
        │
        ▼
Cursor
        │
        ▼
Execute SQL
        │
        ▼
SQLite Database
        │
        ▼
Save Changes (commit)
        │
        ▼
Close Connection
```

---

# 19. Key Terms Learned

* Database
* SQLite
* SQL
* Table
* Row
* Column
* Primary Key
* Cursor
* Connection
* Commit
* PRAGMA
* fetchall()

---

# 20. Best Practices

* Keep SQL in a separate `schema.sql` file.
* Always close database connections.
* Always commit database changes.
* Use `CREATE TABLE IF NOT EXISTS`.
* Separate database logic into `database.py`.
* Use meaningful table and column names.

---

# ✅ Day 1 Checklist

* [x] Understood what a database is.
* [x] Learned why databases are used.
* [x] Compared file storage with database storage.
* [x] Learned what SQLite is.
* [x] Learned Database terminology.
* [x] Created `students.db`.
* [x] Created the `students` table.
* [x] Learned `CREATE TABLE`.
* [x] Learned `PRIMARY KEY`.
* [x] Learned `sqlite3.connect()`.
* [x] Learned `cursor`.
* [x] Learned `commit()`.
* [x] Learned `close()`.
* [x] Learned `PRAGMA table_info()`.
* [x] Viewed the table structure.
* [x] Completed the Student Database Setup mini project.

---

# 🚀 Next Day Preview

**Phase 4 — Day 2: INSERT Data**

Topics:

* INSERT INTO
* Adding one record
* Adding multiple records
* Saving records permanently
* Viewing inserted data
* Student Registration System mini project
