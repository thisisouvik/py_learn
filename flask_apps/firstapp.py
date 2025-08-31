from flask import Flask , request, make_response, render_template

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
    if request.method == 'POST':
        file = request.files.get('file')
        
        if file:
            file.save(f'uploads/{file.filename}')
            return 'File uploaded successfully'
    return render_template('file_upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)