# 🟣 Phase 5 - Day 1: Authentication Fundamentals

## 🎯 Day Goal

Understand:

- Authentication
- Authorization
- Login Flow
- Registration Flow
- Why passwords should never be stored as plain text
- How authentication works in backend applications

---

# What is Authentication?

## Definition

Authentication is the process of verifying the identity of a user.

It answers the question:

> **"Who are you?"**

A user proves their identity by providing credentials such as:

- Username
- Email
- Password
- OTP
- Fingerprint
- Face ID

If the credentials are correct, the user is authenticated.

---

# Real World Examples

## Gmail

- Enter Email
- Enter Password
- Google verifies the credentials
- Login Successful

---

## Instagram

- Username
- Password
- Server verifies user
- Access granted

---

## ATM Machine

Authentication methods:

- ATM Card
- PIN

Only after verification can the customer access the account.

---

# What is Authorization?

## Definition

Authorization determines what an authenticated user is allowed to do.

It answers the question:

> **"What are you allowed to do?"**

Authorization happens only after successful authentication.

---

# Authentication vs Authorization

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Verifies permissions |
| Who are you? | What can you do? |
| Happens first | Happens after authentication |
| Login process | Access control |

---

# Login vs Authentication

Login is the action performed by the user.

Authentication is the verification process performed by the server.

Example:

User enters:

- Email
- Password

↓

Server verifies credentials

↓

Authentication successful

↓

User logged in

---

# Registration

Registration means creating a new account.

User provides:

- Username
- Email
- Password

The server checks:

- Required fields
- Duplicate email
- Valid input

If everything is correct:

The new user account is stored in the database.

---

# Login Process

User enters:

- Email
- Password

↓

Server receives POST request

↓

Server searches for user

↓

Password is verified

↓

If correct:

Login successful

Else:

Invalid credentials

---

# Why Passwords Should Never Be Stored as Plain Text

Wrong:

| Username | Password |
|----------|----------|
| Sai | hello123 |

If the database is stolen:

Anyone can read every password.

Correct approach:

Store only a hashed password.

Example:

hello123

↓

$2b$12$X5........

Hashing protects user passwords even if the database is compromised.

---

# Authentication Lifecycle

Register

↓

Store user

↓

Login

↓

Authentication

↓

Generate Token (JWT)

↓

Access Protected APIs

---

# User Credentials

Common credentials include:

- Username
- Email
- Password

---

# Backend Responsibilities

The backend must:

- Verify user credentials
- Never trust the client
- Validate every login request
- Protect user information

---

# Best Practices

✔ Never store plain passwords

✔ Always validate user input

✔ Use unique email addresses

✔ Return generic login errors

✔ Authenticate before authorization

✔ Use secure authentication methods

---

# Common Beginner Mistakes

❌ Confusing authentication with authorization

❌ Storing plain passwords

❌ Trusting frontend validation

❌ Giving detailed login errors

❌ Forgetting permission checks

---

# Industry Use Cases

Google

- Authentication: Google Account login
- Authorization: Gmail, Drive, Admin access

Amazon

- Customer login
- Seller login
- Admin login

All authenticate first.

Permissions differ.

---

# Interview Questions

### What is authentication?

Authentication is the process of verifying the identity of a user.

---

### What is authorization?

Authorization determines what actions an authenticated user can perform.

---

### Which comes first?

Authentication

↓

Authorization

---

### Why should passwords never be stored as plain text?

Because if the database is compromised, attackers can immediately read every password.

---

### What is the difference between login and authentication?

Login is the user's action.

Authentication is the server's verification process.

---

# Summary

Today I learned:

- Authentication
- Authorization
- Registration Flow
- Login Flow
- Authentication Lifecycle
- Password Security Basics
- Backend Authentication Responsibilities

Tomorrow:

➡ Password Hashing using bcrypt.