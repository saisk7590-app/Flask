from flask import Blueprint


from app.controllers.task_controller import (
    create_task_controller,
    get_tasks_controller
)



task_bp = Blueprint(
    "tasks",
    __name__
)



@task_bp.route(
    "/tasks",
    methods=["POST"]
)
def create_task():

    return create_task_controller()



@task_bp.route(
    "/tasks",
    methods=["GET"]
)
def get_tasks():

    return get_tasks_controller()