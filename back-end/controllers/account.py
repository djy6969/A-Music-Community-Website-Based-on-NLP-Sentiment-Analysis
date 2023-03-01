import functools

from flask import Blueprint


account = Blueprint('account', __name__)

@account.route("/login")
def login():
    return "login page!"


@account.route("/register")
def register():
    return "register page!"
