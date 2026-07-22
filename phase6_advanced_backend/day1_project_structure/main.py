from flask import Flask

from app.routes.student_routes import student_bp

app = Flask(__name__)

app.register_blueprint(student_bp)

@app.route("/")
def home():
    return {"message": "Welcome to Phase 6"}

if __name__ == "__main__":
    app.run(debug=True)