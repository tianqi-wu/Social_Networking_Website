import os

config_path = os.path.abspath(os.path.dirname(__file__))


#    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///social_network.db"
#    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, 'social_network.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'abc123'
