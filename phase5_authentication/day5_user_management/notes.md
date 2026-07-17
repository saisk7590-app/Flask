# 🟣 PHASE 5 — DAY 5
# Protected Routes & User Management API

---

# 🎯 Goal

Learn how to protect API routes using JWT authentication and build a complete User Management API.

By the end of this lesson, you can:

- Protect API routes
- Verify JWT tokens
- Read Authorization headers
- Authenticate users
- Build profile APIs
- Update user information
- Delete user accounts
- Test a complete authentication system

---

# 📚 Concepts Learned

## 1. Protected Routes

A Protected Route is an API endpoint that can only be accessed by authenticated users.

Examples:

GET /profile

PUT /profile

DELETE /account

Public APIs:

POST /register

POST /login

---

## Why Protected Routes?

Sensitive user data should never be accessible to everyone.

Without authentication:

Anyone could access:

GET /profile

or

DELETE /account

This is a serious security issue.

Protected routes ensure only authenticated users can access their own data.

---

# Authentication Flow

User

↓

Login

↓

Server verifies password

↓

Generate JWT

↓

Return JWT

↓

Client stores JWT

↓

Client sends JWT with every protected request

↓

Server verifies JWT

↓

Allow access

---

# Authorization Header

JWT tokens are sent using the Authorization header.

Example:

Authorization: Bearer JWT_TOKEN

Example:

Authorization: Bearer eyJhbGc...

---

# Bearer Token

Bearer means:

"The client is presenting this token as proof of authentication."

The server still verifies the token before granting access.

---

# HTTP Request Structure

HTTP Request

↓

Request Line

↓

Headers

↓

Body

The Authorization header is inside the Headers section.

---

# Reading Headers in Flask

```python
request.headers.get("Authorization")
```

Returns:

```text
Bearer eyJhbGc...
```

If missing:

Returns:

```python
None
```

---

# Splitting the Header

Example:

```text
Bearer abc123
```

Using:

```python
authorization_header.split()
```

Returns:

```python
["Bearer", "abc123"]
```

Token:

```python
token = parts[1]
```

---

# JWT Verification

```python
payload = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)
```

JWT verification automatically checks:

- Signature
- Secret Key
- Algorithm
- Expiration

If successful:

Returns payload.

---

# JWT Payload Example

```python
{
    "user_id": 1,
    "username": "Sai",
    "email": "sai@gmail.com",
    "exp": ...
}
```

---

# JWT Exceptions

Expired token:

```python
jwt.ExpiredSignatureError
```

Invalid token:

```python
jwt.InvalidTokenError
```

Return:

401 Unauthorized

---

# Authentication Helper

Instead of repeating JWT verification inside every route:

Create:

```python
authenticate_request()
```

Every protected route calls:

```python
payload, error = authenticate_request()
```

Benefits:

- Reusable
- Cleaner code
- Easier maintenance
- Follows DRY principle

---

# DRY Principle

DRY

=

Don't Repeat Yourself

Avoid copying the same authentication logic into every route.

---

# Protected Endpoints

GET /profile

Returns logged-in user's profile.

Requires JWT.

---

PUT /profile

Updates username.

Requires JWT.

---

DELETE /account

Deletes logged-in user's account.

Requires JWT.

---

# Authentication Lifecycle

Register

↓

Hash Password

↓

Store User

↓

Login

↓

Verify Password

↓

Generate JWT

↓

Return JWT

↓

Client Stores JWT

↓

Protected Request

↓

Authorization Header

↓

Verify JWT

↓

Extract User ID

↓

Database Query

↓

Return Response

---

# Project Structure

day5_user_management/

├── app.py

├── database.py

├── schema.sql

├── requests.http

├── users.db

├── requirements.txt

└── notes.md

---

# Files

## app.py

Contains:

- Register API
- Login API
- JWT generation
- JWT verification
- Protected routes
- Profile APIs

---

## database.py

Contains:

SQLite connection

Database initialization

---

## schema.sql

Creates users table.

---

## requests.http

Contains all API test requests.

---

## requirements.txt

Contains required packages.

---

# Packages Used

## Flask

Creates the REST API.

Install:

```powershell
pip install flask
```

---

## bcrypt

Hashes passwords securely.

Install:

```powershell
pip install bcrypt
```

Functions:

