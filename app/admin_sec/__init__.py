from flask import Blueprint

admin_sec = Blueprint('admin_sec', __name__)

from . import views