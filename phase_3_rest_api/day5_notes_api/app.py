from flask import Flask, jsonify, request

app = Flask(__name__)

# ==========================================
# Temporary Database
# ==========================================
notes = [
    {
        "id": 1,
        "title": "Flask",
        "content": "Learn REST APIs",
        "created_date": "2026-07-03"
    },
    {
        "id": 2,
        "title": "Python",
        "content": "Practice every day",
        "created_date": "2026-07-04"
    }
]


# ==========================================
# Helper Functions
# ==========================================
def success_response(message, data=None, status_code=200):
    return jsonify({
        "success": True,
        "message": message,
        "data": data
    }), status_code


def error_response(message, status_code):
    return jsonify({
        "success": False,
        "message": message
    }), status_code


def validate_note(data):

    if not data:
        return "Request body is required"

    required_fields = [
        "title",
        "content",
        "created_date"
    ]

    for field in required_fields:
        if field not in data:
            return f"{field} is required"

    return None


# ==========================================
# Home Route
# ==========================================
@app.get("/")
def home():
    return success_response(
        "Notes API",
        {
            "phase": "Phase 3 - Day 5",
            "topic": "Notes API + API Organization"
        }
    )


# ==========================================
# GET All Notes
# ==========================================
@app.get("/notes")
def get_notes():

    return success_response(
        "Notes Retrieved Successfully",
        notes
    )


# ==========================================
# GET Note By ID
# ==========================================
@app.get("/notes/<int:note_id>")
def get_note(note_id):

    for note in notes:

        if note["id"] == note_id:
            return success_response(
                "Note Found",
                note
            )

    return error_response(
        "Note Not Found",
        404
    )


# ==========================================
# CREATE Note
# ==========================================
@app.post("/notes")
def create_note():

    data = request.json

    error = validate_note(data)

    if error:
        return error_response(
            error,
            400
        )

    if notes:
        new_id = max(note["id"] for note in notes) + 1
    else:
        new_id = 1

    new_note = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"],
        "created_date": data["created_date"]
    }

    notes.append(new_note)

    return success_response(
        "Note Created Successfully",
        new_note,
        201
    )


# ==========================================
# UPDATE Note
# ==========================================
@app.put("/notes/<int:note_id>")
def update_note(note_id):

    data = request.json

    error = validate_note(data)

    if error:
        return error_response(
            error,
            400
        )

    for note in notes:

        if note["id"] == note_id:

            note["title"] = data["title"]
            note["content"] = data["content"]
            note["created_date"] = data["created_date"]

            return success_response(
                "Note Updated Successfully",
                note
            )

    return error_response(
        "Note Not Found",
        404
    )


# ==========================================
# DELETE Note
# ==========================================
@app.delete("/notes/<int:note_id>")
def delete_note(note_id):

    for note in notes:

        if note["id"] == note_id:

            notes.remove(note)

            return success_response(
                "Note Deleted Successfully",
                note
            )

    return error_response(
        "Note Not Found",
        404
    )


# ==========================================
# Run Application
# ==========================================
app.run(debug=True)