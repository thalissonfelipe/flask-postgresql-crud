from flask import request
from functools import wraps
from werkzeug.exceptions import BadRequest
from utils.errors import BadRequestException
from utils.validator import validate_create_body, validate_update_body


def validate_json(ignore_methods=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if ignore_methods is not None:
                for method in ignore_methods:
                    if request.method == method:
                        return f(*args, **kwargs)
            try:
                data = request.get_json()
                if data is None:
                    raise BadRequest
            except BadRequest:
                raise BadRequestException('Invalid JSON.')
            if request.method == 'POST':
                validate_create_body(data)
            if request.method == 'PUT':
                validate_update_body(data)
            return f(*args, **kwargs)
        return wrapper
    return decorator
