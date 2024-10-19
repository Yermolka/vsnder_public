from psycopg import connect, Connection, Cursor
from contextlib import contextmanager
from typing import Iterator
import os
from dotenv import load_dotenv


load_dotenv("db.env", verbose=True)

# Maybe change to a small pool?
def get_db_connection() -> Connection:
    connection = connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_DATABASE"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    connection.autocommit = True
    return connection

connection = get_db_connection()


@contextmanager
def get_db_cursor(name: str | None = None) -> Iterator[Cursor]:
    global connection

    with connection.transaction(name):
        try:
            if name:
                cursor = connection.cursor(name)
            else:
                cursor = connection.cursor()

            yield cursor
        finally:
            cursor.close()
