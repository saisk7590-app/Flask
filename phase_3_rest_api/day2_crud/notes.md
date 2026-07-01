# 🟠 PHASE 3 — DAY 2

# CRUD Operations

---

# 🎯 Day Goal

Today is about understanding **CRUD Operations** and implementing them using Flask.

By the end of this day, you should understand:

* What CRUD is
* CRUD ↔ HTTP Method Mapping
* How to Create data
* How to Read data
* How to Update data
* How to Delete data
* How `request.json` works
* Using Python lists as a temporary database
* Building a complete CRUD REST API

---

# What is CRUD?

CRUD stands for:

* **C** → Create
* **R** → Read
* **U** → Update
* **D** → Delete

CRUD represents the four basic operations performed on data in almost every application.

Examples:

* WhatsApp Messages
* Student Records
* Products
* Employees
* Tasks
* Notes
* Expenses

---

# Why Do We Use CRUD?

Most applications need to:

* Add new data
* View existing data
* Edit existing data
* Delete unwanted data

Instead of creating different systems for each application, CRUD provides a standard way to manage data.

---

# Real-World Analogy

Imagine a notebook.

```text
Notebook

Write New Page
      │
      ▼
Create

Read Page
      │
      ▼
Read

Edit Page
      │
      ▼
Update

Remove Page
      │
      ▼
Delete
```

A REST API performs these same operations on data stored in a server or database.

---

# CRUD ↔ HTTP Methods

| CRUD Operation | HTTP Method | Purpose              |
| -------------- | ----------- | -------------------- |
| Create         | POST        | Add new data         |
| Read           | GET         | Retrieve data        |
| Update         | PUT         | Modify existing data |
| Delete         | DELETE      | Remove data          |

Examples:

```text
GET    /tasks
GET    /tasks/1

POST   /tasks

PUT    /tasks/1

DELETE /tasks/1
```

Notice that the endpoint remains the same.

Only the HTTP method changes.

---

# CRUD Flow

```text
Client
   │
HTTP Request
   │
   ▼
Flask Route
   │
Business Logic
   │
Python List
   │
   ▼
JSON Response
   │
Client
```

---

# Temporary Database

During this phase we are using a Python list instead of a real database.

Example:

```python
tasks = [
    {
        "id": 1,
        "title": "Learn Flask",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Learn REST APIs",
        "status": "Completed"
    }
]
```

Why?

Because we are learning REST concepts first.

In Phase 4, this list will be replaced with a real database.

---

# GET - Read Data

GET retrieves information from the server.

Collection Resource

```text
GET /tasks
```

Returns all tasks.

Example Response:

```json
[
    {
        "id":1,
        "title":"Learn Flask",
        "status":"Pending"
    },
    {
        "id":2,
        "title":"Learn REST APIs",
        "status":"Completed"
    }
]
```

Single Resource

```text
GET /tasks/1
```

Returns one specific task.

Example Response:

```json
{
    "id":1,
    "title":"Learn Flask",
    "status":"Pending"
}
```

---

# POST - Create Data

POST creates a new resource.

Example Request

```text
POST /tasks
```

Request Body

```json
{
    "title":"Learn CRUD",
    "status":"Pending"
}
```

Flask

```python
data = request.json
```

Create Dictionary

```python
new_task = {
    "id": len(tasks) + 1,
    "title": data["title"],
    "status": data["status"]
}
```

Add to List

```python
tasks.append(new_task)
```

Return Response

```json
{
    "message":"Task Created Successfully",
    "task":{
        "id":3,
        "title":"Learn CRUD",
        "status":"Pending"
    }
}
```

---

# What is request.json?

When the client sends JSON data,

```json
{
    "title":"Learn CRUD",
    "status":"Pending"
}
```

Flask converts it into a Python dictionary.

```python
data = request.json
```

Now,

```python
data["title"]
```

returns

```text
Learn CRUD
```

and

```python
data["status"]
```

returns

```text
Pending
```

---

# POST Request Flow

