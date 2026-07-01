# Day 4 — GET & POST Requests

## Goal

Learn how Flask receives input from clients using GET and POST requests.

---

## GET Request

GET is used to retrieve data.

Example:

```
/search?name=sai
```

Read data using:

```python
request.args.get("name")
```

Example:

```python
@app.route("/search")
def search():
    name = request.args.get("name")

    return jsonify({
        "search": name
    })
```

---

## POST Request

POST is used to send data to the server.

Example JSON:

```json
{
    "username": "sai",
    "password": "1234"
}
```

Read JSON using:

```python
data = request.json
```

---

## Reading Values

```python
username = data.get("username")
password = data.get("password")
```

Using `.get()` avoids errors if the key is missing.

---

## POST Route

```python
@app.route("/login", methods=["POST"])
```

Only POST requests are allowed.

---

## Login Example

```python
@app.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "1234":
        return jsonify({
            "message": "Login Successful"
        })

    return jsonify({
        "message": "Invalid Credentials"
    })
```

---

## GET vs POST

GET

- Used to retrieve data
- Data comes from URL
- Read with:

```python
request.args.get()
```

POST

- Used to send data
- Data comes from request body
- Read with:

```python
request.json
```

---

## Backend Flow

### GET

```
Browser
↓
URL
↓
request.args
↓
Function
↓
JSON Response
```

### POST

```
Client
↓
JSON Body
↓
request.json
↓
Function
↓
JSON Response
```

---

## Common Mistakes

### Wrong

```python
request.json
```

inside a GET request.

### Correct

```python
request.args.get("name")
```

---

### Wrong

```python
data["username"]
```

### Better

```python
data.get("username")
```

---

### Wrong

```python
@app.route("/login")
```

### Correct

```python
@app.route("/login", methods=["POST"])
```

---

## Important Syntax

Import:

```python
from flask import request, jsonify
```

GET:

```python
request.args.get("name")
```

POST:

```python
data = request.json
```

Read value:

```python
username = data.get("username")
```

---

## Day 4 Summary

GET

```python
request.args.get()
```

POST

```python
request.json
```

Most login, registration, and form APIs use POST requests.

Status: ✅ Day 4 Complete