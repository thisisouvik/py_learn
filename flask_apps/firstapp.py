from flask import Flask , request, make_response, render_template

app = Flask(__name__, template_folder= 'templates')

@app.route('/')
def index():
    mylist = [10, 12, 13]
    return render_template(template_name_or_list='index.html', my_list=mylist)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555 ,debug = True)