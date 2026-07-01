from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary Database (Python List)
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


# Home Route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Task Manager REST API",
        "phase": "Phase 3 - Day 2",
        "topic": "CRUD Operations"
    })


# ==========================
# GET - All Tasks
# ==========================


# ==========================
# GET - Single Task
# ==========================
@app.route("/tasks", methods=["GET"])
def get_tasks():

    status = request.args.get("status")

    # If no query parameter is provided,
    # return all tasks.
    if status is None:
        return jsonify(tasks)

    filtered_tasks = []

    for task in tasks:
        if task["status"].lower() == status.lower():
            filtered_tasks.append(task)

    return jsonify(filtered_tasks)


# ==========================
# POST - Create Task
# ==========================
@app.route("/tasks", methods=["POST"])
def create_task():

    data = request.json

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "status": data["status"]
    }

    tasks.append(new_task)

    return jsonify({
        "message": "Task Created Successfully",
        "task": new_task
    })


# ==========================
# PUT - Update Task
# ==========================
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.json

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = data["title"]
            task["status"] = data["status"]

            return jsonify({
                "message": "Task Updated Successfully",
                "task": task
            })

    return jsonify({
        "message": "Task Not Found"
    }), 404


# ==========================
# DELETE - Delete Task
# ==========================
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return jsonify({
                "message": "Task Deleted Successfully",
                "deleted_task": task
            })

    return jsonify({
        "message": "Task Not Found"
    }), 404


app.run(debug=True)