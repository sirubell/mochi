import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY_LONG_SECRET-KEY'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get(('DATABASE_URL')) or 'sqlite:///' + os.path.join(basedir, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_DEFAULT_SENDER='admin'
    MAIL_USERNAME='vbg12301230@gmail.com'
    MAIL_PASSWORD='wjbhixguddlinhpc'
