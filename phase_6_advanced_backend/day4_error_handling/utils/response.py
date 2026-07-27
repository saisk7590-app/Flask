def success_response(
    message,
    data=None,
    status_code=200
):
    """
    Creates a standard success response.
    """

    response = {
        "success": True,
        "message": message
    }

    if data is not None:
        response["data"] = data

    return response, status_code


def error_response(
    message,
    code,
    status_code
):
    """
    Creates a standard error response.
    """

    response = {
        "success": False,
        "error": {
            "code": code,
            "message": message
        }
    }

    return response, status_code