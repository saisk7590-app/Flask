from app.models.task_model import Task

from app.repositories.task_repository import (
    create_task,
    get_all_tasks
)


VALID_STATUSES = [
    "pending",
    "completed"
]


def create_new_task(
    title,
    description,
    status
):

    if not title:

        raise ValueError(
            "Task title is required"
        )


    if status not in VALID_STATUSES:

        raise ValueError(
            "Invalid task status"
        )


    task = Task(
        None,
        title,
        description,
        status
    )


    create_task(task)


    return task



def fetch_tasks():

    return get_all_tasks()