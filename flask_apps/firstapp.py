from flask import Flask , request, make_response, render_template, jsonify
import pandas as pd

app = Flask(__name__, template_folder= 'templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username =='souvik' and password== 'password':
            return f'Welcome {username}'
        else:
            return 'Invalid credentials'

@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        df=pd.read_excel(file)
        return df.to_html()
    else:
        return 'Invalid file type'
    
@app.route('/handle_post', methods= ['POST'])
def handle_post():
    greeting = request.json['greetings']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')

    return jsonify({'message':' Sucessfully written'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)