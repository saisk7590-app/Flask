# Day 5 — Build Complete Task API

## Goal

Combine all Flask concepts learned so far to build a simple REST-style API.

---

## Data Storage

Instead of a database, we use a Python list.

Example:

```python
students = []
```

The data is stored temporarily in memory.

---

## GET Request

Used to retrieve all data.

Example:

```python
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)
```

---

## POST Request

Used to add new data.

Example:

```python
@app.route("/students", methods=["POST"])
def add_student():

    data = request.json

    students.append(data)

    return jsonify({
        "message": "Student Added Successfully"
    })
```

---

## DELETE Request

Used to remove data.

Example:

```python
@app.route("/students/<int:index>", methods=["DELETE"])
def delete_student(index):

    if 0 <= index < len(students):

        deleted_student = students.pop(index)

        return jsonify({
            "message": "Student Deleted Successfully",
            "deleted_student": deleted_student
        })

    return jsonify({
        "error": "Student Not Found"
    })
```

---

## Methods Learned

GET

- Retrieve data

POST

- Add new data

DELETE

- Remove data

---

## Backend Flow

### GET

Client

↓

GET /students

↓

Return List

↓

JSON Response

---

### POST

Client

↓

POST /students

↓

request.json

↓

students.append()

↓

JSON Response

---

### DELETE

Client

↓

DELETE /students/0

↓

students.pop(0)

↓

JSON Response

---

## Important Functions

Read JSON:

```python
request.json
```

Return JSON:

```python
jsonify(...)
```

Add Item:

```python
students.append(data)
```

Delete Item:

```python
students.pop(index)
```

---

## Common Mistakes

### Forgetting POST method

Wrong:

```python
@app.route("/students")
```

Correct:

```python
@app.route("/students", methods=["POST"])
```

---

### Forgetting Bounds Check

Wrong:

```python
students.pop(index)
```

Correct:

```python
if 0 <= index < len(students):
```

---

### Forgetting request.json

Wrong:

```python
students.append("Sai")
```

Correct:

```python
data = request.json
students.append(data)
```

---

## Phase 2 Summary

Topics Mastered:

- Flask Installation
- Flask Application Structure
- Routes
- Dynamic Routes
- JSON Responses
- GET Requests
- POST Requests
- DELETE Requests
- Request Handling
- Building Simple APIs

Status: ✅ Phase 2 Complete