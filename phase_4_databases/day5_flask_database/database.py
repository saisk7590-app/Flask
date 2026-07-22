import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

with open("schema.sql", "r") as file:
    cursor.executescript(file.read())

cursor.execute("DELETE FROM students")

students = [
    ("Sai", 21, "Python"),
    ("Rahul", 20, "Flutter"),
    ("Anjali", 22, "Java"),
    ("Vikram", 19, "C++"),
    ("Priya", 22, "Data Science")
]

insert_query = """
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
"""

cursor.executemany(insert_query, students)

connection.commit()
connection.close()

print("✅ Database initialized successfully!")