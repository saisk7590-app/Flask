from werkzeug.exceptions import HTTPException

from errors.custom_errors import (
    ExpenseNotFoundError,
    ValidationError,
    DatabaseError
)

from utils.response import error_response


def register_error_handlers(app):
    """
    Register all application-wide
    error handlers.
    """

    @app.errorhandler(ExpenseNotFoundError)
    def handle_expense_not_found(error):

        return error_response(
            message=str(error),
            code="EXPENSE_NOT_FOUND",
            status_code=404
        )


    @app.errorhandler(ValidationError)
    def handle_validation_error(error):

        return error_response(
            message=str(error),
            code="VALIDATION_ERROR",
            status_code=400
        )


    @app.errorhandler(DatabaseError)
    def handle_database_error(error):

        return error_response(
            message=str(error),
            code="DATABASE_ERROR",
            status_code=500
        )


    # Handle Flask HTTP errors (404, 405, etc.)
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):

        return error_response(
            message=error.description,
            code=error.name.upper().replace(" ", "_"),
            status_code=error.code
        )


    # Handle all other unexpected errors
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):

        return error_response(
            message="An unexpected error occurred.",
            code="INTERNAL_SERVER_ERROR",
            status_code=500
        )