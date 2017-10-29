from flask_security.forms import RegisterForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username', [DataRequired(), Length(max=24)])
