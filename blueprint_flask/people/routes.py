from flask import request, render_template, redirect, url_for, Blueprint

from blueprint_flask.app import db

from blueprint_flask.todos.models import Todo

todos = Blueprint('todos', __name__, template_folder='templates')

@todos.route('/', methods=['GET'])
def index():
    todos_list = Todo.query.all()
    return render_template(template_name_or_list='todos/index.html', todos=todos)


@todos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET': 
        return render_template('todos/create.html')
    elif request.method == 'POST':
        title= request.form.get('title')
        description= request.form.get('description')
        done = True if 'done' in request.form.keys() else False

        description = description if description != '' else None

        todo = Todo(name=name, description=description, done=done)

        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('todo.index'))
        
