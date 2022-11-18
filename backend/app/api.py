from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError

from app.database import db
from app.model import User



api = Blueprint('api', __name__, url_prefix='/api')


def init_app(app):
    app.register_blueprint(api)


@api.route('/users', methods=['post'])
def create_user():
    data = request.get_json()
    email, password = data.get('email'), data.get('password')

    if email == None or password == None:
        return {'error': 'Parâmetros incorretos.'}

    user = User(email=data['email'], password=data['password'])
    db.session.add(user)

    try:
        db.session.commit()
        return {'id': user.id, 'email': user.email, 'password': user.password}

    except IntegrityError:
        return {'error': 'Usuário já existe.'}


@api.route('/users', methods=['get'])
def read_user():
    id = request.args.get('id')

    if id:
        try:
            id = int(id)

        except ValueError:
            return {'error': 'ID incorreto.'}

        user = User.query.get(id)
        if not user:
            return {'error': 'Usuário não existe.'}

        return {'id': user.id, 'email': user.email, 'password': user.password}

    users = []
    for user in User.query.all():
        user = {'id': user.id, 'email': user.email, 'password': user.password}
        users.append(user)

    return users


@api.route('/users', methods=['put'])
def update_user():
    id = request.args.get('id')

    try:
        id = int(id)

    except ValueError:
        return {'error': 'ID incorreto.'}

    user = User.query.get(id)
    if not user:
        return {'error': 'Usuário não existe.'}

    data = request.get_json()
    email, password = data.get('email'), data.get('password')

    if email == None or password == None:
        return {'error': 'Parâmetros incorretos.'}

    user.email = email
    user.password = password

    try:
        db.session.commit()
        return {'id': user.id, 'email': user.email, 'password': user.password}

    except IntegrityError:
        return {'error': 'Usuário já existe.'}


@api.route('/users', methods=['path'])
def update_user_password():
    id = request.args.get('id')

    try:
        id = int(id)

    except ValueError:
        return {'error': 'ID incorreto.'}

    user = User.query.get(id)
    if not user:
            return {'error': 'Usuário não existe.'}

    data = request.get_json()
    password = data.get('password')

    if not isinstance(password, bool):
        return {'error': 'Parâmetro inválido.'}

    user.password = password

    try:
        db.session.commit()
        return {'id': user.id, 'email': user.email, 'password': user.password}

    except IntegrityError:
        return {'error': 'Usuário já existe.'}


@api.route('/users', methods=['delete'])
def delete_user():
    id = request.args.get('id')

    try:
        id = int(id)

    except ValueError:
        return {'error': 'ID incorreto.'}

    user = User.query.get(id)
    if not user:
            return {'error': 'Usuário não existe.'}

    db.session.delete(user)
    db.session.commit()
    return {'id': user.id, 'email': user.email, 'password': user.password}
