from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.get("/")
def home():
    return jsonify({
        "message": "Flask API is running"
    })


if __name__ == "__main__":
    app.run(debug=True)