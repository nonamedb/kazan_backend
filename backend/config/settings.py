# coding: utf-8


testing = False


DATABASE = dict(
    user='user',
    password='password',
    host='host',
    port='port',
    dbname='dbname',
    driver='postgresql+psycopg2',
)


VK_TOKEN = ''


try:
    from .local import *
except ModuleNotFoundError as exc:
    pass
