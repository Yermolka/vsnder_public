from psycopg import connect, Connection, Cursor
from contextlib import contextmanager
from typing import Iterator
import os
from utils.logger import logger


# Maybe change to a small pool?
def get_db_connection() -> Connection:
    connection = connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_DATABASE"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )
    connection.autocommit = True
    return connection

connection = get_db_connection()
logger.info("Connected to database")


@contextmanager
def get_db_cursor(name: str | None = None) -> Iterator[Cursor]:
    global connection

    if connection.closed or connection.broken:
        connection = get_db_connection()

    with connection.transaction(name):
        try:
            if name:
                cursor = connection.cursor(name)
            else:
                cursor = connection.cursor()

            yield cursor
        finally:
            cursor.close()
