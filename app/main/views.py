from flask import render_template, url_for

from . import main
from ..models import Challenge


@main.route('/')
def index():

    current_challenge = Challenge.query.order_by(Challenge.timestamp.desc()).first()
    past_challenges = Challenge.query.order_by(Challenge.timestamp.desc()).offset(1).all()

    return render_template('index.html', current_challenge=current_challenge, past_challenges=past_challenges)


@main.route('/<user>')
def profile(user):
    pass
