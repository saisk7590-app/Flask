from datetime import datetime, timedelta

import bcrypt
import jwt
from flask import Flask, jsonify, request

from database import get_connection, initialize_database

app = Flask(__name__)

# In production, store this in an environment variable.
SECRET_KEY = "replace_this_with_a_long_random_secret_key"

initialize_database()


@app.route("/")
def home():
    return jsonify({
        "message": "JWT Authentication API is running."
    })


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({
            "error": "All fields are required."
        }), 400

    connection = get_connection()

    existing_user = connection.execute(
        """
        SELECT id
        FROM users
        WHERE email = ?
        """,
        (email,)
    ).fetchone()

    if existing_user:
        connection.close()

        return jsonify({
            "error": "Email already registered."
        }), 409

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    connection.execute(
        """
        INSERT INTO users
        (
            username,
            email,
            password
        )
        VALUES
        (
            ?,
            ?,
            ?
        )
        """,
        (
            username,
            email,
            hashed_password.decode("utf-8")
        )
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "User registered successfully."
    }), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email and password are required."
        }), 400

    connection = get_connection()

    user = connection.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
    ).fetchone()

    connection.close()

    if not user:
        return jsonify({
            "error": "Invalid email or password."
        }), 401

    password_matches = bcrypt.checkpw(
        password.encode("utf-8"),
        user["password"].encode("utf-8")
    )

    if not password_matches:
        return jsonify({
            "error": "Invalid email or password."
        }), 401

    payload = {
        "user_id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({
        "message": "Login successful.",
        "token": token
    }), 200


if __name__ == "__main__":
    app.run(debug=True)