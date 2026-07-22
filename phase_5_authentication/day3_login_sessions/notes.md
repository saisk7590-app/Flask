# 🟣 Phase 5 — Day 3: Login System + Sessions

## 🎯 Day Goal

Learn how users log in securely by understanding:

* Login Fundamentals
* Password Verification
* `bcrypt.checkpw()`
* HTTP Statelessness
* Sessions
* Cookies
* Login API using Flask + SQLite + bcrypt

---

# Login System Overview

A login system verifies that a user is who they claim to be.

Unlike registration, login **does not create a new account**.

It checks whether the provided credentials match an existing user.

---

# Registration vs Login

## Registration

Purpose:

Create a new user account.

Flow:

```text
User
   │
   ▼
Enter Username
Enter Email
Enter Password
   │
   ▼
Hash Password
   │
   ▼
Store User in Database
```

---

## Login

Purpose:

Verify an existing user's identity.

Flow:

```text
User
   │
   ▼
Enter Email
Enter Password
   │
   ▼
Find User
   │
   ▼
Verify Password
   │
   ▼
Login Successful
```

---

# Login Process

Complete flow:

```text
User
   │
   ▼
POST /login
   │
   ▼
Validate Input
   │
   ▼
Find User by Email
   │
   ▼
User Exists?
 ┌──────┴──────┐
 │             │
No            Yes
 │             │
 ▼             ▼
401      Verify Password
               │
         ┌─────┴─────┐
         │           │
      False        True
         │           │
         ▼           ▼
401      Login Success
```

---

# Password Verification

During registration:

```python
bcrypt.hashpw()
```

creates and stores a secure password hash.

During login:

```python
bcrypt.checkpw()
```

verifies the entered password against the stored hash.

---

# Why Don't We Hash Again During Login?

Every call to:

```python
bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)
```

creates a **new random salt**, producing a different hash.

Example:

```text
hello123

↓

Hash A
```

Later:

```text
hello123

↓

Hash B
```

Hash A ≠ Hash B

Therefore we use:

```python
bcrypt.checkpw()
```

which extracts the original salt from the stored hash automatically.

---

# bcrypt.checkpw()

Syntax:

```python
bcrypt.checkpw(
    entered_password.encode("utf-8"),
    stored_hash.encode("utf-8")
)
```

Returns:

* `True` → Password is correct.
* `False` → Password is incorrect.

---

# Login Validation Steps

A secure login system performs these checks:

1. Email provided?
2. Password provided?
3. User exists?
4. Password matches?

If any check fails, login is rejected.

---

# HTTP is Stateless

## Definition

HTTP is a **stateless protocol**.

Each request is treated as a completely new request.

Example:

```text
POST /login

↓

Server responds

↓

Server forgets
```

Later:

```text
GET /profile

↓

Server has no memory
```

---

# Why Sessions Exist

Without sessions, users would need to enter their password for every request.

Sessions allow the server to remember authenticated users.

---

# What is a Session?

A session is a **server-side mechanism** that keeps track of a logged-in user across multiple HTTP requests.

The server remembers the user by using a **Session ID**.

---

# Session Flow

```text
User

↓

Login

↓

Password Verified

↓

Server Creates Session

↓

Generate Session ID

↓

Store Session

↓

Send Session ID

↓

Browser Stores Session ID

↓

Future Requests Include Session ID

↓

Server Identifies User
```

---

# Session ID

A Session ID is a random unique identifier.

Example:

```text
ABC123XYZ
```

It is **not** the user's password.

It does **not** contain sensitive information.

It simply identifies a session stored on the server.

---

# Where is Session Data Stored?

## Server

Stores:

| Session ID | User ID |
| ---------- | ------- |
| ABC123XYZ  | 1       |

The server controls the session.

---

## Browser

Stores only:

```text
session_id=ABC123XYZ
```

Usually inside a cookie.

---

# What is a Cookie?

A cookie is a small piece of information stored in the browser.

Authentication cookies usually contain only the Session ID.

They do **not** contain the user's password.

---

# Logout Flow

When the user logs out:

Server:

* Deletes the session.

Browser:

* Removes the session cookie.

Future requests are no longer authenticated.

---

# Sessions vs JWT

