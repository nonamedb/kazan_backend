# coding: utf-8


import datetime


from flask import abort, g
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, out):
        if isinstance(out, (datetime.date, datetime.datetime)):
            return out.isoformat()
        return super().default(out)
