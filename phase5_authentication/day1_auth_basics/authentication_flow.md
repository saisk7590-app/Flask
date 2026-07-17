# 🔐 Authentication Flow Diagrams

---

# 1. Registration Flow

```text
                User
                  │
                  ▼
      Enter Username
                  │
                  ▼
         Enter Email
                  │
                  ▼
       Enter Password
                  │
                  ▼
      POST /register
                  │
                  ▼
         Flask Server
                  │
                  ▼
      Validate Input
                  │
                  ▼
   Email Already Exists?
          │           │
        Yes           No
         │             │
         ▼             ▼
 Return Error     Save User
                       │
                       ▼
         Registration Successful
```

---

# 2. Login Flow

```text
                User
                  │
                  ▼
         Enter Email
                  │
                  ▼
       Enter Password
                  │
                  ▼
         POST /login
                  │
                  ▼
         Flask Server
                  │
                  ▼
        Find User in DB
                  │
                  ▼
      User Found?
          │            │
         No           Yes
         │             │
         ▼             ▼
   Return Error   Verify Password
                        │
                        ▼
              Password Correct?
                  │          │
                 No         Yes
                 │           │
                 ▼           ▼
          Invalid Login  Login Success
                              │
                              ▼
                      Generate JWT
                              │
                              ▼
                 Access Protected APIs
```

---

# 3. Authentication Lifecycle

```text
Register
    │
    ▼
Database Stores User
    │
    ▼
Login
    │
    ▼
Authentication
    │
    ▼
JWT Token Generated
    │
    ▼
Future Requests
    │
    ▼
Token Verified
    │
    ▼
Protected Resources
```

---

# 4. Client–Server Authentication Flow

```text
+----------------------+
|       Client         |
| Browser / Mobile App |
+----------+-----------+
           |
           | POST /login
           |
           ▼
+----------------------+
|    Flask Server      |
+----------+-----------+
           |
           | Query User
           |
           ▼
+----------------------+
|      SQLite DB       |
+----------+-----------+
           |
           | User Data
           |
           ▼
+----------------------+
| Password Verification|
+----------+-----------+
           |
      +----+----+
      |         |
      |         |
    Valid     Invalid
      |         |
      ▼         ▼
 Generate JWT  Error
      |
      ▼
Protected API Access
```

---

# 5. Authentication vs Authorization

```text
User
 │
 ▼
Enter Credentials
 │
 ▼
Authentication
(Who are you?)
 │
 ▼
Identity Verified
 │
 ▼
Authorization
(What can you do?)
 │
 ▼
Allowed Resources
```

---

# 6. User Login Journey

```text
User Opens App
      │
      ▼
Login Screen
      │
      ▼
Enter Email & Password
      │
      ▼
Server Verification
      │
      ▼
Credentials Valid?
   │            │
  No           Yes
   │            │
   ▼            ▼
Show Error   Login Success
                 │
                 ▼
            Receive JWT
                 │
                 ▼
      Access Protected Routes
```

---

# Key Points

- Authentication verifies identity.
- Authorization verifies permissions.
- Registration creates a new user.
- Login verifies an existing user.
- JWT is generated after successful login (covered on Day 4).
- Passwords should never be stored as plain text.
- The backend is responsible for validating every login request.