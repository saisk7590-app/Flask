from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = "students.db"


# =====================================================
# Database Helper
# =====================================================
def get_connection():
    """Create and return a SQLite database connection."""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


# =====================================================
# Home Route
# =====================================================
@app.route("/")
def home():
    """Check whether the API is running."""
    return "Student API is running!"


# =====================================================
# GET - All Students
# =====================================================
@app.route("/students", methods=["GET"])
def get_students():
    """Return all students."""

    connection = get_connection()
    cursor = connection.cursor()

    select_query = """
    SELECT *
    FROM students
    ORDER BY id
    """

    cursor.execute(select_query)
    students = cursor.fetchall()

    connection.close()

    return jsonify([dict(student) for student in students]), 200


# =====================================================
# GET - Student by ID
# =====================================================
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    """Return one student by ID."""

    connection = get_connection()
    cursor = connection.cursor()

    select_query = """
    SELECT *
    FROM students
    WHERE id = ?
    """

    cursor.execute(select_query, (student_id,))
    student = cursor.fetchone()

    connection.close()

    if student is None:
        return jsonify({
            "message": "Student not found."
        }), 404

    return jsonify(dict(student)), 200


# =====================================================
# POST - Add Student
# =====================================================
@app.route("/students", methods=["POST"])
def add_student():
    """Add a new student."""

    data = request.get_json()

    # Basic Validation
    if not data:
        return jsonify({
            "message": "Request body is required."
        }), 400

    required_fields = ["name", "age", "course"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required."
            }), 400

    name = data["name"]
    age = data["age"]
    course = data["course"]

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO students (name, age, course)
    VALUES (?, ?, ?)
    """

    cursor.execute(insert_query, (name, age, course))

    connection.commit()

    new_student_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "Student added successfully.",
        "student": {
            "id": new_student_id,
            "name": name,
            "age": age,
            "course": course
        }
    }), 201


# =====================================================
# PUT - Update Student
# =====================================================
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """Update an existing student."""

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required."
        }), 400

    required_fields = ["name", "age", "course"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required."
            }), 400

    name = data["name"]
    age = data["age"]
    course = data["course"]

    connection = get_connection()
    cursor = connection.cursor()

    update_query = """
    UPDATE students
    SET
        name = ?,
        age = ?,
        course = ?
    WHERE id = ?
    """

    cursor.execute(
        update_query,
        (name, age, course, student_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        return jsonify({
            "message": "Student not found."
        }), 404

    connection.close()

    return jsonify({
        "message": "Student updated successfully.",
        "student": {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }
    }), 200


# =====================================================
# DELETE - Delete Student
# =====================================================
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """Delete a student."""

    connection = get_connection()
    cursor = connection.cursor()

    delete_query = """
    DELETE FROM students
    WHERE id = ?
    """

    cursor.execute(delete_query, (student_id,))

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        return jsonify({
            "message": "Student not found."
        }), 404

    connection.close()

    return jsonify({
        "message": f"Student {student_id} deleted successfully."
    }), 200


# =====================================================
# Run Application
# =====================================================
if __name__ == "__main__":
    app.run(debug=True)