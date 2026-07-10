# 📝 Phase 4 — Day 4 Notes
# UPDATE & DELETE (Full CRUD with SQLite)

---

# 🎯 Day Goal

Learn how to:

- Update existing records
- Delete records
- Complete CRUD operations
- Build a Student Management System

---

# 📚 Topics Covered

- UPDATE
- DELETE
- WHERE
- cursor.rowcount
- CRUD
- Parameterized Queries
- Student Management System

---

# 1. What is UPDATE?

The `UPDATE` statement is used to modify existing records in a database table.

Imagine a student changes their course or age.

Instead of deleting the student and adding them again, we simply update the existing record.

---

# SQL Syntax

```sql
UPDATE table_name
SET column_name = value
WHERE condition;
```

Example:

```sql
UPDATE students
SET age = 23
WHERE id = 1;
```

---

# Line-by-Line Explanation

```sql
UPDATE students
```

Selects the **students** table to update.

---

```sql
SET age = 23
```

Changes the value of the **age** column.

---

```sql
WHERE id = 1;
```

Updates only the student whose ID is **1**.

Without `WHERE`, every row in the table would be updated.

---

# 2. Updating Multiple Columns

You can update more than one column in a single query.

Example:

```sql
UPDATE students
SET
    age = 23,
    course = 'Full Stack Python'
WHERE id = 1;
```

---

# 3. Why WHERE is Important

Correct:

```sql
UPDATE students
SET age = 30
WHERE id = 2;
```

Only Student 2 is updated.

---

Wrong:

```sql
UPDATE students
SET age = 30;
```

Result:

Every student's age becomes **30**.

Always use a `WHERE` clause unless you intentionally want to update every record.

---

# 4. Parameterized UPDATE Query

Python:

```python
update_query = """
UPDATE students
SET age = ?
WHERE id = ?
"""

cursor.execute(update_query, (new_age, student_id))
```

Benefits:

- Prevents SQL Injection
- Cleaner code
- Industry standard

---

# 5. cursor.rowcount

After executing an UPDATE or DELETE query:

```python
cursor.rowcount
```

returns the number of rows affected.

Example:

Existing ID:

```python
update_student_age(2, 25)
```

Result:

```text
rowcount = 1
```

Non-existing ID:

```python
update_student_age(100, 30)
```

Result:

```text
rowcount = 0
```

---

# Why use rowcount?

Instead of always displaying:

```text
Student updated successfully.
```

we check whether a row was actually updated.

Example:

```python
if cursor.rowcount > 0:
    print("Student updated.")
else:
    print("Student not found.")
```

This makes the application more accurate and professional.

---

# 6. What is DELETE?

The `DELETE` statement removes records from a table.

Example:

Before:

| ID | Name |
|----|------|
|1|Sai|
|2|Rahul|
|3|Anjali|

Delete:

```sql
DELETE FROM students
WHERE id = 2;
```

After:

| ID | Name |
|----|------|
|1|Sai|
|3|Anjali|

Student 2 has been removed.

---

# SQL Syntax

```sql
DELETE FROM table_name
WHERE condition;
```

Example:

```sql
DELETE FROM students
WHERE id = 5;
```

---

# Why WHERE is Important in DELETE

Correct:

```sql
DELETE FROM students
WHERE id = 4;
```

Deletes only Student 4.

---

Wrong:

```sql
DELETE FROM students;
```

This deletes **every record** in the table.

This is one of the most dangerous SQL mistakes.

---

# 7. Parameterized DELETE Query

```python
delete_query = """
DELETE FROM students
WHERE id = ?
"""

cursor.execute(delete_query, (student_id,))
```

Always use placeholders (`?`) instead of string formatting.

---

# 8. CRUD Operations

CRUD stands for:

| Operation | SQL Command | Purpose |
|-----------|-------------|---------|
| Create | INSERT | Add new records |
| Read | SELECT | Retrieve records |
| Update | UPDATE | Modify existing records |
| Delete | DELETE | Remove records |

By the end of Day 4, you have implemented all four operations.

---

# 9. Flow Diagram

## UPDATE

