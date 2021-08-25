import json
from ..request import get_quotes
from flask import render_template, url_for
from . import main

# landing page
@main.route('/')
def home():
    return render_template('index.html')

@main.route('/blogs')
def blogs():
    raw_quotes = get_quotes()
    quotes = json.loads(raw_quotes)
    return render_template('blogs.html', quotes=quotes)

