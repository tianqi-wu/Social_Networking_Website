from flask_script import Manager
from flask_migrate import MigrateCommand
from __init__ import create_app

#import create_app

app = create_app()
server = Server(host="0.0.0.0", port=5000)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command("runserver", server)

manager.run()

#if __name__ == "__main__":
#    manager.run()
