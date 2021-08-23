from flask_sqlalchemy import sqlalchemy
from flask import app

db = sqlalchemy(app)
class user( db.models):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(6), unique=True, nullable=False)
    email = db.column(db.String(120), unique=True, nullable=False)
    image_file = db.column(db.String(20), nullable=False, default= 'default.jpeg')
    password =db.column(db.String(60), nullable=False)
    
    #how the object is printed when printed out
    def __repr__(self):
        return f"User"('{self.username}','{self.email}','{self.image_file}')
    
class post( db.models):
    id = db.Column(db.Integer, primary_key=True)