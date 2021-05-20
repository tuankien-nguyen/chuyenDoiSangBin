from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello moi nguoi, nhom huffi xin chao tat ca!"
