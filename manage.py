""" handles db migrations """

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

# import models
from models.user import User
from models.admin import Admin

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()