from database.db import db
from models.models import User
from flask import Blueprint, request
from utils.decorators import validate_json
from utils.http import ok, created, no_content, not_found
from database.helper import get_users, create_user, update_user, delete_user


users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users/<id>/', methods=['GET', 'PUT', 'DELETE'])
@validate_json(ignore_methods=['GET', 'DELETE'])
def user(id):
    user_exists = User.query.get(id)
    if user_exists is None:
        return not_found('user')

    if request.method == 'GET':
        return ok(user_exists)

    if request.method == 'PUT':
        body = request.get_json()
        update_user(db, user_exists, body)
        return no_content()

    if request.method == 'DELETE':
        delete_user(db, user_exists)
        return no_content()


@users_blueprint.route('/users/', methods=['GET', 'POST'])
@validate_json(ignore_methods=['GET'])
def users():
    if request.method == 'GET':
        users = get_users(request)
        return ok(users)

    if request.method == 'POST':
        body = request.get_json()
        user = create_user(db, body)
        return created(user)
