import logging

from flask import Flask
from flask import request

from database import (
    initialize_database,
    add_expense,
    get_all_expenses
)

from handlers.error_handler import (
    register_error_handlers
)

from errors.custom_errors import (
    ValidationError,
    ExpenseNotFoundError
)

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

register_error_handlers(app)

initialize_database()


@app.route("/")
def home():

    return {
        "message": "Welcome to Safe Expense Tracker API"
    }


# ===========================================
# GET ALL EXPENSES
# ===========================================

@app.route("/expenses", methods=["GET"])
def expenses():

    # Optional testing parameter
    # Example:
    # /expenses?simulate=db

    simulate = request.args.get("simulate")

    expenses = get_all_expenses(
        simulate_error=(simulate == "db")
    )

    result = []

    for expense in expenses:

        result.append(dict(expense))

    return {
        "success": True,
        "expenses": result
    }


# ===========================================
# CREATE EXPENSE
# ===========================================

@app.route("/expenses", methods=["POST"])
def create_expense():

    data = request.get_json()

    if data is None:

        raise ValidationError(
            "Request body must be valid JSON."
        )

    title = data.get("title")
    amount = data.get("amount")
    category = data.get("category")

    if not title:

        raise ValidationError(
            "Title is required."
        )

    if amount is None:

        raise ValidationError(
            "Amount is required."
        )

    if not isinstance(amount, (int, float)):

        raise ValidationError(
            "Amount must be a number."
        )

    if amount <= 0:

        raise ValidationError(
            "Amount must be greater than zero."
        )

    if not category:

        raise ValidationError(
            "Category is required."
        )

    add_expense(
        title,
        amount,
        category
    )

    logging.info("Expense added successfully.")

    return {
        "success": True,
        "message": "Expense added successfully."
    }, 201


# ===========================================
# TEST CUSTOM 404
# ===========================================

@app.route("/expenses/<int:expense_id>")
def get_expense(expense_id):

    raise ExpenseNotFoundError(
        f"Expense with ID {expense_id} not found."
    )


# ===========================================
# TEST INTERNAL SERVER ERROR
# ===========================================

@app.route("/test500")
def test500():

    number = 10 / 0

    return {
        "number": number
    }


if __name__ == "__main__":

    app.run(
        debug=True
    )