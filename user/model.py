from server import db
from dataclasses import dataclass


@dataclass
class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(30), nullable=False)
    email: str = db.Column(db.String, nullable=False, unique=True)
    password: str = db.Column(db.String, nullable=False)


def create_user():
    pass


def check_credentials():
    pass
