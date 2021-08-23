from . import auth
from flask import  render_template,url_for, flash, redirect
from .forms import registrationForm, loginForm

@auth.route('/signup', methods=['POST', 'GET'])
def signUp():
    form = registrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('signUp.html', form= form, title='signUp')

@auth.route("/login", methods=['POST', 'GET'])
def signIn():
    form = loginForm()
    if form.validate_on_submit():
        flash('you have successfully Loged in', 'success')
        return redirect(url_for('main.home'))
    return render_template('signIn.html', form= form, title="signIn")

