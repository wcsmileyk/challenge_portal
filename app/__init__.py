from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin import Admin
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
security = Security()
admin = Admin(name='python challenges', template_mode='bootstrap3')


def create_app(config_name):
    '''
    Creates the app at run time, allowing the loading of correct configuration settings
    :param config_name: Runtime Config
    :return: Running Flask app
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from .models import User, Role

    # Initialize Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    # Initialize Flask-Admin
    admin.init_app(app)

    # Blueprint registrations go here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin_sec import admin_sec as admin_blueprint
    # app.register_blueprint(admin_blueprint)

    return app

