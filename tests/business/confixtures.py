# coding: utf-8


import pytest
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base
from application import init_app
from backend.models.base import db
from backend.utils import get_session, get_engine


@pytest.fixture(scope='session', autouse=True)
def database():
    db.create_all(app=init_app())


@pytest.fixture(scope='session')
def session():
    session = get_session()
    yield session
    session.close()
