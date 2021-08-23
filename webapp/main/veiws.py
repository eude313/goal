from flask import render_template, url_for
from . import main

# landing page
@main.route('/')
def home():
    return render_template('index.html')

@main.route('/blogs')
def blogs():
    return render_template('blogs.html')

@main.route('/quotes')
def quotes():
    return render_template('quotes.html')