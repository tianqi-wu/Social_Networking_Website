from flask import Flask
from route import index


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', 'index', index)
    return app

