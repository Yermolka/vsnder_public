from psycopg import Cursor
import pandas as pd
from utils.logger import logger
from db import connection


def insert(username: str, password: str, cursor: Cursor):
    try:
        query = """
        INSERT INTO users (username, password, original_password) 
        VALUES (%s, crypt(%s, gen_salt('bf')), %s);
        """
        cursor.execute(query, (username, password, password))
    except Exception as e:
        logger.error(f"Error inserting {username}: {e}")


if __name__ == "__main__":
    cursor = connection.cursor()

    logger.info("Begin inserting users to database")
    df = pd.read_csv('VSNTinder_DataBase_csv.csv', delimiter=';')

    for index, row in df.iterrows():
        if not pd.isna(row['Имя']) and not pd.isna(row['Фамилия']):
            username = f"{row['Имя']}_{row['Фамилия']}"
            password = row['Пароль']
            insert(username, password, cursor)

    logger.info(f"Inserted {cursor.rowcount} users")

    cursor.close()
    connection.close()
