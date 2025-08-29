from flask import Flask

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)