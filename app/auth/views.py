from .forms import registrationForm, loginForm
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/register")
def register():
    form = registrationForm()
    return render_template( "signUp.html", form=form, title="Register" )

@app.route("/login")
def logIn():
    form = loginForm()
    return render_template( "signIn.html", form=form, title="login" )