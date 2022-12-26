from server import db
from dataclasses import dataclass
import bcrypt


@dataclass
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(30), nullable=False)
    email: str = db.Column(db.String, nullable=False, unique=True)
    password: str = db.Column(db.String, nullable=False)


def create_admin(username, email, password):
    password = password.encode('utf8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(10))
    admin = Admin(username=username, email=email, password=hashed_password)
    db.session.add(admin)
    db.session.commit()


def check_password(email, candidate_password):
    admin = Admin.query.filter_by(email=email).first()
    if admin is None:
        return False
    candidate_password = candidate_password.encode('utf8')
    is_correct_password = bcrypt.checkpw(candidate_password, admin.password)

    return is_correct_password





