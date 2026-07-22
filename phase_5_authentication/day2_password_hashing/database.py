import sqlite3


DATABASE_NAME = "users.db"


def get_connection():
    """
    Create and return a SQLite connection.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Create database tables from schema.sql.
    """

    connection = get_connection()

    with open("schema.sql", "r") as schema_file:
        connection.executescript(schema_file.read())

    connection.commit()
    connection.close()