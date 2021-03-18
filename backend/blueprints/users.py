from models.models import User
from flask import Blueprint, jsonify


users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/', methods=['GET'])
def index():
    users = User.query.all()

    return jsonify([user.serialize() for user in users])
