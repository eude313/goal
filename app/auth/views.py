from config import Config
from flask import Flask, render_template
from forms import registrationForm, loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.get('SECRET_KEY')

@app.route("/")
def register():
    form = registrationForm()
    return render_template( "signUp.html", form=form, title="Register" )

@app.route("/login")
def logIn():
    form = loginForm()
    return render_template( "signIn.html", form=form, title="login" )

if __name__ == "__main__" :
    app.run(debug=True)