from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config_option

bootstrap = Bootstrap()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_option[config_name])
    app.config.from_pyfile('api_config.py')
    bootstrap.init_app(app)
    moment.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .requests import configure_request
    configure_request(app)

    return app
