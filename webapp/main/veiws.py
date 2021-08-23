from flask import render_template, url_for
from . import main

# landing page
@main.route('/')
def home():
    return render_template('index.html')