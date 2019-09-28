# coding: utf-8


from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    def marshall(self) -> dict:
        raise NotImplementedError

