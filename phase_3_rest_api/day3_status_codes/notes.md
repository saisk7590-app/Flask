# 🟠 PHASE 3 — DAY 3

# Status Codes & Error Responses

---

# 🎯 Day Goal

Learn how professional REST APIs communicate success and failure using HTTP status codes.

By the end of this day, you should understand:

- HTTP Status Codes
- Success vs Error Responses
- 200 OK
- 201 Created
- 400 Bad Request
- 404 Not Found
- 500 Internal Server Error
- Request Validation
- Consistent JSON Responses

---

# What is an HTTP Status Code?

An HTTP Status Code is a three-digit number returned by the server along with every response.

It tells the client whether the request was successful or failed.

Example:

Request

```http
GET /students/1
```

Response

```http
HTTP/1.1 200 OK
```

```json
{
    "id":1,
    "name":"Sai"
}
```

The JSON contains the data.

The status code tells the client the result of the request.

---

# Why Are Status Codes Important?

Suppose an API always returned:

```http
200 OK
```

even when something failed.

Example:

```json
{
    "message":"Student Not Found"
}
```

The frontend would think the request was successful.

Instead:

```http
404 Not Found
```

clearly tells the client that the resource does not exist.

Status codes allow applications to react correctly without reading every response message.

---

# Common HTTP Status Codes

## ✅ 200 OK

Meaning:

The request completed successfully.

Used for:

- GET
- Successful PUT
- Successful DELETE
- Successful validation

Example

```http
GET /students/1
```

Response

```http
200 OK
```

---

## ✅ 201 Created

Meaning:

A new resource was created successfully.

Used for:

```http
POST /students
```

Response

```http
201 Created
```

---

## ✅ 400 Bad Request

Meaning:

The client sent invalid or incomplete data.

Examples:

Missing JSON body

```json
{}
```

Missing required fields

```json
{
    "age":22
}
```

Response

```http
400 Bad Request
```

---

## ✅ 404 Not Found

Meaning:

The requested resource does not exist.

Example

```http
GET /students/100
```

Response

```http
404 Not Found
```

---

## ✅ 500 Internal Server Error

Meaning:

An unexpected error occurred on the server.

Examples:

- Division by zero
- Database crash
- Programming errors
- Unhandled exceptions

Example

```python
result = 10 / 0
```

Flask automatically returns:

```http
500 Internal Server Error
```

---

# Success vs Error Responses

Success Response

```json
{
    "success": true,
    "message": "Student Found",
    "data": {
        "id":1,
        "name":"Sai"
    }
}
```

Error Response

```json
{
    "success": false,
    "message": "Student Not Found"
}
```

Using a consistent structure makes APIs easier for frontend developers to use.

---

# Request Validation

Before processing data, always validate it.

Example

```python
data = request.json

if not data:
    return jsonify({
        "success": False,
        "message": "Request Body Required"
    }), 400
```

Check required fields

```python
if "name" not in data:
    return jsonify({
        "success": False,
        "message": "Name is Required"
    }), 400
```

Validation prevents runtime errors and ensures only valid data is processed.

---

# Request Flow

```
Client
   │
   ▼
HTTP Request
   │
   ▼
Validate Request
   │
   ├───────────────┐
   │               │
Valid           Invalid
   │               │
Process      Return 400
   │
   ▼
Find Resource
   │
   ├───────────────┐
   │               │
Found        Not Found
   │               │
Return 200     Return 404
```

---

# Difference Between Client Errors and Server Errors

| Type | Meaning | Examples |
|------|---------|----------|
| 2xx | Success | 200, 201 |
| 4xx | Client Error | 400, 404 |
| 5xx | Server Error | 500 |

Client errors mean the client made a mistake.

Server errors mean the backend failed unexpectedly.

---

# Industry Best Practices

✔ Always return the correct status code.

✔ Validate request data before processing.

✔ Use consistent JSON responses.

✔ Include meaningful error messages.

✔ Don't expose internal server details in production.

---

# Common Beginner Mistakes

❌ Returning 200 for every response.

✅ Return the appropriate status code.

---

❌ Not validating request data.

✅ Validate request body and required fields.

---

❌ Returning different JSON structures.

✅ Keep response format consistent.

---

# Key Points to Remember

- Every HTTP response includes a status code.
- Status codes help clients understand the result.
- 200 → Success.
- 201 → Resource created.
- 400 → Invalid request.
- 404 → Resource not found.
- 500 → Server error.
- Always validate incoming data.
- Use consistent JSON responses.

---

# Day 3 Summary

```
HTTP Response
      │
      ├── Status Code
      │      │
      │      ├── 200 OK
      │      ├── 201 Created
      │      ├── 400 Bad Request
      │      ├── 404 Not Found
      │      └── 500 Internal Server Error
      │
      └── JSON Response
             │
             ├── success
             ├── message
             └── data
```

---

# Day 3 Completion Checklist

- ✅ I understand HTTP Status Codes.
- ✅ I know when to use 200 OK.
- ✅ I know when to use 201 Created.
- ✅ I know when to use 400 Bad Request.
- ✅ I know when to use 404 Not Found.
- ✅ I know when to use 500 Internal Server Error.
- ✅ I can validate request data.
- ✅ I can return consistent JSON responses.
- ✅ I understand client errors vs server errors.
- ✅ I can build more professional REST APIs.