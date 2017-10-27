from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
security = Security()


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

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    # Blueprint registrations go here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

