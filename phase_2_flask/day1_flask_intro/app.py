from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my API"

@app.route("/about")
def about():
    return "I am learning Flask"

@app.route("/contact")
def contact():
    return "Contact: sai@example.com"

app.run()
