# coding: utf-8
# use flask-sqlalcodegen to help generate the models easier
from app import db


class TUser(db.Model):
    __tablename__ = 't_user'

    id = db.Column(db.SmallInteger, primary_key=True)
    username = db.Column(db.String(32, 'utf8_bin'), nullable=False, unique=True)
    password = db.Column(db.String(32, 'utf8_bin'), nullable=False)
    password_salt = db.Column(db.String(32, 'utf8_bin'))
    email = db.Column(db.String(32, 'utf8_bin'))
    tel = db.Column(db.String(11, 'utf8_bin'))
    nickname = db.Column(db.String(32, 'utf8_bin'), nullable=False)
    created_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, server_default=db.FetchedValue())