```text
Python Function
      │
      ▼
UPDATE Query
      │
      ▼
SQLite Database
      │
      ▼
Matching Row Found?
      │
      ├───────────────┐
      │               │
     Yes              No
      │               │
      ▼               ▼
Update Record     No Changes
      │
      ▼
Commit Changes
```

---

## DELETE

```text
Python Function
      │
      ▼
DELETE Query
      │
      ▼
SQLite Database
      │
      ▼
Matching Row Found?
      │
      ├───────────────┐
      │               │
     Yes              No
      │               │
      ▼               ▼
Delete Record     No Changes
      │
      ▼
Commit Changes
```

---

# 10. Student Management System

Functions Created:

```python
display_students()
```

Displays all students.

---

```python
add_student()
```

Adds a new student.

---

```python
update_student_age()
```

Updates a student's age.

---

```python
update_student_course()
```

Updates a student's course.

---

```python
delete_student()
```

Deletes a student.

---

# 11. Best Practices Learned

✔ Use parameterized queries (`?`).

✔ Always use `WHERE` with `UPDATE` and `DELETE`.

✔ Check `cursor.rowcount` after modifying data.

✔ Commit changes using:

```python
connection.commit()
```

✔ Close the database connection:

```python
connection.close()
```

✔ Organize SQL into reusable functions.

✔ Give SQL queries meaningful variable names (`insert_query`, `update_query`, `delete_query`, `select_query`).

---

# 12. Real-World Usage

In a production application:

Updating a user profile:

```sql
UPDATE users
SET email = 'new@example.com'
WHERE id = 15;
```

Deleting a product:

```sql
DELETE FROM products
WHERE id = 20;
```

Changing an employee's salary:

```sql
UPDATE employees
SET salary = 70000
WHERE employee_id = 101;
```

These operations are used daily in backend development.

---

# 13. Key Terms Learned

- UPDATE
- DELETE
- SET
- WHERE
- cursor.rowcount
- CRUD
- Parameterized Query
- Commit
- SQLite
- Student Management System

---

# 14. Day 4 Summary

Today you completed the final two CRUD operations:

- Updated student information.
- Deleted student records.
- Verified database changes using `cursor.rowcount`.
- Built a complete Student Management System.
- Learned safe database modification practices.

You now understand the complete CRUD workflow using SQLite and Python.

---

# 🧠 Assessment Questions

1. What does the UPDATE statement do?

2. Why should UPDATE usually include a WHERE clause?

3. What happens if you execute:

```sql
DELETE FROM students;
```

4. What is the purpose of `cursor.rowcount`?

5. Why do we use parameterized queries instead of string formatting?

6. What does CRUD stand for?

7. Which SQL statement removes records from a table?

8. Why is `connection.commit()` required after UPDATE and DELETE?

9. What happens if an UPDATE query matches no rows?

10. Why should database connections be closed after operations?

---

# ✅ Day 4 Completion Checklist

- [x] Learned UPDATE statement
- [x] Updated student age
- [x] Updated student course
- [x] Learned DELETE statement
- [x] Deleted student records
- [x] Understood the importance of WHERE
- [x] Used parameterized queries
- [x] Learned cursor.rowcount
- [x] Completed all CRUD operations
- [x] Built Student Management System

---

# 🎉 Phase 4 Progress

| Day | Status |
|------|--------|
| Day 1 — Database Fundamentals | ✅ Completed |
| Day 2 — INSERT | ✅ Completed |
| Day 3 — SELECT | ✅ Completed |
| Day 4 — UPDATE & DELETE | ✅ Completed |
| Day 5 — Flask + SQLite | ⏳ Next |

---

# 🚀 Next Day Preview

## 📅 Phase 4 — Day 5

### Flask + SQLite Integration

Topics:

- sqlite3 module
- Database connection in Flask
- GET API with SQLite
- POST API with SQLite
- PUT API with SQLite
- DELETE API with SQLite
- Replacing Python lists with real database storage
- Building a Student REST API using Flask + SQLite

By the end of Day 5, your Flask APIs will perform real database operations instead of using Python lists, making your backend much closer to a production-ready application.