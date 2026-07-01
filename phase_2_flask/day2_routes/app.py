from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/student/<name>")
def student(name):
    return f"Student Name: {name}"

@app.route("/product/<product>")
def product(product):
    return f"Product Name: {product}"

app.run(debug=True)