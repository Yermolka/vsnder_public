from psycopg import Cursor
import pandas as pd
from utils.logger import logger
from db import connection
from common.utils.auth import get_password_hash
from string import ascii_letters
from random import choices


def insert(username: str, password: str, cursor: Cursor):
    try:
        query = """
        INSERT INTO users (username, password, original_password) 
        VALUES (%s, crypt(%s, gen_salt('bf')), %s);
        """
        cursor.execute(query, (username, password, password))
    except Exception as e:
        print(f"Error inserting {username}: {e}")


def update(username: str, cursor: Cursor):
    try:
        query = """
        UPDATE users SET password=%(password)s, original_password=%(original_password)s WHERE username=%(username)s;
        """
        password = "".join(choices(ascii_letters, k=10))
        cursor.execute(query, {'username': username, 'password': get_password_hash(password), 'original_password': password})
    except Exception as e:
        print(f"Error updating user {username}: {e}")


if __name__ == "__main__":
    cursor = connection.cursor()

    logger.info("Begin inserting users to database")
    df = pd.read_csv('CSS_students.csv', delimiter=';')

    for index, row in df.iterrows():
        if pd.isna(row['Имя']) or pd.isna(row['Фамилия']):
            continue
        
        username = f"{row['Имя']}_{row['Фамилия']}"
        password = row['Пароль']
        # insert(username, password, cursor)
        update(username, cursor)

    logger.info(f"Inserted {cursor.rowcount} users")

    cursor.close()
    connection.close()
