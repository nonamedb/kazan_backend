# coding: utf-8


import functools
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from config.settings import DATABASE, testing


def get_engine() -> Engine:
    if DATABASE['driver'] in ('sqlite',):
        engine_url = '%(driver)s://%(dbname)s' % DATABASE
    else:
        engine_url = '%(driver)s://%(user)s:%(password)s@%(host)s:%(port)s/%(dbname)s' % DATABASE
    return create_engine(engine_url, echo=False)


def get_session() -> Session:
    return Session(bind=get_engine(), autoflush=False)


def use_session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = list(args)
        session = get_session()
        args.insert(1, session)
        try:
            res = func(*args, **kwargs)
            session.commit()
            return res
        except (SQLAlchemyError, ) as exc:
            session.rollback()
        finally:
            session.close()
    return wrapper
