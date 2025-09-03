from flask import Flask , request, make_response, render_template, jsonify, session

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

@app.route('clear_data')
def clear_data():
    session.clear()

    return render_template('index.html', )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)