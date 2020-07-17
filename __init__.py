from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

from route import index, login

def create_app():
    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:social_network.db"
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login','login', login, methods=['GET','POST'])
    return app

