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
    # TODO Convert this once I have a mail setup
    SECURITY_SEND_REGISTER_EMAIL = False

    CHALLENGE_MAIL_SUBJECT_PREFIX = '[Python Challenge]'
    CHALLENGE_MAIL_SENDER = 'Python Challenge <admin@pythonchallenge.com>'
    CHALLENGE_ADMIN = os.environ.get('APP_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '''
    Set configuration values for development environments.
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev-db.sqlite')


class TestingConfig(Config):
    '''Set configuration values for testing environment'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test-db.sqlite')


class ProdConfig(Config):
    '''Set configuration values for testing environment'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProdConfig,
    'default': DevelopmentConfig
}
