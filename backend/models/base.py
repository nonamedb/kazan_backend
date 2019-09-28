# coding: utf-8


from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy.ext.declarative import declarative_base


class _Query(BaseQuery):  # out of the box it can `get_or_404` only
    def one_or_abort(self, http_status):
        obj = self.one_or_none()
        if obj is None:
            abort(http_status)
        return obj

    def one_or_404(self):
        return self.one_or_abort(http_status=404)


db = SQLAlchemy(query_class=_Query)


class BaseModel(db.Model):
    __abstract__ = True

    def marshall(self) -> dict:
        raise NotImplementedError

