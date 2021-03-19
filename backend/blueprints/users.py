from database.db import db
from models.models import User, Address
from flask import Blueprint, jsonify, request, Response


users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users/<id>', methods=['GET', 'DELETE'])
def user(id):
    user_exists = User.query.get(id)
    if user_exists is None:
        response = Response(response='User not found.', status=404)
        return response
    if request.method == 'GET':
        return jsonify(user_exists.serialize())
    elif request.method == 'DELETE':
        db.session.delete(user_exists)
        db.session.commit()
        response = Response(status=204)
        return response


@users_blueprint.route('/users', methods=['GET', 'POST'])
def users():
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
    if request.method == 'POST':
        body = request.get_json()
        user = User(body['name'], body['age'])
        db.session.add(user)
        db.session.commit()
        address = Address(
            body['address']['street'],
            body['address']['number'],
            body['address']['city'],
            body['address']['state'],
            user.id
        )
        db.session.add(address)
        db.session.commit()

        return jsonify(user.serialize()), 201
