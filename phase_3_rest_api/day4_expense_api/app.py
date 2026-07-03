from flask import Flask, jsonify, request

app = Flask(__name__)

# ==========================================
# Temporary Database
# ==========================================
expenses = [
    {
        "id": 1,
        "amount": 250,
        "category": "Food",
        "description": "Lunch",
        "payment_method": "UPI"
    },
    {
        "id": 2,
        "amount": 120,
        "category": "Travel",
        "description": "Bus Ticket",
        "payment_method": "Cash"
    }
]


def validate_expense(data):
    if not data:
        return "Request body is required"

    required_fields = [
        "amount",
        "category",
        "description",
        "payment_method"
    ]

    for field in required_fields:
        if field not in data:
            return f"{field} is required"

    return None


@app.get("/")
def home():
    return jsonify({
        "success": True,
        "message": "Expense Tracker API",
        "phase": "Phase 3 - Day 4"
    }), 200


@app.get("/expenses")
def get_expenses():
    return jsonify({
        "success": True,
        "count": len(expenses),
        "data": expenses
    }), 200


@app.get("/expenses/<int:expense_id>")
def get_expense(expense_id):

    for expense in expenses:
        if expense["id"] == expense_id:
            return jsonify({
                "success": True,
                "data": expense
            }), 200

    return jsonify({
        "success": False,
        "message": "Expense Not Found"
    }), 404


@app.post("/expenses")
def create_expense():

    data = request.json

    error = validate_expense(data)

    if error:
        return jsonify({
            "success": False,
            "message": error
        }), 400

    if expenses:
        new_id = max(expense["id"] for expense in expenses) + 1
    else:
        new_id = 1

    new_expense = {
        "id": new_id,
        "amount": data["amount"],
        "category": data["category"],
        "description": data["description"],
        "payment_method": data["payment_method"]
    }

    expenses.append(new_expense)

    return jsonify({
        "success": True,
        "message": "Expense Created Successfully",
        "data": new_expense
    }), 201


@app.put("/expenses/<int:expense_id>")
def update_expense(expense_id):

    data = request.json

    error = validate_expense(data)

    if error:
        return jsonify({
            "success": False,
            "message": error
        }), 400

    for expense in expenses:
        if expense["id"] == expense_id:

            expense["amount"] = data["amount"]
            expense["category"] = data["category"]
            expense["description"] = data["description"]
            expense["payment_method"] = data["payment_method"]

            return jsonify({
                "success": True,
                "message": "Expense Updated Successfully",
                "data": expense
            }), 200

    return jsonify({
        "success": False,
        "message": "Expense Not Found"
    }), 404


@app.delete("/expenses/<int:expense_id>")
def delete_expense(expense_id):

    for expense in expenses:
        if expense["id"] == expense_id:

            expenses.remove(expense)

            return jsonify({
                "success": True,
                "message": "Expense Deleted Successfully",
                "data": expense
            }), 200

    return jsonify({
        "success": False,
        "message": "Expense Not Found"
    }), 404


app.run(debug=True)