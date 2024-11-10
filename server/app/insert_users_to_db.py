from psycopg import Cursor
import pandas as pd
from utils.logger import logger
from db import connection
from common.utils.auth import get_password_hash
from string import ascii_letters
from random import choices
from transliterate import translit


def insert(first_name: str, last_name: str, cursor: Cursor):
    try:
        query = """
        INSERT INTO "user" ("username", "first_name", "last_name", "password_hash", "original_password") 
        VALUES (%(username)s, %(first_name)s, %(last_name)s, %(password_hash)s, %(original_password)s);
        """
        username = translit(f"{last_name}{first_name[0]}", reversed=True)
        password = "".join(choices(ascii_letters, k=10))

        cursor.execute(query, dict(
            username=username,
            first_name=first_name,
            last_name=last_name,
            original_password=password,
            password_hash=get_password_hash(password),
        ))
    except Exception as e:
        print(f"Error inserting {username}: {e}")


def update(username: str, cursor: Cursor):
    try:
        query = """
        UPDATE user SET password=%(password)s, original_password=%(original_password)s WHERE username=%(username)s;
        """
        password = "".join(choices(ascii_letters, k=10))
        cursor.execute(query, {'username': username, 'password': get_password_hash(password), 'original_password': password})
    except Exception as e:
        print(f"Error updating user {username}: {e}")


if __name__ == "__main__":
    cursor = connection.cursor()

    logger.info("Begin inserting users to database")
    df = pd.read_csv('CSS_students.csv', delimiter=';')
    count = 0

    for index, row in df.iterrows():
        if pd.isna(row['Имя']) or pd.isna(row['Фамилия']):
            continue
        
        first_name = row['Имя']
        last_name = row['Фамилия']
        # password = row['Пароль']
        insert(first_name, last_name, cursor)
        # update(username, cursor)
        count += cursor.rowcount

    logger.info(f"Inserted {count} users")

    cursor.close()
    connection.close()