```text
Client
   │
POST /tasks
   │
JSON Body
   │
request.json
   │
Python Dictionary
   │
Create Task
   │
Append to List
   │
Return JSON Response
```

---

# PUT - Update Data

PUT modifies an existing resource.

Example

```text
PUT /tasks/1
```

Request Body

```json
{
    "title":"Master Flask",
    "status":"Completed"
}
```

Steps

1. Read request.json
2. Find the task
3. Update values
4. Return updated task

Example

```python
task["title"] = data["title"]
task["status"] = data["status"]
```

---

# PUT Request Flow

```text
Client
   │
PUT /tasks/1
   │
request.json
   │
Find Task
   │
Update Dictionary
   │
Return Updated Task
```

---

# DELETE - Delete Data

DELETE removes an existing resource.

Example

```text
DELETE /tasks/2
```

Flask

```python
tasks.remove(task)
```

Response

```json
{
    "message":"Task Deleted Successfully"
}
```

---

# DELETE Request Flow

```text
Client
   │
DELETE /tasks/2
   │
Find Task
   │
Remove from List
   │
Return Confirmation
```

---

# Working with Python Lists

Add Item

```python
tasks.append(new_task)
```

Update Item

```python
task["title"] = data["title"]
task["status"] = data["status"]
```

Delete Item

```python
tasks.remove(task)
```

Loop Through Items

```python
for task in tasks:
```

---

# Route Summary

| Method | Endpoint         | Purpose       |
| ------ | ---------------- | ------------- |
| GET    | /tasks           | Get all tasks |
| GET    | /tasks/<task_id> | Get one task  |
| POST   | /tasks           | Create task   |
| PUT    | /tasks/<task_id> | Update task   |
| DELETE | /tasks/<task_id> | Delete task   |

---

# Current ID Generation

Current approach:

```python
"id": len(tasks) + 1
```

This works while learning.

However, if a task is deleted, duplicate IDs can occur.

In real applications, IDs are usually generated automatically by the database.

---

# Common Beginner Mistakes

❌ Forgetting to import request

```python
from flask import Flask, jsonify
```

✅ Correct

```python
from flask import Flask, jsonify, request
```

---

❌ Forgetting request.json

```python
title = data["title"]
```

without creating

```python
data = request.json
```

---

❌ Forgetting append()

The task is created but never stored.

Always use

```python
tasks.append(new_task)
```

---

❌ Forgetting remove()

The DELETE endpoint runs but nothing is removed.

Always remove the task from the list.

---

❌ Forgetting to check whether the task exists

Always search first.

If not found, return

```json
{
    "message":"Task Not Found"
}
```

---

# Industry Best Practices

* Keep endpoints resource-based.
* Use meaningful variable names like `task_id`.
* Return JSON responses.
* Keep route names consistent.
* Use proper HTTP methods.
* Separate API logic clearly.
* Return appropriate status codes (covered in Day 3).
* Validate client input (covered in Day 3).

---

# Key Points to Remember

* CRUD is the foundation of backend development.
* POST creates data.
* GET reads data.
* PUT updates data.
* DELETE removes data.
* `request.json` converts JSON into a Python dictionary.
* `append()` adds new data.
* `remove()` deletes data.
* We use a Python list as a temporary database.
* REST uses the same resource URL with different HTTP methods.

---

# Day 2 Summary

```text
CRUD

Create
   │
POST
   │
request.json
   │
append()

Read
   │
GET
   │
Return JSON

Update
   │
PUT
   │
Modify Dictionary

Delete
   │
DELETE
   │
remove()
```

---

# Day 2 Completion Checklist

* ✅ I understand CRUD.
* ✅ I know the CRUD ↔ HTTP Method mapping.
* ✅ I can create data using POST.
* ✅ I can read data using GET.
* ✅ I can update data using PUT.
* ✅ I can delete data using DELETE.
* ✅ I understand `request.json`.
* ✅ I know how to use `append()`.
* ✅ I know how to update dictionaries.
* ✅ I know how to use `remove()`.
* ✅ I understand why we use a Python list before learning databases.
* ✅ I can build a complete CRUD API using Flask.
