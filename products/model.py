from extensions import db
from dataclasses import dataclass


@dataclass
class Product(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(80), nullable=False)
    price: str = db.Column(db.Float, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)
