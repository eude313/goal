from flask_wtf import Flask_form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, DataRequired, EqualTo

class registrationForm( Flask_form):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=6)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=8)])
    confirm_password = PasswordField('confirm_password', validators=[Length(min=5, max=8), DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class loginForm( Flask_form):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=6)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')