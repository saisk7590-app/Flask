from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():

    return {
        "success": True,
        "message": "Deployment Ready Flask API is running."
    }


@app.route("/health")
def health_check():

    return {
        "success": True,
        "status": "healthy"
    }


if __name__ == "__main__":

    app.run(
        debug=True
    )