from flask import request, render_template, redirect, url_for, Blueprint

from blueprint_flask.app import db

core = Blueprint(name='core', __name__, template_folder='templates')

@core.route('/', methods=['GET'])
def index():
    people = Person.query.all()
    return render_template(template_name_or_list='people/index.html', people=people)

        
