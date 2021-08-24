from . import auth
from webapp import db, bcrypt
from ..models import User
from flask import  render_template,url_for, flash, redirect
from .forms import registrationForm, loginForm

@auth.route('/signup', methods=['POST', 'GET'])
def signUp():
    form = registrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login ', 'success')
        return redirect(url_for('auth.signIn'))
    return render_template('signUp.html', form= form, title='signUp')

@auth.route("/login", methods=['POST', 'GET'])
def signIn():
    form = loginForm()
    if form.validate_on_submit():
        flash('you have successfully Loged in', 'success')
        return redirect(url_for('main.home'))
    return render_template('signIn.html', form= form, title="signIn")

