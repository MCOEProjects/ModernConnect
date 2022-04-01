import pymysql
from contextlib2 import contextmanager

from config import database, database_password, database_username, hostname


@contextmanager
def connection():
    con = pymysql.connect(user=database_username, password=database_password, host=hostname, database=database)
    try:
        yield con
    finally:
        con.close()
