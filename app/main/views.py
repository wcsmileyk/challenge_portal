from flask import render_template, url_for, request, current_app
from flask_security import current_user, login_required

from . import main
from ..models import Challenge, User
from ..hash_utils import decode_hashid


def get_challenge(challenge_id):
    challenge = Challenge.query.filter_by(id=challenge_id).first()
    return challenge


def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


@main.route('/')
def index():
    current_challenge = Challenge.query.order_by(Challenge.timestamp.desc()).first()
    page = request.args.get('page', 1, type=int)
    pagination = Challenge.query.order_by(Challenge.timestamp.desc()).paginate(page, per_page=5, error_out=False)
    past_challenges = pagination.items

    return render_template('index.html', current_challenge=current_challenge, past_challenges=past_challenges, pagination=pagination)


@main.route('/<challenge_id>')
def challenge_detailed(challenge_id):
    challenge = get_challenge(challenge_id)

    return render_template('challenge.html', challenge=challenge)


@main.route('/profile/<string:hashid>')
@login_required
def profile(hashid):
    user_id = decode_hashid(hashid)
    user = get_user(user_id)

    return render_template('profile.html', user=user)


@main.route('/submissions/<string:hashid>')
@login_required
def user_submissions(hashid):
    user_id = decode_hashid(hashid)
    user = get_user(user_id)

    return render_template('user_submissions.html', user=user)


@main.route('/submit/<challenge_id>/<string:hashid>', methods=['GET', 'POST'])
@login_required
def submit_challenge(challenge_id, hashid):
    user_id = decode_hashid(hashid)

    challenge = get_challenge(challenge_id)
    user = get_user(user_id)

    return render_template('submit.html', user=user, challenge=challenge)


@main.route('/edit_profile/<string:hashid>')
@login_required
def edit_profile(hashid):
    user_id = decode_hashid(hashid)
    user = get_user(user_id)

    return render_template('edit_profile.html', user=user)

