import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is missing.")

DATABASE_PATH = os.getenv("DATABASE_PATH", "students.db")

APP_NAME = os.getenv("APP_NAME", "Student API")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

VERSION = os.getenv("VERSION", "1.0.0")