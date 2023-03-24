from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(50), nullable=False)
    deadline = db.Column(db.String(50))
    priority = db.Column(db.Integer, nullable=False)

    def __init__(self, description, deadline, priority):
        self.description = description
        self.deadline = deadline
        self.priority = priority


app.app_context().push()
db.create_all()


@app.route("/todos", methods=["GET"])
def get_all_todos():
    todo_list = []
    todos = Todo.query.all()
    for todo in todos:
        todo_data = {
            "id": todo.id,
            "description": todo.description,
            "deadline": todo.deadline,
            "priority": todo.priority,
        }
        todo_list.append(todo_data)
    return {"Todo list": todo_list}, 200


@app.route("/todo", methods=["GET"])
def get_single_todo_item():
    todo_id = request.args.get("id")
    try:
        todo_item = Todo.query.get(todo_id)
        return {
            "id": todo_item.id,
            "description": todo_item.description,
            "deadline": todo_item.deadline,
            "priority": todo_item.priority,
        },  "200"
    except:
        return {"Response": "Todo item {} has not been found in the list".format(todo_id)}, 404


@app.route("/todo", methods=["POST"])
def create_todo_item():
    todo_item = Todo(
        description=request.args.get("description"),
        deadline=request.args.get("deadline"),
        priority=request.args.get("priority"),
    )
    db.session.add(todo_item)
    db.session.commit()
    return {"Response": "Todo item has been added"}, 200


@app.route("/", methods=["DELETE"])
def delete_todo_item():
    todo_id = request.args.get("id")
    try:
        todo_item = Todo.query.get(todo_id)
        db.session.delete(todo_item)
        db.session.commit()
        return {"Response": "Todo item {} has been deleted".format(todo_id)}, 200
    except:
        return {"Response": "Todo item {} has not been found in the list".format(todo_id)}, 404

if __name__ == "__main__":
    app.run(debug=True)
