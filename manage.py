from app import create_app,db
from flask_script import Manager, Server
from app.models import User, Pitch
app = create_app('development')
app.app_context().push()

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch = Pitch)


manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()