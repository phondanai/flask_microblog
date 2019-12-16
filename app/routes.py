from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Phondanai"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Poland!"
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!"
        },

    ]
    return render_template('index.html', user=user, posts=posts)
