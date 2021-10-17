
from flask import Flask
from flask import request
todos = list()
counter = 0

app = Flask(__name__)

@app.route("/home")
def home_route():
    return "Hello World"

@app.route("/get_todos")
def get_todo_route():
    result = {"todo":todos}
    return result

@app.route("/add_todo", methods=['POST'])
def add_todo():
    data=request.get_json()
    global counter
    counter += 1
    data["id"]=counter
    todos.append(data)
    return "todo added successfully"

@app.route("/update_todo/<int:id>", methods=['PUT'])
def update_todo(id):
    print("id is: ", id, "type ", type(id))
    data = request.get_json()
    for each_todo in todos:
        if each_todo["id"] == id:
            each_todo["title"]=data["title"]
            each_todo["status"]= data["status"]
            return "todo updated!!!"
    return "todo not found!!!"

@app.route ("/delete_todo/<int:todo_id>", methods=['DELETE'])
def delete_todo(todo_id):
    for each_todo in todos:
        if each_todo["id"] == todo_id:
            todos.remove(each_todo)
            return "deleted successfully"

    return "data not found..."

app.run(debug=True)

