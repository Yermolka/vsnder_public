from psycopg import AsyncConnection, AsyncCursor, IsolationLevel
from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
import os
from utils.logger import logger

YOYO_CONN_STR = f"postgresql+psycopg://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:5432/{os.environ["DB_DATABASE"]}"

POOL_MIN_CONNS = 5
POOL_MAX_CONNS = 25


async def reset_conn(conn: AsyncConnection):
    if conn.isolation_level != IsolationLevel.READ_COMMITTED:
        await conn.set_isolation_level(IsolationLevel.READ_COMMITTED)


pg_pool = AsyncConnectionPool(
    f"postgresql://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:5432/{os.environ["DB_DATABASE"]}",
    open=False,
    reset=reset_conn,
    min_size=POOL_MIN_CONNS,
    max_size=POOL_MAX_CONNS,
    kwargs={"row_factory": dict_row},
)


async def open_pg_pool(_app):
    await pg_pool.open()
    await pg_pool.wait()
    logger.info("Connected to database")


async def close_pg_pool(_app):
    await pg_pool.close()


@asynccontextmanager
async def get_db_cursor(name: str | None = None) -> AsyncGenerator[AsyncCursor, Any]:
    async with pg_pool.connection() as conn:
        if conn.autocommit is False:
            await conn.set_autocommit(True)

        async with conn.transaction(name):
            try:
                if name:
                    cursor = conn.cursor(name)
                else:
                    cursor = conn.cursor()

                yield cursor
            finally:
                await cursor.close()
