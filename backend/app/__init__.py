from flask import Flask

from app import config, database, cli, api


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    database.init_app(app)
    cli.init_app(app)
    api.init_app(app)
    return app
