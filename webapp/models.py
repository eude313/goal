from flask_sqlalchemy import sqlalchemy
from flask import app
from datetime import datetime
from webapp import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
# db = sqlalchemy(app)
class User( db.Model,UserMixin ):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default= "https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(45).jpg")
    password =db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)
    
    #how the object is printed when printed out
    def __repr__(self):
        return f"user"('{self.username}','{self.email}','{self.image_file}')
    
class Post( db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post"('{self.title}','{self.date_posted}')
    


class Quote:
    '''
    Quote class to define quote Objects
    '''
    def __init__(self,author,id,quote,permalink):
        self.id =id
        self.author = author
        self.quote = quote
        self.permalink = permalink