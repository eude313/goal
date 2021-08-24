from flask_sqlalchemy import sqlalchemy
from flask import app
from datetime import datetime

db = sqlalchemy(app)
class user( db.models):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(6), unique=True, nullable=False)
    email = db.column(db.String(120), unique=True, nullable=False)
    image_file = db.column(db.String(20), nullable=False, default= 'default.jpeg')
    password =db.column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='auther', lazy='True')
    
    #how the object is printed when printed out
    def __repr__(self):
        return f"user"('{self.username}','{self.email}','{self.image_file}')
    
class Post( db.models):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)
    def __repr__(self):
        return f"Post"('{self.title}','{self.date_posted}')
    