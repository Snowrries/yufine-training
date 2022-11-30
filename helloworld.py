from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is Yufine Training Co.</p>"


@app.route("/add/")
def add_2_and_2():
    return f"<p>2 + 2 = {2+2}</p>"

