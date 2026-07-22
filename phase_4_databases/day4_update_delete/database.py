import sqlite3

# -----------------------------
# Connect to Database
# -----------------------------
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# -----------------------------
# Create Table
# -----------------------------
with open("schema.sql", "r") as file:
    cursor.executescript(file.read())

# -----------------------------
# Clear Existing Data
# -----------------------------
cursor.execute("DELETE FROM students")

# -----------------------------
# Sample Data
# -----------------------------
students = [
    ("Sai", 21, "Python"),
    ("Rahul", 20, "Flutter"),
    ("Anjali", 22, "Java"),
    ("Vikram", 19, "C++"),
    ("Priya", 22, "Data Science")
]

# -----------------------------
# Insert Query
# -----------------------------
insert_query = """
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
"""

# -----------------------------
# Insert Sample Data
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

print("✅ Database initialized successfully!")