from flask import Blueprint, jsonify, request, session
from .model import create_admin, check_password

admin = Blueprint('admin', __name__)


@admin.post('/login')
def login():
    data = request.json
    email = data.get('email', None)
    password = data.get('password', None)

    if email is None or password is None:
        return jsonify({'success': False}), 401

    session['email'] = email
    session['logged_in'] = True

    return jsonify({'success':True})


@admin.post('/signup')
def signup():
    data = request.json
    print(data)
    username = data.get('username', None)
    email = data.get('email', None)
    password = data.get('password', None)

    if email is None or password is None or username is None:
        return jsonify({'success': False}), 400

    try:
        create_admin(username, email, password)
    except Exception as e:
        print(e)
        return jsonify({'success': False}), 400

    return jsonify({'success': True})

@admin.post('/logout')
def logout():
    session.clear()
    return jsonify({'success': True})

