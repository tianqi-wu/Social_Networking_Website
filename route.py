from flask import render_template, redirect, url_for, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from forms import LoginForm, RegisterForm, EditProfileForm
from models import User, Tweet

from __init__ import db

@login_required
def index():
    name = {'username': current_user.username}
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(u, remember = form.remember_me.data)
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html',title="Sign In",form=form)

def logout():
    logout_user()
    return redirect(url_for('login'))

def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm() # Used to store the user.
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title="Registration",form=form)

@login_required
def user(username):
    u = User.query.filter_by(username=username).first()
    posts = [
    {
        'author': {'username': u.username},
        'body': "hi I'm {}!".format(u.username)
    },
    {
        'author': {'username': u.username},
        'body': "hi I'm {}!".format(u.username)
    }
    ]
    if u is None:
        abort(404)
    return render_template('user.html', title='Profile', posts=posts, user=u)

def page_not_found():
    return render_template('404.html'), 404


@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method == 'GET':
        form.about_me.data = current_user.about_me
    if form.validate_on_submit():
        current_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('profile'),username = current_user.username) # has to give profile, and username
    return render_template('edit_profile.html',form=form)
    

