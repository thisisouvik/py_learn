 # Removed unnecessary Flask imports

from blueprint_flask.app import db

class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.String(120))

    def __repr__(self):
        return f'<PERSON: {self.name}, Age: {self.age}>'
    
    def get_id(self):
        return self.pid