class ExpenseNotFoundError(Exception):
    """
    Raised when the requested expense
    cannot be found.
    """
    pass


class ValidationError(Exception):
    """
    Raised when user input
    fails validation.
    """
    pass


class DatabaseError(Exception):
    """
    Raised when a database
    operation fails.
    """
    pass