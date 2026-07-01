from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {
        "student_id": 1001,
        "name": "Sai",
        "course": "BDS",
        "device": "iPad Air 5"
    },
    {
        "student_id": 1002,
        "name": "John",
        "course": "BDS",
        "device": "iPad 10th Gen"
    },
    {
        "student_id": 1003,
        "name": "Alex",
        "course": "MDS",
        "device": "iPad Pro 11"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Student Device Management API"
    })


# GET - View all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# POST - Add new student
@app.route("/students", methods=["POST"])
def add_student():

    data = request.json

    students.append(data)

    return jsonify({
        "message": "Student Added Successfully",
        "students": students
    })


# DELETE - Delete student using list index
@app.route("/students/<int:index>", methods=["DELETE"])
def delete_student(index):

    if index < len(students):

        deleted_student = students.pop(index)

        return jsonify({
            "message": "Student Deleted Successfully",
            "deleted_student": deleted_student
        })

    return jsonify({
        "error": "Student Not Found"
    })


app.run(debug=True)