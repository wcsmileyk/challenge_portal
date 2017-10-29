from datetime import datetime

from flask_security import RoleMixin, UserMixin

from . import db


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer())

    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    github = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    location = db.Column(db.String(64))

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    submissions = db.relationship('Submission', backref='submitter', lazy='dynamic')


class Challenge(db.Model):
    __tablename__ = 'challenges'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True)


class Submission(db.Model):
    __tablename__ = 'submissions'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    submitter_id = db.Column(db.Integer, db.ForeignKey('users.id'))

