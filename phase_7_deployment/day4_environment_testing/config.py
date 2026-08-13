import os


class Config:
    """
    Central configuration for the Flask application.

    Configuration values are loaded from environment
    variables instead of being hardcoded in the source code.
    """

    # --------------------------------------------------
    # Secret Configuration
    # --------------------------------------------------

    SECRET_KEY = os.getenv("SECRET_KEY")


    # --------------------------------------------------
    # Database Configuration
    # --------------------------------------------------

    DATABASE_URL = os.getenv("DATABASE_URL")


    # --------------------------------------------------
    # Debug Configuration
    # --------------------------------------------------

    # Environment variables are strings.
    #
    # Examples:
    # DEBUG=True
    # DEBUG=true
    # DEBUG=TRUE
    #
    # .lower() makes the comparison case-insensitive.
    #
    # Default is False so that debugging is disabled
    # unless it is explicitly enabled.

    DEBUG = (
        os.getenv("DEBUG", "False").lower() == "true"
    )