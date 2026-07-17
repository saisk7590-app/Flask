# 🟣 Phase 5 - Day 2: Password Hashing (bcrypt)

## 🎯 Day Goal

Learn how to securely store user passwords by understanding:

* Hashing
* Salt
* bcrypt
* Password Verification
* Secure User Registration
* Flask + SQLite + bcrypt Integration

---

# What is Hashing?

## Definition

Hashing is the process of converting data into a fixed-length value called a **hash** using a mathematical algorithm.

A hash function takes an input and produces an output that cannot practically be reversed.

```
Password
    │
    ▼
Hash Function
    │
    ▼
Hash Value
```

Example:

```
hello123

↓

$2b$12$eImiTXuWVxfM37uY4JANjQ...
```

---

# Why Do We Hash Passwords?

Passwords should never be stored in plain text.

Bad Example:

| Username | Password |
| -------- | -------- |
| Sai      | hello123 |

If a hacker steals the database, they immediately know every user's password.

Correct Approach:

Store only the hashed password.

| Username | Password                         |
| -------- | -------------------------------- |
| Sai      | $2b$12$eImiTXuWVxfM37uY4JANjQ... |

---

# One-Way Function

Hashing is a **one-way process**.

```
Password
    │
    ▼
Hash
```

Possible ✔

```
Hash
    │
    ▼
Password
```

Not practically possible ✖

Because of this property, hashing is ideal for password storage.

---

# Hashing vs Encryption

| Hashing                          | Encryption                                |
| -------------------------------- | ----------------------------------------- |
| One-way                          | Two-way                                   |
| Cannot recover original password | Original data can be recovered with a key |
| Used for passwords               | Used for confidential data                |
| No decryption key                | Requires a decryption key                 |

---

# What is a Hash?

A hash is the output produced by a hash function.

Example:

```
Password

↓

hello123

↓

Hash

↓

$2b$12$abcXYZ...
```

The hash is stored in the database instead of the original password.

---

# Small Input Change

Even a one-character difference creates a completely different hash.

```
hello123

↓

Hash A
```

```
Hello123

↓

Hash B
```

This property improves security.

---

# What is a Collision?

A collision occurs when two different inputs produce the same hash.

```
Password A

↓

Hash XYZ
```

```
Password B

↓

Hash XYZ
```

Good hashing algorithms make collisions extremely rare.

---

# Rainbow Table Attack

Hackers maintain databases of common passwords and their hashes.

Example:

```
password

↓

5f4dcc...
```

```
123456

↓

e10adc...
```

```
hello123

↓

ABC123XYZ
```

If your database stores simple hashes, attackers can compare them against these precomputed values and discover passwords quickly.

---

# What is Salt?

A salt is a random value added to the password before hashing.

Purpose:

* Makes identical passwords generate different hashes.
* Prevents rainbow table attacks.
* Makes password cracking much more difficult.

Without Salt:

```
hello123

↓

ABC123XYZ
```

```
hello123

↓

ABC123XYZ
```

Same password → Same hash.

With Salt:

```
A1X9 + hello123

↓

Hash A
```

```
Q7P2 + hello123

↓

Hash B
```

Same password → Different hashes.

---

# Where is the Salt Stored?

With bcrypt, the salt is stored inside the hash itself.

Example:

```
$2b$12$W8f2K9...
```

This string contains:

* Algorithm information
* Cost factor
* Salt
* Password hash

bcrypt automatically extracts the salt during verification.

---

# What is bcrypt?

bcrypt is a password hashing library designed specifically for securely storing passwords.

It automatically:

* Generates a random salt
* Combines the password and salt
* Hashes the password
* Stores the salt within the hash

---

# Why Use bcrypt?

bcrypt is intentionally slow.

A slow algorithm makes brute-force attacks much more difficult because each password guess takes time.

Advantages:

* Automatic salt generation
* Strong security
* Widely used
* Easy verification
* Resistant to rainbow table attacks

---

# bcrypt Functions

## Generate Salt

```python
bcrypt.gensalt()
```

Creates a new random salt.

---

## Hash Password

```python
bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)
```

Returns a secure hashed password.

---

## Verify Password

```python
bcrypt.checkpw(
    entered_password.encode("utf-8"),
    stored_hash.encode("utf-8")
)
```

