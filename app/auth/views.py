from app import auth
from flask import Flask, render_template
from forms import registrationForm, loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd5c3d02c8abc064f2b1f5a83'

@auth.route('/', methods=['POST', 'GET'])
def signup():
    form = registrationForm()
    return render_template('signup.html', form= form, title='Login')

@app.route("/login", methods=['POST', 'GET'])
def signIn():
    form = loginForm()
    return render_template('index.html', form= form, title="signIn")

