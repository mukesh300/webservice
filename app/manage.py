import os
import unittest
import sys

sys.path.append('/home/mukesh/PycharmProjects/webservice/app/__init__.py')
__package__ = "app"

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import create_app, db
from app import blueprint
from main.model import user
from main.model import blacklist

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    # app.run(host='0.0.0.0', port=5000)
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
