import os
from flask import Flask
from database.db import db
from dotenv import load_dotenv
from blueprints.users import users_blueprint

load_dotenv()  # load env files


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    db.init_app(app)

    app.register_blueprint(users_blueprint)

    return app


app = create_app()
