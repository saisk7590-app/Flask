import sqlite3


def display_students(query, params=()):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(query, params)
    students = cursor.fetchall()

    print("=" * 70)

    if students:
        for student in students:
            print(
                f"ID: {student[0]:<3} | "
                f"Name: {student[1]:<10} | "
                f"Age: {student[2]:<2} | "
                f"Course: {student[3]}"
            )
    else:
        print("No students found.")

    print("=" * 70)

    connection.close()


print("\n" + "=" * 70)
print("               STUDENT SEARCH SYSTEM")
print("=" * 70)

print("\n📋 All Students")
display_students("""
SELECT *
FROM students
""")

print("\n🔍 Student with ID = 3")
display_students("""
SELECT *
FROM students
WHERE id = ?
""", (3,))

print("\n🔍 Student Named Rahul")
display_students("""
SELECT *
FROM students
WHERE name = ?
""", ("Rahul",))

print("\n📊 Students Sorted by Age (Descending)")
display_students("""
SELECT *
FROM students
ORDER BY age DESC
""")

print("\n📊 Students Sorted by Name (Descending)")
display_students("""
SELECT *
FROM students
ORDER BY name DESC
""")