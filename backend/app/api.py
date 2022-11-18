from flask import Blueprint

from app.model import User


api = Blueprint('api', __name__, url_prefix='/api')


def init_app(app):
    app.register_blueprint(api)


@api.route('/users')
def home():
    User(email='email@hotmail.com', password='1234').save()
    return 'Ok'
