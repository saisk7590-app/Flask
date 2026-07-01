from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Flask",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Learn REST APIs",
        "status": "Completed"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Task REST API",
        "phase": "Phase 3 - Day 1",
        "topic": "REST API Fundamentals"
    })


# GET Collection Resource
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


# GET Single Resource
@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):

    for task in tasks:
        if task["id"] == id:
            return jsonify(task)

    return jsonify({
        "message": "Task Not Found"
    }),404


# POST Resource (Placeholder)
@app.route("/tasks", methods=["POST"])
def create_task():
    return jsonify({
        "message": "POST /tasks",
        "info": "Implementation will be covered in Phase 3 - Day 2 (CRUD)."
    })


# PUT Resource (Placeholder)
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    return jsonify({
        "message": f"PUT /tasks/{id}",
        "info": "Implementation will be covered in Phase 3 - Day 2 (CRUD)."
    })


# DELETE Resource (Placeholder)
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    return jsonify({
        "message": f"DELETE /tasks/{id}",
        "info": "Implementation will be covered in Phase 3 - Day 2 (CRUD)."
    })


app.run(debug=True)