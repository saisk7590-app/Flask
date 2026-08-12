import os

import psycopg
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    connection = psycopg.connect(DATABASE_URL)

    return connection


if __name__ == "__main__":
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT current_database();")

    result = cursor.fetchone()

    print("Connected database:", result[0])

    cursor.close()
    connection.close()