from flask import render_template, url_for, request, current_app

from . import main
from ..models import Challenge


@main.route('/')
def index():
    current_challenge = Challenge.query.order_by(Challenge.timestamp.desc()).first()
    page = request.args.get('page', 1, type=int)
    pagination = Challenge.query.order_by(Challenge.timestamp.desc()).paginate(page, per_page=5, error_out=False)
    past_challenges = pagination.items

    return render_template('index.html', current_challenge=current_challenge, past_challenges=past_challenges, pagination=pagination)


@main.route('/<challenge>')
def challenge_detailed(challenge):
    # current_challenge = Challenge.query.filter_by(id=challenge).first()
    return render_template('challenge.html')


@main.route('/<user>')
def profile(user):
    pass
