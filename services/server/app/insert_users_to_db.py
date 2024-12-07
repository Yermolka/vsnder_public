import asyncio
from psycopg import AsyncCursor
import pandas as pd
from utils.logger import logger
from db import pg_pool, open_pg_pool, close_pg_pool
from common.utils.auth import get_password_hash
from string import ascii_letters
from random import choices


async def insert(first_name: str, last_name: str, year: int, cursor: AsyncCursor):
    try:
        query = """
        INSERT INTO "user" ("username", "first_name", "last_name", "password_hash", "original_password", "year_of_study") 
        VALUES (%(username)s, %(first_name)s, %(last_name)s, %(password_hash)s, %(original_password)s, %(year_of_study)s);
        """
        username = f"{last_name}{first_name[0]}"
        password = "".join(choices(ascii_letters, k=10))

        await cursor.execute(
            query,
            dict(
                username=username,
                first_name=first_name,
                last_name=last_name,
                original_password=password,
                password_hash=get_password_hash(password),
                year_of_study=year,
            ),
        )
    except Exception as e:
        print(f"Error inserting {username}: {e}")

async def insert_test(first_name: str, last_name: str, year: int, cursor: AsyncCursor):
    try:
        query = """
        INSERT INTO "user" ("username", "first_name", "last_name", "password_hash", "original_password", "year_of_study") 
        VALUES (%(username)s, %(first_name)s, %(last_name)s, %(password_hash)s, %(original_password)s, %(year_of_study)s);
        """
        username = f"{last_name}{first_name[0]}"
        password = "12345678"

        await cursor.execute(
            query,
            dict(
                username=username,
                first_name=first_name,
                last_name=last_name,
                original_password=password,
                password_hash=get_password_hash(password),
                year_of_study=year,
            ),
        )
    except Exception as e:
        print(f"Error inserting {username}: {e}")


async def update(username: str, cursor: AsyncCursor):
    try:
        query = """
        UPDATE "user" SET password=%(password)s, original_password=%(original_password)s WHERE username=%(username)s;
        """
        password = "".join(choices(ascii_letters, k=10))
        await cursor.execute(
            query,
            {
                "username": username,
                "password": get_password_hash(password),
                "original_password": password,
            },
        )
    except Exception as e:
        print(f"Error updating user {username}: {e}")


async def update_year_of_study(
    first_name: str, last_name: str, year: int, cursor: AsyncCursor
):
    try:
        query = """
        UPDATE "user" SET year_of_study=%(year_of_study)s WHERE first_name=%(first_name)s AND last_name=%(last_name)s;
        """
        await cursor.execute(
            query,
            {"first_name": first_name, "last_name": last_name, "year_of_study": year},
        )
    except Exception as e:
        print(f"Error updating user {first_name} {last_name}: {e}")


async def update_username_to_ru(first_name: str, last_name: str, cursor: AsyncCursor):
    try:
        query = """
        UPDATE "user" SET username=%(username)s WHERE first_name=%(first_name)s AND last_name=%(last_name)s;
        """
        username = f"{last_name}{first_name[0]}"
        await cursor.execute(
            query,
            {"first_name": first_name, "last_name": last_name, "username": username},
        )
    except Exception as e:
        print(f"Error updating user {first_name} {last_name}: {e}")


async def main():
    await open_pg_pool(None)

    async with pg_pool.connection() as connection:
        async with connection.cursor() as cursor:
            count = 0

            logger.info("Begin inserting users to database")
            df = pd.read_csv("CSS_students.csv", delimiter=";")
            for index, row in df.iterrows():
                if pd.isna(row["Имя"]) or pd.isna(row["Фамилия"]):
                    continue

                first_name = row["Имя"]
                last_name = row["Фамилия"]
                year_of_study = row["Курс"]
                # await update_username_to_ru(first_name, last_name, cursor)
                await insert_test(first_name, last_name, year_of_study, cursor)
                count += cursor.rowcount
            
            logger.info(f"Inserted {count} users")

    await close_pg_pool(None)


if __name__ == "__main__":
    asyncio.run(main())
