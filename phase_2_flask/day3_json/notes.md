# Day 3 — JSON Responses

## Goal

Learn how to return structured JSON data from Flask APIs.

---

## What is JSON?

JSON stands for:

JavaScript Object Notation

JSON is used to exchange data between:

Frontend ↔ Backend

---

## Plain Text vs JSON

Plain Text:

```python
return "Hello"
```

Output:

```text
Hello
```

JSON:

```python
return jsonify({
    "message": "Hello"
})
```

Output:

```json
{
    "message": "Hello"
}
```

JSON is easier for applications to process.

---

## Import jsonify

```python
from flask import Flask, jsonify
```

---

## Basic JSON Response

```python
@app.route("/student")
def student():
    return jsonify({
        "name": "Sai",
        "course": "Python"
    })
```

Output:

```json
{
    "name": "Sai",
    "course": "Python"
}
```

---

## JSON Structure

```json
{
    "key": "value"
}
```

Example:

```json
{
    "name": "Sai",
    "age": 22
}
```

---

## JSON Data Types

String:

```python
"name": "Sai"
```

Number:

```python
"age": 22
```

Boolean:

```python
"is_student": True
```

List:

```python
"skills": ["Python", "Flask"]
```

Nested Object:

```python
{
    "student": {
        "name": "Sai"
    }
}
```

---

## Dynamic JSON Response

```python
students = {
    1001: {
        "name": "Sai"
    }
}

@app.route("/student/<int:student_id>")
def get_student(student_id):
    student = students.get(student_id)

    if student:
        return jsonify(student)

    return jsonify({
        "error": "Student Not Found"
    })
```

---

## Route Type Converter

```python
@app.route("/student/<int:student_id>")
```

Only accepts integer values.

Examples:

Valid:

```text
/student/1001
/student/1002
```

Invalid:

```text
/student/sai
```

---

## Dictionary Lookup

```python
student = students.get(student_id)
```

Returns:

```python
None
```

if the key is not found.

Safer than:

```python
students[student_id]
```

which can crash.

---

## Error JSON

```python
return jsonify({
    "error": "Student Not Found"
})
```

Example Output:

```json
{
    "error": "Student Not Found"
}
```

---

## Backend Flow

Request
↓
Route
↓
Function
↓
Data Lookup
↓
jsonify()
↓
JSON Response

---

## Common Mistakes

### Forgetting jsonify

Wrong:

```python
return "Student Found"
```

Correct:

```python
return jsonify({
    "message": "Student Found"
})
```

### Missing Colon

Wrong:

```python
{
    "name" = "Sai"
}
```

Correct:

```python
{
    "name": "Sai"
}
```

### Missing Comma

Wrong:

```python
{
    "id": 1
    "name": "Sai"
}
```

Correct:

```python
{
    "id": 1,
    "name": "Sai"
}
```

---

## Important Syntax

Import:

```python
from flask import jsonify
```

Return JSON:

```python
return jsonify({
    "name": "Sai"
})
```

Dynamic Route:

```python
@app.route("/student/<int:student_id>")
```

Dictionary Lookup:

```python
students.get(student_id)
```

---

## Day 3 Summary

Plain Text:

```python
return "Hello"
```

JSON:

```python
return jsonify({
    "message": "Hello"
})
```

Most APIs return JSON responses.

Status: ✅ Day 3 Complete
