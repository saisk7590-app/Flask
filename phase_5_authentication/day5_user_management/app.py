from datetime import datetime, timedelta

import bcrypt
import jwt
from flask import Flask, jsonify, request

from database import get_connection, initialize_database

app = Flask(__name__)

SECRET_KEY = "replace_this_with_a_long_random_secret_key"

initialize_database()


def authenticate_request():
    authorization_header = request.headers.get("Authorization")

    if not authorization_header:
        return None, (
            jsonify({"error": "Authorization header is missing."}),
            401,
        )

    parts = authorization_header.split()

    if len(parts) != 2 or parts[0] != "Bearer":
        return None, (
            jsonify({"error": "Invalid Authorization header format."}),
            401,
        )

    token = parts[1]

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload, None

    except jwt.ExpiredSignatureError:
        return None, (
            jsonify({"error": "Token has expired."}),
            401,
        )

    except jwt.InvalidTokenError:
        return None, (
            jsonify({"error": "Invalid token."}),
            401,
        )


@app.route("/")
def home():
    return jsonify({
        "message": "User Management API is running."
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
            "error": "Email already exists."
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


@app.route("/profile", methods=["GET"])
def get_profile():

    payload, error = authenticate_request()

    if error:
        return error

    connection = get_connection()

    user = connection.execute(
        """
        SELECT
            id,
            username,
            email
        FROM users
        WHERE id = ?
        """,
        (payload["user_id"],)
    ).fetchone()

    connection.close()

    if not user:
        return jsonify({
            "error": "User not found."
        }), 404

    return jsonify({
        "id": user["id"],
        "username": user["username"],
        "email": user["email"]
    })


@app.route("/profile", methods=["PUT"])
def update_profile():

    payload, error = authenticate_request()

    if error:
        return error

    data = request.get_json()

    username = data.get("username")

    if not username:
        return jsonify({
            "error": "Username is required."
        }), 400

    connection = get_connection()

    connection.execute(
        """
        UPDATE users
        SET username = ?
        WHERE id = ?
        """,
        (
            username,
            payload["user_id"]
        )
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Profile updated successfully."
    })


@app.route("/account", methods=["DELETE"])
def delete_account():

    payload, error = authenticate_request()

    if error:
        return error

    connection = get_connection()

    connection.execute(
        """
        DELETE FROM users
        WHERE id = ?
        """,
        (payload["user_id"],)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Account deleted successfully."
    })


if __name__ == "__main__":
    app.run(debug=True)