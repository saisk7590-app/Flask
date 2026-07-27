# Phase 6 - Day 5
# MVC Architecture + Scalable Design

## Goal

Learn professional backend architecture and separate application responsibilities.

---

# MVC

MVC stands for:

- Model
- View
- Controller


## Model

Responsible for data structure.

Example:

Task:

- id
- title
- description
- status


---

## View

In Flask REST APIs:

View represents JSON responses.

Example:

```json
{
 "success":true,
 "data":[]
}
```

---

## Controller

Handles HTTP requests.

Responsibilities:

- Receive request
- Call service
- Return response


Does NOT contain:

- SQL
- Business rules


---

# Service Layer

Contains business logic.

Example:

Rules:

- Title required
- Status must be valid


---

# Repository Pattern

Repository separates database operations.

Flow:

```
Controller

↓

Service

↓

Repository

↓

Database
```


Benefits:

- Cleaner code
- Easier testing
- Database can change easily


---

# Professional Backend Structure

```
app/

controllers/

models/

routes/

services/

repositories/

database/

utils/

config/
```


---

# Request Flow

Example:

POST /tasks


```
Client

↓

Route

↓

Controller

↓

Service

↓

Repository

↓

Database
```


---

# Why MVC?

Without MVC:

- Everything in one file
- Hard maintenance
- Difficult scaling


With MVC:

- Separation of concerns
- Easier debugging
- Team friendly
- Production ready


---

# Concepts Learned

✅ MVC Architecture

✅ Application Factory Pattern

✅ Flask Blueprints

✅ Service Layer

✅ Repository Pattern

✅ Separation of Concerns

✅ Scalable Project Structure


---

# Phase 6 Completed

Day 1:
Professional Project Structure

Day 2:
Environment Variables

Day 3:
API Validation

Day 4:
Error Handling

Day 5:
MVC Architecture


---

# Next Phase

Phase 7 - Deployment & Production

Topics:

- Git workflow
- GitHub
- Render deployment
- PostgreSQL
- Production configuration
- Monitoring