from flask import Flask
from extensions import db
from flask_bcrypt import Bcrypt
from products import product
from products.model import Product

bcrypt = None
def create_app():
    app = Flask(__name__)

    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project1.db"
    app.register_blueprint(product, url_prefix='/product')

    app.config.update(
        TESTING=True,
        SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    )

    # initialize the app with the extension
    db.init_app(app)

    bcrypt = Bcrypt(app)

    with app.app_context():
        db.create_all()
    return app
