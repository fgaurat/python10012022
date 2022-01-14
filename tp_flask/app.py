from flask import Flask
from TodoDAO import TodoDAO
app = Flask(__name__)

@app.route("/")
def hello_world():
    dao = TodoDAO("todos.db")
    html = ""
    for todo in dao.findAll():
        html+=todo.title+"<br/>"
    return html

@app.route("/toto")
def toto():
    return "<h1>toto</h1>"
