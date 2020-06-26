from flask import Flask
from route import index, login


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login','login', login, methods=['GET','POST'])
    return app

