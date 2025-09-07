from flask import request, render_template, redirect, url_for, Blueprint

from blueprint_flask.app import db

from blueprint_flask.blueprints.todos.models import Todo

todos = Blueprint(name : 'todos', __name__ , template_folder='templates')

@todos.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)