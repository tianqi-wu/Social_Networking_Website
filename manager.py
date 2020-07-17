from flask_script import Manager
from flask_migrate import MigrateCommand
from __init__ import create_app

#import create_app

app = create_app()

app.run(host="0.0.0.0", port=5000)

#if __name__ == "__main__":
#    manager.run()
