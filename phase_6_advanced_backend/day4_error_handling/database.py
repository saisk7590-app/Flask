import sqlite3

from errors.custom_errors import DatabaseError

DATABASE_NAME = "expenses.db"


def get_connection():
    """
    Creates and returns a SQLite database connection.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Reads schema.sql and creates the required database tables.
    """

    connection = get_connection()

    try:

        with open("schema.sql", "r") as file:

            connection.executescript(file.read())

        connection.commit()

    except sqlite3.Error as error:

        raise DatabaseError(
            "Failed to initialize the database."
        ) from error

    finally:

        connection.close()


def add_expense(title, amount, category):
    """
    Inserts a new expense into the database.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO expenses
            (
                title,
                amount,
                category
            )

            VALUES (?, ?, ?)
            """,
            (
                title,
                amount,
                category
            )
        )

        connection.commit()

    except sqlite3.Error as error:

        raise DatabaseError(
            "Failed to save expense."
        ) from error

    finally:

        connection.close()


def get_all_expenses(simulate_error=False):
    """
    Returns all expenses.

    Set simulate_error=True to test
    DatabaseError handling.
    """

    if simulate_error:

        raise DatabaseError(
            "Database connection failed (Simulated)."
        )

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM expenses
            ORDER BY id DESC
            """
        )

        expenses = cursor.fetchall()

        return expenses

    except sqlite3.Error as error:

        raise DatabaseError(
            "Unable to fetch expenses."
        ) from error

    finally:

        connection.close()