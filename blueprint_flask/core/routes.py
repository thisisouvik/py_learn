from flask import request, render_template, redirect, url_for, Blueprint

from blueprint_flask.app import db
from blueprint_flask.people.models import Person

core = Blueprint('core', __name__, template_folder='templates')

@core.route('/', methods=['GET'])
def index():
    people = Person.query.all()
    return render_template('people/index.html', people=people)

        
