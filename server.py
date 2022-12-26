from flask import Flask
from extensions import db
from products import product
from admin import admin
from flask_cors import CORS
from products.model import Product
from admin.model import Admin


def create_app():
    app = Flask(__name__)

    # configure the SQLite database, relative to the app instance folder
    app.register_blueprint(product, url_prefix='/product')
    app.register_blueprint(admin, url_prefix='/admin')
    app.config.from_object('config')

    # initialize the app with the extension
    db.init_app(app)

    #cors
    CORS(app,supports_credentials=True)

    with app.app_context():
        db.create_all()
    return app
