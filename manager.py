from app import app
from ext import db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from models.user import User


migrate = Migrate(app, db)
manager = Manager(app)
server = Server(host='0.0.0.0', port='5000',use_debugger=True)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', server)

if __name__ == '__main__':
    manager.run()