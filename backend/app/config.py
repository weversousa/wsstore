from os import getenv

from dotenv import load_dotenv


load_dotenv()


def init_app(app):
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
