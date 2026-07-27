def validate_student(data):
    errors = []

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    # Name Validation
    if not name:
        errors.append("Name is required.")
    elif len(name.strip()) < 3:
        errors.append("Name must contain at least 3 characters.")

    # Age Validation
    if age is None:
        errors.append("Age is required.")
    elif not isinstance(age, int):
        errors.append("Age must be an integer.")
    elif age <= 0:
        errors.append("Age must be greater than 0.")

    # Course Validation
    if not course:
        errors.append("Course is required.")

    return errors