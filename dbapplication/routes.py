from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from models import Person, User

from models import Person

def register_routes(app, db, bcrypt):
    @app.route('/', methods=['GET','POST'])
    def index():
        people = Person.query.all()
        return render_template(template_name_or_list='index.html', people=people)
    
    @app.route('/signup', methods = ['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username= request.form.get('username')
            password= request.form.get('password')

            hashed_password=bcrypt.generate_password_hash(password)

            user= User(username=username, password= password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

    @app.route('/login/<int:uid>')
    def login(uid):
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username =request.form.get('username')
            password = request.form.get('password')

            hashed_password= bcrypt.generated_password_hash(password)

            user = User.query.filter(User.username == username).first()

            if bcrypt.check_password_hash(user.password, password):
                login(user)
                return render_template('index.html')
            else:
                return 'Login Failed!!!'
    
    @app.route('/logout')
    def logout():
        logout_user()
        return 'Success'

    @app.route('/delete/<int:pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        return {'success': True}
