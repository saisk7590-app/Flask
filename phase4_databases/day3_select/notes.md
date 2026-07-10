# 📝 Phase 4 — Day 3 Notes
# SELECT Data

---

# 🎯 Day Goal

Learn how to retrieve data from a database using SQL.

Topics covered:

- SELECT
- SELECT *
- WHERE
- ORDER BY
- fetchall()
- fetchone()

---

# 1. What is SELECT?

`SELECT` is an SQL command used to retrieve (read) data from a table.

Syntax:

```sql
SELECT column_name
FROM table_name;
```

To retrieve all columns:

```sql
SELECT *
FROM students;
```

`*` means "all columns."

---

# 2. fetchall()

```python
students = cursor.fetchall()
```

Returns **all matching rows**.

Return type:

```python
[
    (1, "Sai", 21, "Python"),
    (2, "Rahul", 20, "Flutter")
]
```

---

# 3. fetchone()

```python
student = cursor.fetchone()
```

Returns only the **first matching row**.

Useful when searching by a unique field like `id`.

---

# 4. WHERE Clause

The `WHERE` clause filters rows.

Example:

```sql
SELECT *
FROM students
WHERE id = 3;
```

Search by name:

```sql
SELECT *
FROM students
WHERE name = 'Rahul';
```

Always use parameterized queries in Python:

```python
cursor.execute(query, ("Rahul",))
```

---

# 5. ORDER BY

Sorts query results.

Ascending:

```sql
SELECT *
FROM students
ORDER BY age ASC;
```

Descending:

```sql
SELECT *
FROM students
ORDER BY age DESC;
```

Alphabetical:

```sql
SELECT *
FROM students
ORDER BY name ASC;
```

Reverse alphabetical:

```sql
SELECT *
FROM students
ORDER BY name DESC;
```

---

# 6. ASC vs DESC

- `ASC` → Ascending (A→Z, Small→Large)
- `DESC` → Descending (Z→A, Large→Small)

---

# 7. Parameterized Queries

Use placeholders (`?`) instead of string concatenation.

Correct:

```python
cursor.execute(query, (student_id,))
```

Benefits:

- Prevents SQL Injection
- Cleaner code
- Easier maintenance

---

# 8. Workflow

```text
Python Program
      │
      ▼
Connect to Database
      │
      ▼
Execute SELECT Query
      │
      ▼
SQLite Database
      │
      ▼
Rows Returned
      │
      ▼
fetchall() / fetchone()
      │
      ▼
Display Results
```

---

# 9. Key Terms Learned

- SELECT
- SELECT *
- WHERE
- ORDER BY
- ASC
- DESC
- fetchall()
- fetchone()
- Parameterized Query

---

# 10. Best Practices

- Use `SELECT *` only when all columns are needed.
- Use `WHERE` to filter records.
- Use `ORDER BY` to sort data.
- Always use placeholders (`?`) with `WHERE`.
- Use meaningful SQL variable names (`select_query`, `insert_query`).

---

# ✅ Day 3 Checklist

- [x] Learned SELECT
- [x] Retrieved all students
- [x] Used fetchall()
- [x] Used fetchone()
- [x] Searched by ID
- [x] Searched by Name
- [x] Learned WHERE
- [x] Learned ORDER BY
- [x] Sorted data using ASC and DESC
- [x] Built Student Search System

---

# 🚀 Next Day Preview

## Phase 4 — Day 4

Topics:

- UPDATE
- DELETE
- Full CRUD Operations
- Student Management System