| Sessions                   | JWT                                |
| -------------------------- | ---------------------------------- |
| Server stores session data | Token contains user information    |
| Browser stores Session ID  | Browser stores JWT                 |
| Cookie commonly used       | Authorization header commonly used |
| Stateful                   | Stateless                          |
| Easier to invalidate       | Better for scalable REST APIs      |

JWT will be covered in **Day 4**.

---

# Login API

Endpoint:

```http
POST /login
```

Request:

```json
{
    "email": "sai@gmail.com",
    "password": "hello123"
}
```

Success Response:

```json
{
    "message": "Login successful.",
    "user": {
        "id": 1,
        "username": "Sai",
        "email": "sai@gmail.com"
    }
}
```

Status:

```text
200 OK
```

---

# SQL Query Used

Find user:

```sql
SELECT *
FROM users
WHERE email = ?;
```

Uses parameterized queries to prevent SQL injection.

---

# Important Flask Functions

## request.get_json()

Reads JSON sent by the client.

---

## jsonify()

Returns a JSON response.

---

# Important SQLite Functions

## fetchone()

Returns a single matching row.

Returns `None` if no record exists.

---

## connection.close()

Closes the database connection after the operation.

Always close connections when finished.

---

# Important bcrypt Functions

## bcrypt.hashpw()

Creates a secure password hash.

Used during registration.

---

## bcrypt.checkpw()

Verifies the entered password against the stored hash.

Used during login.

---

# HTTP Status Codes

| Code | Meaning      | Usage                     |
| ---- | ------------ | ------------------------- |
| 200  | OK           | Successful login          |
| 201  | Created      | Successful registration   |
| 400  | Bad Request  | Missing required fields   |
| 401  | Unauthorized | Invalid email or password |
| 409  | Conflict     | Email already exists      |

---

# Security Best Practices

* Never store plain-text passwords.
* Always hash passwords with bcrypt.
* Always verify passwords using `bcrypt.checkpw()`.
* Return generic login errors such as "Invalid email or password."
* Never reveal whether the email or password was incorrect.
* Always use parameterized SQL queries.
* Close database connections after use.
* Never return the password hash in API responses.

---

# Common Beginner Mistakes

* Comparing the entered password directly with the stored hash.
* Calling `bcrypt.hashpw()` during login instead of `bcrypt.checkpw()`.
* Returning different error messages for wrong email and wrong password.
* Forgetting to encode passwords before verification.
* Forgetting to close the database connection.
* Returning password hashes in API responses.
* Thinking HTTP remembers previous requests automatically.
* Confusing cookies with sessions.

---

# Interview Questions

### What is authentication?

Authentication is the process of verifying a user's identity.

---

### What is a login system?

A login system verifies a user's credentials and authenticates them.

---

### Why is `bcrypt.checkpw()` used during login?

Because it securely compares the entered password with the stored bcrypt hash.

---

### What does HTTP being stateless mean?

Each HTTP request is independent. The server does not remember previous requests by default.

---

### What is a session?

A session is a server-side mechanism used to remember authenticated users across multiple requests.

---

### What is stored in the browser?

Usually only the Session ID inside a cookie.

---

### What is stored on the server?

The session information, such as the Session ID and the associated User ID.

---

### Why do websites use sessions?

To avoid asking users to log in again for every request.

---

### Why do modern REST APIs prefer JWT?

JWTs are stateless, making them easier to scale across multiple servers.

---

# Summary

Today I learned:

* Login Fundamentals
* Password Verification
* `bcrypt.checkpw()`
* Login Validation
* HTTP Statelessness
* Sessions
* Cookies
* Session IDs
* Login API using Flask
* Secure Authentication Flow

---

# Day 3 Completion Checklist

✅ Understand the difference between registration and login.

✅ Explain why `bcrypt.checkpw()` is required.

✅ Build a working `/login` endpoint.

✅ Validate login input.

✅ Return appropriate HTTP status codes.

✅ Understand why HTTP is stateless.

✅ Explain sessions and cookies.

✅ Compare Sessions and JWT.

✅ Build a complete authentication system with:

* `POST /register`
* `POST /login`

---

# Next Day Preview

## 🟣 Phase 5 — Day 4: JWT Authentication

Topics:

* What is JWT?
* JWT Structure
* Header, Payload, Signature
* Token Generation
* Token Verification
* Authorization Header
* Building JWT Authentication in Flask
* Protecting API Endpoints using JWT
