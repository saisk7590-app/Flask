# 📝 Phase 4 — Day 2 Notes
# INSERT Data into SQLite

---

# 🎯 Day Goal

Learn:

- INSERT INTO
- Add one record
- Add multiple records
- Verify stored data
- Student Registration System

---

# 1. What is INSERT?

INSERT is an SQL command used to add new records into a table.

Example:

```sql
INSERT INTO students (name, age, course)
VALUES ('Sai',21,'Python');
```

Meaning:

Insert one new row into the students table.

---

# 2. INSERT Syntax

```sql
INSERT INTO table_name (column1,column2,column3)
VALUES(value1,value2,value3);
```

Explanation

INSERT INTO

→ Add new data.

table_name

→ Table where data will be inserted.

(column1,column2)

→ Columns receiving data.

VALUES

→ Actual values.

---

# 3. Why don't we insert id?

Our table:

```sql
id INTEGER PRIMARY KEY
```

SQLite automatically generates IDs.

Example

First insert

ID = 1

Second insert

ID = 2

Third insert

ID = 3

No need to manually provide IDs.

---

# 4. Parameterized Queries

Instead of

```python
"INSERT INTO students VALUES ('Sai',21,'Python')"
```

use

```python
cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ("Sai",21,"Python")
)
```

Benefits

- Prevents SQL Injection
- Cleaner
- Easier to maintain
- Industry standard

---

# 5. execute()

Used for one SQL execution.

Example

```python
cursor.execute(query, student)
```

Used for

- One INSERT
- One UPDATE
- One DELETE
- One SELECT

---

# 6. executemany()

Used to execute the same SQL query multiple times.

Example

```python
students = [
    ("Sai",21,"Python"),
    ("Rahul",20,"Flutter"),
    ("Anjali",22,"Java")
]

cursor.executemany(query, students)
```

Benefits

- Faster
- Less code
- Better performance

Called a Bulk Insert.

---

# 7. fetchall()

```python
students = cursor.fetchall()
```

Returns all rows from the SQL query.

Return type

Python List of Tuples

Example

```python
[
 (1,'Sai',21,'Python'),
 (2,'Rahul',20,'Flutter')
]
```

---

# 8. commit()

```python
connection.commit()
```

Saves changes permanently.

Without commit

Inserted records may not be saved.

---

# 9. close()

```python
connection.close()
```

Always close the database connection.

Benefits

- Releases resources
- Prevents connection leaks
- Good practice

---

# 10. Workflow

```
Python Program
      │
      ▼
Connect Database
      │
      ▼
Cursor
      │
      ▼
INSERT Query
      │
      ▼
SQLite Database
      │
      ▼
commit()
      │
      ▼
close()
```

---

# 11. Key Terms Learned

- INSERT
- VALUES
- execute()
- executemany()
- fetchall()
- commit()
- SQLite Connection
- Cursor
- Bulk Insert
- Parameterized Query

---

# 12. Best Practices

- Use parameterized queries (`?`)
- Use `executemany()` for bulk inserts
- Commit after data changes
- Close database connections
- Use meaningful variable names
- Keep SQL readable with multiline strings

---

# ✅ Day 2 Checklist

- [x] Learned INSERT INTO
- [x] Inserted one student
- [x] Inserted multiple students
- [x] Learned execute()
- [x] Learned executemany()
- [x] Learned fetchall()
- [x] Learned commit()
- [x] Learned close()
- [x] Verified stored data
- [x] Completed Student Registration System

---

# 🚀 Next Day

## Phase 4 — Day 3

Topics

- SELECT
- WHERE
- ORDER BY
- Search by ID
- Search by Name
- Student Search System