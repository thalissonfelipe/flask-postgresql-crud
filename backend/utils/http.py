from models.models import User
from flask import Response, jsonify


def ok(resource):
    if isinstance(resource, User):
        return jsonify(resource.serialize())
    return jsonify([res.serialize() for res in resource])


def no_content():
    return Response(status=204)


def created(model):
    return jsonify(model.serialize()), 201


def not_found(resource):
    return Response(response=f'{resource} not found.'.capitalize(), status=404)


def not_allowed():
    return Response(response='Method not allowed.', status=405)


def internal_error():
    return Response(response='Internal Error.', status=500)
