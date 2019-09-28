# coding: utf-8


import logging
import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from config import settings
from backend.utils.database import get_engine_url
from backend.utils.json import CustomJSONEncoder
from backend.urls import route
from backend.models.base import db


def init_app():
    __setup_logging()

    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder

    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', get_engine_url())
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    route(app=app)

    app.app_context().push()

    db.init_app(app)
    Migrate(app=app, db=db)
    db.create_all()

    return app


def __setup_logging():
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
    )


if __name__ == '__main__':
    app = init_app()
    app.run('0.0.0.0', port=8080)
