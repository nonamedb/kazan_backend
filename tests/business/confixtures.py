# coding: utf-8


import pytest
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base
from backend.models.base import db
from backend.utils import get_session, get_engine


@pytest.fixture(scope='session', autouse=True)
def database():
    Base = declarative_base()
    Base.metadata.create_all(get_engine())


@pytest.fixture(scope='session')
def session():
    session = get_session()
    yield session
    session.close()
