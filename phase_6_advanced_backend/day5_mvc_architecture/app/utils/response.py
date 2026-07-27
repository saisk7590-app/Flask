def success_response(
    message,
    data,
    status_code
):

    return {

        "success": True,

        "message": message,

        "data": data

    }, status_code