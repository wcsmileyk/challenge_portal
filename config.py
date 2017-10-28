import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''
    Base Configuration values. Any values used across the app go here. If running locally, need to set a shell variable
    of SECRET_KEY and HMAC_SALT
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SQL Alchemy Config Options
    SQLALCHEMY_COMMIT_ON_TEARTDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Security Config Options
    SECURITY_REGISTERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = os.environ.get('HMAC_SALT')
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_UNAUTHORIZED_VIEW = 'main.internal_server_error'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '''
    Set configuration values for development environments.
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev-db.sqlite')

    # Flask-Mail setup
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SECURITY_EMAIL_SENDER = os.environ.get('MAIL_USERNAME')



class TestingConfig(Config):
    '''Set configuration values for testing environment'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test-db.sqlite')


class ProdConfig(Config):
    '''Set configuration values for testing environment'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # TODO: Set up production email


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProdConfig,
    'default': DevelopmentConfig
}
