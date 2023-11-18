import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'a-very-big-apple-tree'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

TEMPLATES_AUTO_RELOAD = True