from enum import IntEnum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_names: str = Field(..., min_length=3, max_length=512, description= 'Name of the todo')
    todo_description:str =Field(..., description='Description of the todo')
    priority: Priority =Field(default=Priority.LOW, description='Priority of the todo')
    
    


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
    
@api.post('/todos')
def create_todo(todo : dict):
    new_todo_id= max(todo['todo_id'] for todo in all_todos) + 1

    new_todo = {
        'todo_id' : new_todo_id,
        'role' : todo['role'],
        'Desc' : todo['Desc']
    }

    all_todos.append(new_todo)

    return  new_todo

@api.put('/todos/{todo_id}')
def ubdate_todo(todo_id: int, ubdated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['role'] == ubdate_todo['role']
            todo['Desc'] == ubdate_todo['Desc']
            return todo
        return "Error, Not Found!"
    
@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            delete_todo = all_todos.pop(index)
            return delete_todo
        return "Error! Not Found"