from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is Yufine Training Co.</p>"


@app.route("/add/", methods=['GET', 'POST'])
def add():
    data = request.json
    
    output = ""
    sum = 0
    for a in data[0:len(data)-1]:
        output += f"{a} + "
        sum += a

    output += f"{data[-1]}"
    sum += data[-1]
    output += f" = {sum}"
    
    return output
