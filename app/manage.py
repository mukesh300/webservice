import os
import unittest
import sys

# sys.path.append('/home/mukesh/PycharmProjects/webservice/app/__init__.py')

from flask_migrate import Migrate
from main import create_app, db
from app import blueprint
from main.model import user

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db)


def run():
    app.run()


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    run()
