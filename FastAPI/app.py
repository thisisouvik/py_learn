from fastapi import FastAPI

api = FastAPI()

#GET - getting information from  server
#POST- creating/submit in the server
#PUT - putting req in server
#DELETE - deleting something in server

@api.get('/')
def index():
    return