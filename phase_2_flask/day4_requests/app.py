from flask import Flask, request, jsonify

app = Flask(__name__)

students = {
    "sai": {
        "password": "1234",
        "student_id": 1001,
        "course": "BDS",
        "device": "iPad Air 5"
    },
    "john": {
        "password": "5678",
        "student_id": 1002,
        "course": "BDS",
        "device": "iPad 10th Gen"
    },
    "alex": {
        "password": "9999",
        "student_id": 1003,
        "course": "MDS",
        "device": "iPad Pro 11"
    }
}


@app.route("/")
def home():
    return jsonify({
        "message": "Dental College Login API"
    })


@app.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    student = students.get(username)

    if student and student["password"] == password:

        return jsonify({
            "message": "Login Successful",
            "student_id": student["student_id"],
            "course": student["course"],
            "device": student["device"]
        })

    return jsonify({
        "message": "Invalid Credentials"
    })


app.run(debug=True)