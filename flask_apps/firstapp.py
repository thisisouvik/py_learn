from flask import Flask , request, make_response, render_template, jsonify

app = Flask(__name__, template_folder= 'templates', static_folder= 'static', static_url_path='/')

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)