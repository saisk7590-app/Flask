# Day 2 — Routes & Dynamic URLs

## Goal

Learn how Flask maps URLs to functions and how to create dynamic routes using URL parameters.

---

## Routing

Routing means:

URL → Function

Example:

```python
@app.route("/")
def home():
    return "Home Page"
```

When user visits `/`, Flask runs `home()`.

---

## Static Route

Fixed URL.

Example:

```python
@app.route("/about")
def about():
    return "About Page"
```

Only works for:

/about

---

## Dynamic Route

Variable URL.

Example:

```python
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
```

Works for:

/user/sai
/user/john
/user/rahul

---

## URL Parameter

```python
@app.route("/user/<name>")
```

`<name>` captures data from the URL.

Example:

/user/sai

Flask stores:

```python
name = "sai"
```

and passes it to:

```python
def user(name):
```

---

## Examples

### User Route

```python
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
```

### Student Route

```python
@app.route("/student/<name>")
def student(name):
    return f"Student Name: {name}"
```

### Product Route

```python
@app.route("/product/<product>")
def product(product):
    return f"Product Name: {product}"
```

---

## Flow

/user/sai
↓
Route Match
↓
name = "sai"
↓
user(name)
↓
Response
↓
Browser

---

## Important Rules

Variable names must match.

Correct:

```python
@app.route("/user/<name>")
def user(name):
```

Wrong:

```python
@app.route("/user/<name>")
def user(username):
```

---

## Static vs Dynamic

Static:

```python
@app.route("/about")
```

Dynamic:

```python
@app.route("/user/<name>")
```

---

## Common Mistakes

### Forgetting < >

Wrong:

```python
@app.route("/user/name")
```

Correct:

```python
@app.route("/user/<name>")
```

### Variable mismatch

Wrong:

```python
@app.route("/user/<name>")
def user(username):
```

Correct:

```python
@app.route("/user/<name>")
def user(name):
```

---

## Day 2 Summary

Static Route:

```python
@app.route("/about")
```

Dynamic Route:

```python
@app.route("/user/<name>")
```

Example:

```python
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
```

Status: ✅ Day 2 Complete