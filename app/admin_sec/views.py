from flask_admin.contrib.sqla import ModelView

from .. import admin
from .. import db
from ..models import User, Role, Challenge, Tag

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Challenge, db.session))
admin.add_view(ModelView(Tag, db.session))
