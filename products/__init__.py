from extensions import db
from flask import Blueprint, jsonify

product = Blueprint('product', __name__)

# get all the products
@product.get('/')
def get_all_products():
    products = [
        {'id':'1', 'name': 'chair', 'price': 23, 'quantity': 20},
        {'id':'2', 'name': 'sofa', 'price': 150, 'quantity': 3},
        {'id':'3', 'name': 'tables', 'price': 80, 'quantity': 2},
        {'id':'4', 'name': 'book shelf', 'price': 100, 'quantity': 1}
    ]
    return jsonify(products)


# create a product

# delete a product

# edit a product