Returns:

* True → Password is correct
* False → Password is incorrect

---

# Why Do We Use .encode()?

Python strings must be converted into bytes before bcrypt can process them.

Example:

```python
password.encode("utf-8")
```

```
"hello123"

↓

b"hello123"
```

---

# Why Do We Use .decode()?

bcrypt returns bytes.

SQLite stores text more naturally.

Example:

```python
hashed_password.decode("utf-8")
```

```
b"$2b$12$..."

↓

"$2b$12$..."
```

---

# Registration Flow

```
User

↓

Enter Username

↓

Enter Email

↓

Enter Password

↓

Validate Input

↓

Email Exists?

↓

No

↓

Hash Password

↓

Store User

↓

Registration Successful
```

---

# Login Flow

```
User

↓

Enter Email

↓

Enter Password

↓

Find User

↓

Retrieve Stored Hash

↓

bcrypt.checkpw()

↓

Password Correct?

↓

Yes

↓

Login Successful
```

---

# Database Schema

```
users

-----------------------------------

id

username

email

password
```

The password column stores only the hashed password.

---

# Flask Registration API

Endpoint:

```
POST /register
```

JSON Request:

```json
{
    "username": "Sai",
    "email": "sai@gmail.com",
    "password": "hello123"
}
```

Success Response:

```json
{
    "message": "User registered successfully."
}
```

HTTP Status:

```
201 Created
```

---

# SQL Used

Check if email exists:

```sql
SELECT id
FROM users
WHERE email = ?;
```

Insert user:

```sql
INSERT INTO users
(
    username,
    email,
    password
)
VALUES
(
    ?,
    ?,
    ?
);
```

Parameterized queries prevent SQL Injection.

---

# Important Python Functions

## encode()

Converts a string to bytes.

```python
password.encode("utf-8")
```

---

## decode()

Converts bytes to a string.

```python
hashed.decode("utf-8")
```

---

## bcrypt.hashpw()

Hashes a password.

---

## bcrypt.gensalt()

Generates a random salt.

---

## bcrypt.checkpw()

Verifies an entered password against the stored hash.

---

# Best Practices

* Never store plain-text passwords.
* Always hash passwords before saving them.
* Use bcrypt, Argon2, or scrypt for password hashing.
* Let bcrypt generate salts automatically.
* Use parameterized SQL queries.
* Validate all user input.
* Keep email addresses unique.
* Store only the hashed password.

---

# Common Beginner Mistakes

* Storing plain passwords.
* Forgetting to encode passwords before hashing.
* Forgetting to decode hashes before storing them.
* Trying to decrypt a bcrypt hash.
* Using MD5 or SHA-1 for password storage.
* Generating a new salt during password verification.
* Building SQL queries using string concatenation.

---

# Industry Use Cases

Companies that securely store passwords use dedicated password hashing algorithms such as bcrypt, Argon2, or scrypt.

Examples include:

* Google
* Microsoft
* GitHub
* Amazon
* Netflix
* Banking Applications

---

# Interview Questions

### What is hashing?

Hashing is the process of converting data into a one-way fixed-format value called a hash.

---

### Why should passwords be hashed?

To prevent attackers from reading user passwords if the database is compromised.

---

### What is a salt?

A random value added to the password before hashing to ensure identical passwords produce different hashes.

---

### Why is bcrypt preferred?

Because it automatically uses salts, is intentionally slow, and is designed specifically for password storage.

---

### Why do we use `.encode()`?

bcrypt works with bytes instead of Python strings.

---

### What does `bcrypt.checkpw()` do?

It compares an entered password with the stored bcrypt hash and returns `True` if they match.

---

### Why is the email field UNIQUE?

To prevent multiple accounts from being created with the same email address.

---

# Summary

Today I learned:

* Hashing
* One-way functions
* Hashing vs Encryption
* Rainbow Tables
* Salt
* bcrypt
* Password Verification
* Secure Password Storage
* Flask + SQLite + bcrypt Integration
* Secure Registration API

Tomorrow:

➡ **Day 3 – Login System + Password Verification + Sessions**

After reviewing these notes a few times, you should be able to explain password hashing confidently in interviews and implement a secure registration system from scratch.
