from flask import Flask, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask_admin import Admin, helpers as admin_helpers
from flask_mail import Mail

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
security = Security()
admin = Admin(name='python challenges', template_mode='bootstrap3')
mail = Mail()


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
    mail.init_app(app)

    from .models import User, Role

    # Initialize Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    # This is an ugly fix to an issue in Flask-Security with state changes using Factory Model
    security._state = security.init_app(app, user_datastore)

    # Initialize Flask-Admin
    admin.init_app(app)

    # Blueprint registrations go here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin_sec import admin_sec as admin_blueprint
    app.register_blueprint(admin_blueprint)

    # TODO: This seems to have change login url to admin/login - which I don't want.
    # Use Flask-Admin style for security
    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
            get_url=url_for
        )

    return app

