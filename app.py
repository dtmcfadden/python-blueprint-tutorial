from blueprints.about.views import about
from blueprints.contact.views import contact
from blueprints.products.views import product
from blueprints.main.views import main
import os
from dotenv import load_dotenv
from flask import Flask
from extensions import database, commands


# blueprint import


def create_app():
    load_dotenv()

    app = Flask(__name__)
    # setup with the configuration provided by the user / environment
    app.config.from_object(os.getenv('APP_SETTINGS'))

    # setup all our dependencies
    database.init_app(app)
    commands.init_app(app)

    # register blueprint
    app.register_blueprint(main)
    app.register_blueprint(product)
    app.register_blueprint(contact)
    app.register_blueprint(about)

    return app


if __name__ == "__main__":
    create_app().run()
