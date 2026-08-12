from flask import Flask, jsonify, request

from database import get_connection


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Student API is running"
    })


@app.route("/students", methods=["GET"])
def get_students():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, email, age, course FROM students"
    )

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    students = []

    for row in rows:
        student = {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "age": row[3],
            "course": row[4]
        }

        students.append(student)

    return jsonify(students)


@app.route("/students", methods=["POST"])
def create_student():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    course = data.get("course")

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students (name, email, age, course)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """,
        (name, email, age, course)
    )

    student_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Student created successfully",
        "student_id": student_id
    }), 201


if __name__ == "__main__":
    app.run(debug=True)