from flask import Blueprint, session, jsonify

user = Blueprint('user', __name__)


@user.post('/login')
def login():
    pass


@user.post('/signup')
def signup():
    pass


@user.post('/logout')
def logout():
    pass

