from flask import Flask

import logging

from config import Config


# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Flask Application
# --------------------------------------------------

app = Flask(__name__)

app.config.from_object(Config)


logger.info("Flask application starting")


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.route("/health", methods=["GET"])
def health():
    """
    Health check endpoint.

    Used to verify that the Flask application
    is running correctly.
    """

    logger.info("Health check requested")

    return {
        "status": "healthy"
    }, 200


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.route("/", methods=["GET"])
def home():
    """
    Basic API information endpoint.
    """

    return {
        "message": "Day 4 Environment Testing API",
        "status": "running"
    }, 200


# --------------------------------------------------
# Configuration Check
# --------------------------------------------------

@app.route("/config", methods=["GET"])
def config_check():
    """
    Displays safe configuration information.

    IMPORTANT:
    Actual secrets are never returned.
    Only Boolean values are exposed to confirm
    whether configuration values exist.
    """

    return {
        "debug": app.config["DEBUG"],
        "database_configured": bool(
            app.config["DATABASE_URL"]
        ),
        "secret_configured": bool(
            app.config["SECRET_KEY"]
        )
    }, 200


# --------------------------------------------------
# Test Error Endpoint
# --------------------------------------------------

@app.route("/test-error", methods=["GET"])
def test_error():
    """
    Demonstrates safe production-style error handling.

    Technical error details are logged internally,
    while the client receives a safe error message.
    """

    try:

        result = 10 / 0

        return {
            "result": result
        }, 200

    except Exception as error:

        logger.error(
            "An error occurred: %s",
            error
        )

        return {
            "error": "Internal server error"
        }, 500


# --------------------------------------------------
# Application Entry Point
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=app.config["DEBUG"]
    )