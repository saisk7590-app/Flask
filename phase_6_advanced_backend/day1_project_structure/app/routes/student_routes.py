from flask import Blueprint

from app.services.student_service import get_all_students

student_bp = Blueprint("students", __name__)

@student_bp.route("/students")
def get_students():
    students = get_all_students()

    return {
        "students": students
    }