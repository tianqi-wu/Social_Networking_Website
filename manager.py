from flask_script import Manager
from flask_migrate import MigrateCommand
from __init__ import create_app

#import create_app

app = create_app()

manager = Manager(app)

manager.add_command('db',MigrateCommand)

manager.run()

#if __name__ == "__main__":
#    manager.run()
