from app.database.connection import get_connection

from app.models.task_model import Task



def create_task(task):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO tasks
        (
            title,
            description,
            status
        )

        VALUES (?, ?, ?)
        """,

        (
            task.title,
            task.description,
            task.status
        )
    )


    connection.commit()


    connection.close()
def get_all_tasks():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM tasks
        """
    )


    rows = cursor.fetchall()


    tasks = []


    for row in rows:

        task = Task(

            row["id"],

            row["title"],

            row["description"],

            row["status"]

        )


        tasks.append(task)


    connection.close()


    return tasks