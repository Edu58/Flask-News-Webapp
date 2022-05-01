from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_option

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_option[config_name])
    bootstrap.init_app(app)

    from .main import main
    app.register_blueprint(main)

    return app
