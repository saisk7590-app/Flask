from flask import Flask, jsonify, request

app = Flask(__name__)


# ==========================
# 200 OK
# ==========================
@app.route("/success")
def success():

    return jsonify({
        "success": True,
        "message": "Request Successful"
    }), 200


# ==========================
# 201 Created
# ==========================
@app.route("/created", methods=["POST"])
def created():

    return jsonify({
        "success": True,
        "message": "Resource Created Successfully"
    }), 201


# ==========================
# 400 Bad Request
# ==========================
@app.route("/bad-request", methods=["POST"])
def bad_request():

    data = request.json

    if not data:
        return jsonify({
            "success": False,
            "message": "Request Body Required"
        }), 400

    if "name" not in data:
        return jsonify({
            "success": False,
            "message": "Name is Required"
        }), 400

    return jsonify({
        "success": True,
        "message": "Valid Request",
        "data": data
    }), 200


# ==========================
# 404 Not Found
# ==========================
students = [
    {
        "id": 1,
        "name": "Sai"
    },
    {
        "id": 2,
        "name": "John"
    }
]

@app.route("/students/<int:id>")
def get_student(id):

    for student in students:

        if student["id"] == id:
            return jsonify({
                "success": True,
                "data": student
            }), 200

    return jsonify({
        "success": False,
        "message": "Student Not Found"
    }), 404


# ==========================
# 500 Internal Server Error
# ==========================
@app.route("/server-error")
def server_error():

    # Intentional error for learning
    result = 10 / 0

    return jsonify({
        "result": result
    })


app.run(debug=True)