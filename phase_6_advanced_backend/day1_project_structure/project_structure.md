# Professional Flask Project Structure

## Folder Structure

```
day1_project_structure/

│
├── app/
│
├── routes/
│   ├── __init__.py
│   └── student_routes.py
│
├── services/
│   ├── __init__.py
│   └── student_service.py
│
├── models/
│   ├── __init__.py
│   └── student.py
│
├── database/
│   └── __init__.py
│
├── utils/
│   └── __init__.py
│
├── helpers/
│   └── __init__.py
│
├── config/
│   └── __init__.py
│
├── __init__.py
│
├── main.py
│
├── requirements.txt
│
└── notes.md
```

---

# Purpose of Each Folder

## app/

Main application package.

Contains all application modules.

---

## routes/

Handles HTTP requests.

Responsibilities:

- Receive request
- Call service
- Return response

Example:

```
GET /students

POST /students
```

---

## services/

Contains business logic.

Responsibilities:

- Process data
- Perform calculations
- Communicate with the database

Example:

```
get_all_students()

add_student()

delete_student()
```

---

## models/

Represents application data.

Example:

```
Student

Expense

User
```

Later these become SQLAlchemy models.

---

## database/

Responsible for database operations.

Examples:

```
Database connection

SQLite connection

PostgreSQL connection
```

---

## config/

Stores configuration.

Examples:

```
SECRET_KEY

DATABASE_PATH

DEBUG

JWT_SECRET
```

---

## utils/

Contains reusable utility functions.

Examples:

```
format_date()

generate_uuid()

calculate_age()
```

---

## helpers/

Contains reusable helper logic.

Examples:

```
JWT Helper

Password Helper

Response Helper
```

---

# Request Flow

```
Client

↓

main.py

↓

Blueprint Route

↓

Service

↓

Database

↓

Service

↓

Blueprint Route

↓

JSON Response
```

---

# Role of main.py

Responsibilities:

- Create Flask app
- Register Blueprints
- Configure application
- Start Flask server

Example:

```
app = Flask(__name__)

app.register_blueprint(student_bp)

app.run(debug=True)
```

---

# Role of Blueprint

A Blueprint groups related routes.

Example:

```
student_routes.py

↓

GET /students

POST /students

DELETE /students
```

Advantages:

- Cleaner code
- Modular application
- Easier maintenance

---

# Role of Service Layer

Services contain business logic.

Example:

Instead of:

```
Route

↓

Connect Database

↓

Fetch Students

↓

Return Response
```

Use:

```
Route

↓

Service

↓

Return Response
```

Advantages:

- Reusable logic
- Easier testing
- Cleaner routes

---

# Architecture Diagram

```
Browser

↓

Flask Application

↓

Blueprint

↓

Service Layer

↓

Database Layer

↓

Database

↓

JSON Response
```

---

# Industry Architecture

```
Client

↓

Routes

↓

Controllers (optional)

↓

Services

↓

Models

↓

Database

↓

Response
```

This layered architecture is commonly used in professional Flask applications because it improves readability, maintainability, scalability, and collaboration among developers.