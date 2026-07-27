from flask import Flask, request

from database import add_student, initialize_database
from validators.student_validator import validate_student

app = Flask(__name__)

initialize_database()


@app.route("/")
def home():
    return {
        "message": "Student Validation API"
    }


@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    errors = validate_student(data)

    if errors:
        return {
            "success": False,
            "errors": errors
        }, 400

    add_student(
        data["name"],
        data["age"],
        data["course"]
    )

    return {
        "success": True,
        "message": "Student added successfully."
    }, 201


if __name__ == "__main__":
    app.run(debug=True)