from flask import Flask, jsonify

app = Flask(__name__)

students = {
    1001: {
        "name": "Sai",
        "course": "BDS",
        "device": "iPad Air 5"
    },
    1002: {
        "name": "John",
        "course": "BDS",
        "device": "iPad 10th Gen"
    },
    1003: {
        "name": "Alex",
        "course": "MDS",
        "device": "iPad Pro 11"
    }
}

@app.route("/student/<int:student_id>")
def get_student(student_id):
    student = students.get(student_id)

    if student:
        return jsonify(student)

    return jsonify({
        "error": "Student Not Found"
    })

app.run(debug=True)