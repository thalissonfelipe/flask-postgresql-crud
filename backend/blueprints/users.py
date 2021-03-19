from models.models import User
from flask import Blueprint, jsonify, request


users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users', methods=['GET'])
def index():
    if request.method == 'GET':
        limit = request.args.get('limit', None)
        order_by = request.args.get('order_by', None)
        filter_obj = {}

        for key in request.args:
            if key not in ['limit', 'order_by']:
                filter_obj[key] = request.args[key]

        users = User.query \
                    .filter_by(**filter_obj) \
                    .order_by(order_by) \
                    .limit(limit) \
                    .all()

        return jsonify([user.serialize() for user in users])
