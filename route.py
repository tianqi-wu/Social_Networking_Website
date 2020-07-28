from flask import render_template, redirect, url_for
from forms import LoginForm
from models import User, Tweet


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
    if form.validate_on_submit:
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('Invalid username or password!')
            return redirect(url_for('login'))
        return redirect(url_for('index'))
    return render_template('login.html',title="Sign In",form=form)
