from flask import render_template, request

from models import Person

def register_routes(app, db):

    @app.route('/', methods= ['GET', 'POST'])
    def index():
        message = None
        if request.method == 'POST':
            name = request.form.get('name')
            age = request.form.get('age')
            job = request.form.get('job')

            if name:
                try:
                    age_val = int(age) if age else None
                except ValueError:
                    age_val = None

                person = Person(name=name, age=age_val, job=job)
                db.session.add(person)
                db.session.commit()
                message = f'Added {name}'

        people = Person.query.all()
        return render_template(template_name_or_list= 'index.html', people=people, message=message)