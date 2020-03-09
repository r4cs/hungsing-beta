import os
from notificadorHSproject import app

os.environ['DATABASE_URL'] = "postgres://zxqyvveypxgjuj:922e4159152ba1013a5c0bc4e2710e2b550f8467864b17e925435d744535f951@ec2-34-192-30-15.compute-1.amazonaws.com:5432/d6beobe9ouo427"

# OBS:

# os.environ.get('') => localiza pela value daqui, que tb eh key quando em exports, ex:
#    os.environ.get('APP_MAIL_USERNAME') retorna 'n0t1f1c4d0r'
#    os.environ.get('MAIL_USERNAME') n retrona nada
#
# app.config[''] => localiza pela key do script, ex:
#    app.config['MAIL_USERNAME'] retorna 'n0t1f1c4d0r'
#     app.config['APP_MAIL_USERNAME'] retorna KeyError


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['PASSWORD_SALT'] = os.environ.get('SECURITY_PASSWORD_SALT')


    # mail settings
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465

    # # gmail authentication
    app.config['MAIL_USERNAME'] = os.environ.get('APP_MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('APP_MAIL_PASSWORD')
    # mail account
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get("MAIL_DEFAULT_SENDER")



class ProductionConfig(BaseConfig):
    DEBUG = True


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
