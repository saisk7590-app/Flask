from flask import request


from app.services.task_service import (
    create_new_task,
    fetch_tasks
)


from app.utils.response import (
    success_response
)



def create_task_controller():

    data = request.get_json()


    task = create_new_task(

        data.get("title"),

        data.get("description"),

        data.get("status")

    )


    return success_response(
        "Task created successfully",
        task.to_dict(),
        201
    )



def get_tasks_controller():


    tasks = fetch_tasks()


    data = []


    for task in tasks:

        data.append(
            task.to_dict()
        )


    return success_response(
        "Tasks fetched successfully",
        data,
        200
    )