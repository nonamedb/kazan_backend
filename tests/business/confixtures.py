# coding: utf-8


import pytest
from backend.models.base import Base
from backend.utils import get_session, get_engine


@pytest.fixture(scope='session', autouse=True)
def database():
    Base.metadata.create_all(get_engine())


@pytest.fixture(scope='session')
def session():
    session = get_session()
    yield session
    session.close()
