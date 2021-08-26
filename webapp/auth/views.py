import webapp
from . import auth
from webapp import db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from ..models import User
from flask import  render_template,url_for, flash, redirect
from .forms import registrationForm, loginForm, Update_AccountForm, blog_form
import json
import os
import secrets
from ..request import get_quotes


@auth.route('/signup', methods=['POST', 'GET'])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
           login_user(user, remember=form.remember.data)
           return redirect(url_for('main.home')) 
        else:
            flash('login unsuccessful. please check your email or password.', 'danger')
    return render_template('signIn.html', form= form, title="signIn")

@auth.route("/logout")
def signOut():
    logout_user()
    return redirect(url_for('main.home')) 

def save_picture( form_picture):
    random_hex = secrets.token_hex(8)
    f_ext = os.path.splitext(form_picture.file_name)
    picture_fn = random_hex +  f_ext 
    picture_path = os.path.join(webapp.root_path, 'static/images', picture_fn)
    form_picture.save(picture_path)

    return picture_fn

@auth.route("/account", methods=['POST', 'GET'])
@login_required
def Account():
    raw_quotes = get_quotes()
    quotes = json.loads(raw_quotes)
    form =  Update_AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
           image_file = save_picture(form.picture.data)
           current_user.image_file.data = image_file
        current_user.username.data = form.username.data
        current_user.email.data = form.email.data
        db.session.commit()
        flash(" Account has been updated", "success")
        return redirect(url_for('Account'))
    image_file = url_for('static',filename='/images/')
    return render_template('Profile.html',  title="Profile", image_file= image_file, form= form, quotes=quotes)



@auth.route('/blogs/new', methods=['POST', 'GET'])
@login_required
def blogs():
    raw_quotes = get_quotes()
    quotes = json.loads(raw_quotes)
    form =blog_form()
    if form.validate_on_submit():
        flash( " post has been created", "success" )
        return redirect('blogs')
    return render_template('blogs.html',form=form, quotes=quotes)