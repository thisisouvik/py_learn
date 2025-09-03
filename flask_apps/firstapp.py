from flask import Flask , request, make_response, render_template, jsonify, session

app = Flask(__name__, template_folder= 'templates')

app.secret_key = 'SOME_KEY'

@app.route('/')
def index():
    return 'Hello World'

@app.route('/set_data')
def set_data():
    session['name']= 'Mike'
    session['other'] = 'Hello World'
    return render_template(template_name_or_list= 'index.html', message = ' Session data set')

@app.route('get_data')
def get_data():
    Name = session['name']
    others = session['other']
    return render_template(template_name_or_list='index.html', message= f'Name : {Name}, Other: {others}')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)