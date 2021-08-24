from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Required, EqualTo, Email

class registrationForm(FlaskForm):
    email = StringField('Email Address',validators=[Required(),Email()])
    username = StringField(' username',validators = [Required(), Length(min=3, max=10)])
    password = PasswordField('Password',validators = [Required(), Length(min=3, max=10) ])
    confirm_password = PasswordField('Confirm Password',validators = [Required(), EqualTo('confirm_password',message = 'Passwords must match')])
    submit = SubmitField('Sign Up')

class loginForm(FlaskForm):
    email = StringField('Your Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    
