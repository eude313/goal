from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, EqualTo, Email

class registrationForm(FlaskForm):
    username = StringField('Username', validators=[ DataRequired(), Length(min=3, max=6)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[ DataRequired(), Length(min=5, max=8)])
    confirm_password = PasswordField('Confirm_Password', validators=[Length(min=5, max=8), DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=6)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')