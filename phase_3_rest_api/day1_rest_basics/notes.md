# 🟠 PHASE 3 — DAY 1

# REST API Fundamentals

---

# 🎯 Day Goal

Today is about understanding **REST APIs**.

By the end of this day, you should understand:

* What REST is
* Why REST is used
* What a Resource is
* What an Endpoint is
* Collection vs Single Resource
* HTTP Methods
* REST URL Design
* Path Parameters
* Query Parameters

---

# What is REST?

REST stands for:

**Representational State Transfer**

REST is **not**:

* A programming language ❌
* A framework ❌

REST **is**:

* An architectural style
* A set of guidelines for designing APIs

It helps developers build APIs that are:

* Simple
* Consistent
* Scalable
* Easy to understand
* Easy to maintain

---

# Why Do We Use REST?

Without REST, every developer could create APIs differently.

Example:

```
/getTasks
/createTask
/deleteTask
/updateTask
```

Another developer might write:

```
/tasksList
/newTask
/removeTask
```

There is no consistency.

REST provides one standard so everyone designs APIs similarly.

---

# Real-World Analogy

Imagine a restaurant.

```
Customer
     │
     │ Order Food
     ▼
Waiter (REST API)
     │
     ▼
Kitchen (Server)
     │
     ▼
Food Prepared
     │
     ▲
Waiter
     │
     ▲
Customer
```

The waiter acts as the API between the customer and the kitchen.

---

# What is a Resource?

A resource is any data your API manages.

Examples:

```
Students
Tasks
Books
Products
Orders
Users
Expenses
Notes
```

REST designs APIs around resources.

Examples:

```
/students
/tasks
/books
/products
```

Resources are usually **nouns**, not verbs.

---

# What is an Endpoint?

An endpoint is a URL that clients use to communicate with the backend.

Example:

```
GET /students
```

Here:

* Resource → students
* Endpoint → /students
* Method → GET

Another example:

```
GET /students/1001
```

This endpoint refers to one specific student.

---

# Collection vs Single Resource

Collection Endpoint

Returns all resources.

Example:

```
GET /students
```

Response:

```json
[
    {
        "id":1001,
        "name":"Sai"
    },
    {
        "id":1002,
        "name":"John"
    }
]
```

Single Resource Endpoint

Returns one resource.

Example:

```
GET /students/1001
```

Response:

```json
{
    "id":1001,
    "name":"Sai"
}
```

---

# HTTP Methods

REST combines a resource with an HTTP method.

| Method | Purpose     |
| ------ | ----------- |
| GET    | Read data   |
| POST   | Create data |
| PUT    | Update data |
| DELETE | Delete data |

Examples:

```
GET /tasks
POST /tasks
PUT /tasks/1
DELETE /tasks/1
```

Notice that the URL stays the same.

Only the HTTP method changes.

---

# Resource-Based URL Design

❌ Bad

```
/getStudents
/addStudent
/deleteStudent
/updateStudent
```

✅ Good

```
GET /students
POST /students
GET /students/1001
PUT /students/1001
DELETE /students/1001
```

REST focuses on resources instead of actions.

---

# URL Design Best Practices

Always:

* Use lowercase
* Use plural nouns
* Keep URLs simple
* Avoid verbs

Good:

```
/students
/books
/tasks
/orders
/products
```

Bad:

```
/GetStudents
/addStudent
/DeleteBook
```

---

# Path Parameters

A path parameter identifies a specific resource.

Example:

```
GET /students/1001
```

Here:

```
1001
```

is the path parameter.

More examples:

```
/books/10
/products/5
/tasks/2
```

---

# Query Parameters

Query parameters filter or modify results.

Example:

```
GET /students?course=BDS
```

```
course=BDS
```

is the query parameter.

More examples:

```
GET /tasks?status=completed

GET /products?price=1000

GET /books?author=James
```

Simple rule:

* Path Parameter → Identifies one resource.
* Query Parameter → Filters resources.

---

# Request → Response Flow

```
Client
   │
Request
   │
   ▼
REST API
   │
   ▼
Server
   │
Business Logic
   │
Database
   │
   ▲
Response
   │
Client
```

Every REST API follows this pattern.

---

# API Design Flow

When designing an API, ask yourself:

```
What resource am I managing?
          │
          ▼
What operations are needed?
          │
          ▼
Which HTTP methods fit?
          │
          ▼
Design the endpoints
```

Example:

Resource:

```
Students
```

Operations:

```
View All
View One
Create
Update
Delete
```

REST Design:

```
GET    /students
GET    /students/{id}
POST   /students
PUT    /students/{id}
DELETE /students/{id}
```

---

# Flask Example

```python
@app.get("/tasks")
def get_tasks():
    pass

@app.get("/tasks/<int:id>")
def get_task(id):
    pass

@app.post("/tasks")
def create_task():
    pass

@app.put("/tasks/<int:id>")
def update_task(id):
    pass

@app.delete("/tasks/<int:id>")
def delete_task(id):
    pass
```

Notice:

The endpoint stays consistent.

Only the HTTP method changes.

---

# Real-World REST Examples

Student API

```
GET /students

GET /students/1001

POST /students

PUT /students/1001

DELETE /students/1001
```

Book API

```
GET /books

GET /books/10

POST /books

PUT /books/10

DELETE /books/10
```

Expense API

```
GET /expenses

POST /expenses

PUT /expenses/5

DELETE /expenses/5
```

---

# Common Beginner Mistakes

❌ Using verbs in URLs

```
/createStudent
```

✅ Correct

```
POST /students
```

---

❌ Using singular resources

```
/student
```

✅ Better

```
/students
```

---

❌ Mixing actions with URLs

```
/deleteTask
```

✅ Correct

```
DELETE /tasks/5
```

---

# Key Points to Remember

* REST is an architectural style.
* REST is not a framework.
* APIs should be resource-based.
* Resources are nouns.
* Endpoints are URLs.
* GET reads data.
* POST creates data.
* PUT updates data.
* DELETE removes data.
* Path parameters identify resources.
* Query parameters filter resources.

---

# Day 1 Summary

```
REST
   │
   ├── Resources
   ├── Endpoints
   ├── HTTP Methods
   ├── URL Design
   ├── Path Parameters
   └── Query Parameters
```

---

# Day 1 Completion Checklist

* ✅ I understand what REST is.
* ✅ I know why REST is used.
* ✅ I understand resources.
* ✅ I understand endpoints.
* ✅ I know the four main HTTP methods.
* ✅ I can design REST URLs.
* ✅ I understand collection vs single resource.
* ✅ I understand path parameters.
* ✅ I understand query parameters.
* ✅ I can design REST APIs before writing code.
