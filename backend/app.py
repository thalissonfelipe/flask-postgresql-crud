import os
from database.db import db
from dotenv import load_dotenv
from flask import Flask, Response
from blueprints.users import users_blueprint

load_dotenv()  # load env files


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    db.init_app(app)

    app.register_blueprint(users_blueprint)

    @app.errorhandler(404)
    def route_not_found(e):
        response = Response(response='Route not found.', status=404)
        return response

    @app.errorhandler(405)
    def method_not_allowed(e):
        response = Response(response='Method not allowed.', status=405)
        return response

    @app.errorhandler(Exception)
    def internal_error(e):
        response = Response(response='Internal Error.', status=500)
        return response

    return app


app = create_app()
