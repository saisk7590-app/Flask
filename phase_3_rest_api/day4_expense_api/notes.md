# 🟠 PHASE 3 — DAY 4

# Expense Tracker API

---

# 🎯 Day Goal

Today we built a complete **Expense Tracker REST API** using Flask.

By the end of this day, you should understand:

- REST API design
- CRUD operations
- Multiple API endpoints
- Request validation
- Status codes
- Consistent JSON responses
- Managing resources using a Python list

---

# What is an Expense Tracker?

An Expense Tracker is an application that records money spent on different things.

Examples:

- Food
- Travel
- Shopping
- Bills
- Entertainment
- Healthcare

Each expense is considered a **resource**.

Example:

```json
{
    "id": 1,
    "amount": 250,
    "category": "Food",
    "description": "Lunch",
    "payment_method": "UPI"
}
```

---

# Expense Resource

Each expense contains the following fields:

| Field | Description |
|--------|-------------|
| id | Unique identifier |
| amount | Amount spent |
| category | Expense category |
| description | Short description |
| payment_method | How the payment was made |

Example:

```json
{
    "id": 3,
    "amount": 850,
    "category": "Shopping",
    "description": "Shoes",
    "payment_method": "Credit Card"
}
```

---

# REST Endpoints

| HTTP Method | Endpoint | Purpose |
|-------------|----------|---------|
| GET | /expenses | Get all expenses |
| GET | /expenses/<id> | Get one expense |
| POST | /expenses | Create new expense |
| PUT | /expenses/<id> | Update expense |
| DELETE | /expenses/<id> | Delete expense |

---

# CRUD Mapping

| CRUD Operation | HTTP Method |
|---------------|-------------|
| Create | POST |
| Read | GET |
| Update | PUT |
| Delete | DELETE |

---

# Request → Response Flow

```
Client
   │
HTTP Request
   │
   ▼
Expense API
   │
Validate Request
   │
   ├───────────────┐
   │               │
Valid          Invalid
   │               │
Process      Return 400
   │
Find Resource
   │
   ├───────────────┐
   │               │
Found        Not Found
   │               │
Return Data   Return 404
```

---

# Temporary Storage

During this phase we store data in a Python list.

Example:

```python
expenses = [
    {
        "id": 1,
        "amount": 250,
        "category": "Food",
        "description": "Lunch",
        "payment_method": "UPI"
    }
]
```

This is called **temporary (in-memory) storage**.

### Limitation

If the Flask server restarts, all data is lost.

Example:

```
Start Server
      │
Add Expenses
      │
Stop Server
      │
Restart Server
      │
Expenses Lost
```

This is why databases are introduced in the next phase.

---

# GET Request

Retrieve all expenses.

Example:

```http
GET /expenses
```

Response:

```json
{
    "success": true,
    "count": 2,
    "data": [
        ...
    ]
}
```

---

# GET by ID

Retrieve a single expense.

Example:

```http
GET /expenses/1
```

If found:

```http
200 OK
```

If not found:

```http
404 Not Found
```

---

# POST Request

Create a new expense.

Example:

```http
POST /expenses
```

Request Body:

```json
{
    "amount": 500,
    "category": "Shopping",
    "description": "Shoes",
    "payment_method": "Credit Card"
}
```

Response:

```http
201 Created
```

---

# PUT Request

Update an existing expense.

Example:

```http
PUT /expenses/1
```

Response:

```http
200 OK
```

If the expense doesn't exist:

```http
404 Not Found
```

---

# DELETE Request

Delete an expense.

Example:

```http
DELETE /expenses/2
```

Response:

```http
200 OK
```

If the expense doesn't exist:

```http
404 Not Found
```

---

# Request Validation

Before creating or updating an expense, validate the request.

Example:

```python
data = request.json

if not data:
    return jsonify({
        "success": False,
        "message": "Request body is required"
    }), 400
```

---

# Required Field Validation

Ensure all required fields are present.

Example:

```python
required_fields = [
    "amount",
    "category",
    "description",
    "payment_method"
]

for field in required_fields:
    if field not in data:
        return jsonify({
            "success": False,
            "message": f"{field} is required"
        }), 400
```

This prevents incomplete data from being stored.

---

# HTTP Status Codes Used

## 200 OK

Used when:

- GET succeeds
- PUT succeeds
- DELETE succeeds

---

## 201 Created

Used when:

- A new expense is created successfully.

---

## 400 Bad Request

Used when:

- Request body is missing.
- Required fields are missing.
- Client sends invalid data.

---

## 404 Not Found

Used when:

- Expense ID does not exist.

---

# Consistent JSON Response Format

## Success Response

```json
{
    "success": true,
    "message": "Expense Created Successfully",
    "data": {
        ...
    }
}
```

## Error Response

```json
{
    "success": false,
    "message": "Expense Not Found"
}
```

Using a consistent response structure makes it easier for frontend applications to process API responses.

---

# Industry Best Practices

✔ Use plural resource names.

```
/expenses
```

✔ Validate request data before processing.

✔ Return proper HTTP status codes.

✔ Keep response format consistent.

✔ Use meaningful field names.

✔ Return JSON instead of plain text.

---

# Common Beginner Mistakes

## ❌ Using verbs in URLs

Bad:

```
/createExpense
/deleteExpense
/updateExpense
```

Good:

```
POST /expenses
DELETE /expenses/1
PUT /expenses/1
```

---

## ❌ Returning 200 for every request

Always return the appropriate status code.

Example:

```
201 Created
404 Not Found
400 Bad Request
```

---

## ❌ Not validating request data

Always check:

- Request body exists.
- Required fields are present.

---

## ❌ Inconsistent JSON responses

Bad:

```json
{
    "expense": {}
}
```

Another endpoint:

```json
{
    "data": {}
}
```

Good:

Always use:

```json
{
    "success": true,
    "message": "...",
    "data": {}
}
```

---

# Key Points to Remember

- An expense is a REST resource.
- REST APIs use CRUD operations.
- Resources are managed using HTTP methods.
- Validate request data before processing.
- Return proper HTTP status codes.
- Keep JSON responses consistent.
- Python lists provide temporary storage only.
- Databases will replace list storage in the next phase.

---

# Day 4 Summary

```
Expense Tracker API
        │
        ├── GET /expenses
        ├── GET /expenses/{id}
        ├── POST /expenses
        ├── PUT /expenses/{id}
        ├── DELETE /expenses/{id}
        │
        ├── Validation
        ├── Status Codes
        ├── JSON Responses
        └── Temporary Storage (Python List)
```

---

# Day 4 Completion Checklist

- ✅ I understand the Expense resource.
- ✅ I can build CRUD APIs.
- ✅ I can create expenses.
- ✅ I can retrieve expenses.
- ✅ I can update expenses.
- ✅ I can delete expenses.
- ✅ I can validate request data.
- ✅ I know when to return 200, 201, 400 and 404.
- ✅ I can return consistent JSON responses.
- ✅ I understand the limitation of Python list storage.
- ✅ I can test APIs using requests.http.

---

# What I Have Mastered So Far

## Day 1

- REST Fundamentals
- Resources
- Endpoints
- URL Design
- HTTP Methods

## Day 2

- CRUD Operations
- GET
- POST
- PUT
- DELETE
- Request JSON
- List-based storage

## Day 3

- HTTP Status Codes
- Input Validation
- Error Responses
- Consistent JSON

## Day 4

- Building a larger REST API
- Expense Tracker CRUD
- Request Validation
- Professional API Responses
- Structuring multiple endpoints