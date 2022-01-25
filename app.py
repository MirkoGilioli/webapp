from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello datatonic!"
#This method is a dev a methos
@app.route("/dev")
def dev():
    return "This is the dev page"
