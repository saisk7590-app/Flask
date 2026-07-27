import sqlite3

DATABASE_NAME = "students.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    with open("schema.sql", "r") as file:
        connection.executescript(file.read())

    connection.commit()
    connection.close()


def add_student(name, age, course):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students (name, age, course)
        VALUES (?, ?, ?)
        """,
        (name, age, course),
    )

    connection.commit()
    connection.close()