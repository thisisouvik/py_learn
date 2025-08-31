from flask import Flask , request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>HEllo world</h1>"

@app.route('/xyz')
def hello():
    return "Hello World"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f' {num1} + {num2} = {num1+num2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' is request.args.keys():
        greeting = request.args['greeting']
        name = request.args['name']
        return f'{greeting} {name}'
    else:
        return "Some parameters missing"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)