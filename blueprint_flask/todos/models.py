from flask import request, render_template, redirect, url_for, flash, Blueprint

from blueprint_flask.app import db

class Person(db.Model):
    __tablename__ = 'table'

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, primary_key=False)
    description = db.Column(db.Integer)
    done = db.Column(db.Boolean, nullable= False)

    def __repr__(self):
        return f'<TODO {self.title}, Done: {self.done}>'
    
    def get_id(self):
        return self.tid