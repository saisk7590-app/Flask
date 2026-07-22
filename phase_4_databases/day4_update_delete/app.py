import sqlite3


# -----------------------------
# Display All Students
# -----------------------------
def display_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    select_query = """
    SELECT *
    FROM students
    ORDER BY id
    """

    cursor.execute(select_query)
    students = cursor.fetchall()

    print("=" * 70)
    print("               STUDENT MANAGEMENT SYSTEM")
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


# -----------------------------
# Add Student
# -----------------------------
def add_student(name, age, course):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO students (name, age, course)
    VALUES (?, ?, ?)
    """

    cursor.execute(insert_query, (name, age, course))

    connection.commit()

    print(f"✅ {name} added successfully.")

    connection.close()


# -----------------------------
# Update Student Age
# -----------------------------
def update_student_age(student_id, new_age):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    update_query = """
    UPDATE students
    SET age = ?
    WHERE id = ?
    """

    cursor.execute(update_query, (new_age, student_id))

    connection.commit()

    if cursor.rowcount > 0:
        print(f"✅ Student ID {student_id} age updated to {new_age}.")
    else:
        print(f"❌ Student ID {student_id} not found.")

    connection.close()


# -----------------------------
# Update Student Course
# -----------------------------
def update_student_course(student_id, new_course):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    update_query = """
    UPDATE students
    SET course = ?
    WHERE id = ?
    """

    cursor.execute(update_query, (new_course, student_id))

    connection.commit()

    if cursor.rowcount > 0:
        print(f"✅ Student ID {student_id} course updated to {new_course}.")
    else:
        print(f"❌ Student ID {student_id} not found.")

    connection.close()


# -----------------------------
# Delete Student
# -----------------------------
def delete_student(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    delete_query = """
    DELETE FROM students
    WHERE id = ?
    """

    cursor.execute(delete_query, (student_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print(f"✅ Student ID {student_id} deleted successfully.")
    else:
        print(f"❌ Student ID {student_id} not found.")

    connection.close()


# ==========================================================
#                     DEMONSTRATION
# ==========================================================

print("\n📋 Initial Database")
display_students()

print("\n➕ Adding Student")
add_student("Ramesh", 24, "Django")

print("\n📋 After Adding")
display_students()

print("\n✏️ Updating Age")
update_student_age(2, 26)

print("\n📋 After Age Update")
display_students()

print("\n✏️ Updating Course")
update_student_course(1, "Full Stack Python")

print("\n📋 After Course Update")
display_students()

print("\n🗑️ Deleting Student")
delete_student(4)

print("\n📋 Final Database")
display_students()