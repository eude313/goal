from . import auth
# from . import main 
from flask import Flask, render_template,url_for
from .forms import registrationForm, loginForm

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'd5c3d02c8abc064f2b1f5a83'

@auth.route('/signup', methods=['POST', 'GET'])
def signUp():
    form = registrationForm()
    return render_template('signUp.html', form= form, title='signUp')

@auth.route("/login", methods=['POST', 'GET'])
def signIn():
    form = loginForm()
    return render_template('signIn.html', form= form, title="signIn")

