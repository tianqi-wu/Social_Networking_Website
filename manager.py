from flask_script import Manager

import os, sys

from __init__ import create_app

#import create_app

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
