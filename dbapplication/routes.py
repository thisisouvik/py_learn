from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from models import Person, User


def register_routes(app, db, bcrypt):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        people = Person.query.all()
        return render_template('index.html', people=people)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')

        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash('Username and password required')
            return redirect(url_for('signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created, please log in')
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        # If already logged in, redirect to index
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        if request.method == 'GET':
            return render_template('login.html')

        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            flash('Login failed')
            return redirect(url_for('index'))

        login_user(user)
        flash('Logged in')
        return redirect(url_for('index'))

    @app.route('/logout')
    @login_required
    def logout():
        # log the user out and clear the session
        logout_user()
        session.clear()
        flash('Logged out')
        return redirect(url_for('index'))

    @app.route('/delete/<int:pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        return {'success': True}

    @app.route('/secret')
    @login_required
    def secret():
        # simple protected endpoint
        username = getattr(current_user, 'username', None)
        return f'Secret page. Hello {username or "user"}.'

