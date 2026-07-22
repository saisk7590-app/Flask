from flask import Flask

from config.settings import (
    APP_NAME,
    DATABASE_PATH,
    DEBUG,
    SECRET_KEY,
    VERSION,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def home():
    return {
        "application": APP_NAME,
        "database": DATABASE_PATH,
        "debug": DEBUG,
        "secret_key": SECRET_KEY,
        "version": VERSION,
    }


if __name__ == "__main__":
    app.run(debug=True)