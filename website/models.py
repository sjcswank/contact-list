from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))
    contacts = db.relationship('Contact')


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    address = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))