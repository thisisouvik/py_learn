from flask import render_template, request

from models import Person

def register_routes(app, db):

    @app.route('/', methods= ['GET', 'POST'])
    def index():
        people = Person.query.all()
        return render_template(template_name_or_list= 'index.html', people =people)