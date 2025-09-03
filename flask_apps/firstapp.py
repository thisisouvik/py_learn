from flask import Flask , request, make_response, render_template, jsonify, session, flash

app = Flask(__name__, template_folder= 'templates')

app.secret_key = 'SOME_KEY'

@app.route('/')
def index():
    # Render the index template so the form, buttons and session links are visible
    return render_template('index.html')

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'
    # pass session values and a message to the template
    return render_template('index.html', message='Session data set', name=session.get('name'), other=session.get('other'))

@app.route('/get_data')
def get_data():
    name = session.get('name')
    other = session.get('other')

    if not name and not other:
        message = 'No session data found. Call Set Session Data first.'
    else:
        message = f'Name: {name}, Other: {other}'
    return render_template('index.html', message=message, name=name, other=other)

@app.route('/clear_data')
def clear_data():
    session.clear()

    return render_template('index.html', message= 'Clear session data')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template(template_name_or_list='index.html', message='cookie set'))
    response.set_cookie(key='cookie_name', value='cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template(template_name_or_list='index.html', message = f'Cookie value {cookie_value}')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Souvik' and password == 'Posword':
            flash('Login Sucessful!!!')
            return render_template(template_name_or_list= 'index.html', message = f' username = {username} logged in')
        else:
            flash('Login!!!')
            return render_template(template_name_or_list='index.html', message = 'Not found')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)