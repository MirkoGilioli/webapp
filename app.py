from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "AWS is great!"

@app.route("/dev")
def dev():
    return "This is the dev page"
