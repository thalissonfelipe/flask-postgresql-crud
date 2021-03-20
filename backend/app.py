import os
from flask import Flask
from database.db import db
from flask_cors import CORS
from dotenv import load_dotenv
from utils.errors import BadRequestException
from blueprints.users import users_blueprint
from utils.http import bad_request, not_found, not_allowed, internal_error

load_dotenv()  # load env files


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    app.url_map.strict_slashes = False
    db.init_app(app)
    CORS(app)

    app.register_blueprint(users_blueprint, url_prefix='/api/v1')

    @app.errorhandler(BadRequestException)
    def bad_request_exception(e):
        return bad_request(e)

    @app.errorhandler(404)
    def route_not_found(e):
        return not_found('route')

    @app.errorhandler(405)
    def method_not_allowed(e):
        return not_allowed()

    @app.errorhandler(Exception)
    def internal_server_error(e):
        return internal_error()

    return app


app = create_app()
