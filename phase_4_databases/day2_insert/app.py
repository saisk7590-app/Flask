import sqlite3

# -----------------------------
# Connect to Database
# -----------------------------
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# -----------------------------
# SQL Query
# -----------------------------
select_query = """
SELECT *
FROM students
"""

# -----------------------------
# Execute Query
# -----------------------------
cursor.execute(select_query)

# -----------------------------
# Fetch All Records
# -----------------------------
students = cursor.fetchall()

# -----------------------------
# Display Students
# -----------------------------
print("=" * 55)
print("        STUDENT DATABASE")
print("=" * 55)

if students:
    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Age: {student[2]} | "
            f"Course: {student[3]}"
        )
else:
    print("No students found.")

print("=" * 55)

# -----------------------------
# Close Connection
# -----------------------------
connection.close()