from fastapi import FastAPI

api = FastAPI()

#GET - getting information from  server
#POST- creating/submit in the server
#PUT - putting req in server
#DELETE - deleting something in server

all_todos = [
    {'todo_id': 1, "role": "Student", "Desc": "Jobless"},
    {'todo_id': 2, "role": "Freak", "Desc": "Pitambara"},
    {'todo_id': 3, "role": "Manager", "Desc": "Managing"},
    {'todo_id': 4, "role": "Guard", "Desc": "Guarding"},
    {'todo_id': 5, "role": "Plumber", "Desc": "Plumbing"}
]

@api.get('/')
def index():
    return {"message" : "Hello World"}


@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}
        
@api.get('/todos')
def get_all_todo(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
