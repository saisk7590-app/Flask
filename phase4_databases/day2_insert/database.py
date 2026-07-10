import sqlite3

# -----------------------------
# Connect to SQLite Database
# -----------------------------
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# -----------------------------
# Create students table if it doesn't exist
# -----------------------------
with open("schema.sql", "r") as file:
    cursor.executescript(file.read())

# -----------------------------
# SQL Query
# -----------------------------
insert_query = """
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
"""

# -----------------------------
# Students Data
# -----------------------------
students = [
    ("Sai", 21, "Python"),
    ("Rahul", 20, "Flutter"),
    ("Anjali", 22, "Java"),
    ("Vikram", 19, "C++"),
    ("Priya", 22, "Data Science")
]

# -----------------------------
# Insert Multiple Students
# -----------------------------
cursor.executemany(insert_query, students)

# -----------------------------
# Save Changes
# -----------------------------
connection.commit()

# -----------------------------
# Close Connection
# -----------------------------
connection.close()

print("✅ Students added successfully!")