```python
bcrypt.hashpw()

bcrypt.checkpw()

bcrypt.gensalt()
```

---

## PyJWT

Creates and verifies JWT tokens.

Install:

```powershell
pip install PyJWT
```

Functions:

```python
jwt.encode()

jwt.decode()
```

---

# Functions Learned

request.headers.get()

Reads HTTP headers.

---

authorization_header.split()

Splits:

Bearer TOKEN

into

["Bearer", "TOKEN"]

---

jwt.decode()

Verifies JWT.

Returns payload.

---

bcrypt.hashpw()

Hashes passwords.

---

bcrypt.checkpw()

Verifies password.

---

get_connection()

Creates SQLite connection.

---

initialize_database()

Creates database tables.

---

# SQL Used

Register

```sql
INSERT INTO users
```

Login

```sql
SELECT *
FROM users
WHERE email = ?
```

Profile

```sql
SELECT id, username, email
FROM users
WHERE id = ?
```

Update

```sql
UPDATE users
SET username = ?
WHERE id = ?
```

Delete

```sql
DELETE FROM users
WHERE id = ?
```

---

# HTTP Status Codes

200 OK

Successful request.

---

201 Created

User registered.

---

400 Bad Request

Missing required data.

---

401 Unauthorized

Authentication failed.

Missing token

Invalid token

Expired token

Wrong password

---

404 Not Found

User no longer exists.

---

409 Conflict

Duplicate email.

---

# Complete Testing Flow

1.

Register

↓

201

---

2.

Login

↓

200

↓

Receive JWT

---

3.

GET /profile

↓

200

---

4.

PUT /profile

↓

200

---

5.

GET /profile

↓

Updated data

---

6.

DELETE /account

↓

200

---

7.

GET /profile

↓

404

---

# Common Mistakes

❌ Store plain passwords.

❌ Return password hash.

❌ Forget bcrypt.

❌ Forget JWT verification.

❌ Forget Authorization header.

❌ Forget Bearer keyword.

❌ Use different secret keys.

❌ Copy authentication code into every route.

❌ Trust user_id from request body.

---

# Best Practices

✅ Always hash passwords.

✅ Verify JWT before protected routes.

✅ Keep JWT payload small.

✅ Use Authorization header.

✅ Return proper HTTP status codes.

✅ Never expose password hashes.

✅ Keep authentication reusable.

✅ Use HTTPS in production.

✅ Store secrets in environment variables.

---

# Interview Questions

1. What is a protected route?

2. Difference between Authentication and Authorization?

3. What is JWT?

4. What are the three parts of JWT?

5. Why use bcrypt?

6. What is a salt?

7. Why not store passwords as plain text?

8. What is the Authorization header?

9. What is a Bearer token?

10. What does jwt.decode() verify?

11. What happens when a JWT expires?

12. Why use an authentication helper?

13. What is the DRY principle?

14. Why should protected routes verify every request?

15. What HTTP status code is returned for an invalid JWT?

---

# Summary

In Day 5, we built a complete authentication system.

The backend can now:

✅ Register users

✅ Hash passwords

✅ Verify passwords

✅ Generate JWTs

✅ Verify JWTs

✅ Protect routes

✅ Retrieve user profiles

✅ Update user profiles

✅ Delete user accounts

This completes a complete JWT-based Authentication & User Management API.

---

# ✅ Day 5 Completion Checklist

- [x] Understood protected routes
- [x] Learned Authorization header
- [x] Learned Bearer token
- [x] Read headers in Flask
- [x] Verified JWT using jwt.decode()
- [x] Handled expired tokens
- [x] Handled invalid tokens
- [x] Built authenticate_request() helper
- [x] Created GET /profile
- [x] Created PUT /profile
- [x] Created DELETE /account
- [x] Tested complete authentication flow
- [x] Understood project architecture
- [x] Completed User Management API
- [x] Completed Phase 5

---

# 🏆 Phase 5 Completed

You have successfully mastered:

- Authentication
- Authorization
- Password Hashing
- bcrypt
- Login Systems
- Sessions (Concepts)
- JWT Authentication
- JWT Verification
- Protected Routes
- User Management APIs
- Secure API Design

You are now ready to begin **🔴 Phase 6 — Advanced Backend**, where you'll learn middleware, validation, error handling, environment variables, MVC architecture, and scalable project structure.