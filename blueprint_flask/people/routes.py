from flask import request, render_template, redirect, url_for, Blueprint

from blueprint_flask.app import db

from blueprint_flask.todos.models import Person

people = Blueprint('todos', __name__, template_folder='templates')

@people.route('/', methods=['GET'])
def index():
    people = Person.query.all()
    return render_template(template_name_or_list='people/index.html', people=people)


@people.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET': 
        return render_template('people/create.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        age= request.form.get('age')
        job = request.form.get('job')

        job = job if job != '' else None

        person = Person(name=name, age=age, job=job)

        db.session.add(person)
        db.session.commit()

        return redirect(url_for('todo.index'))
        
