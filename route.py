from flask import render_template
from forms import LoginForm

def index():
    name = {'username':'root'}
    posts = [
        {
            'author': {'username': 'root'},
            'body': "hi I'm root!"
        },
        {
            'author': {'username': 'test'},
            'body': "hi I'm test!"
        },

    ]
    return render_template('index.html', name=name, posts=posts)


def login():

    form = LoginForm(csrf_enabled=False)
    return render_template('login.html'，title="Sign In",form=form)