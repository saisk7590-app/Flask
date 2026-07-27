from flask import Flask


from app.routes.task_routes import task_bp

from app.database.connection import (
    initialize_database
)



def create_app():

    app = Flask(__name__)


    initialize_database()


    app.register_blueprint(
        task_bp
    )


    return app