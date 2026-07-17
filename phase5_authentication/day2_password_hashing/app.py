from flask import Flask, request, jsonify
import bcrypt

from database import get_connection, initialize_database


app = Flask(__name__)

initialize_database()


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Authentication API is running."
        }
    )


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:

        return jsonify(
            {
                "error": "All fields are required."
            }
        ), 400

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

        return jsonify(
            {
                "error": "Email already registered."
            }
        ), 409

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

    return jsonify(
        {
            "message": "User registered successfully."
        }
    ), 201


if __name__ == "__main__":
    app.run(debug=True)