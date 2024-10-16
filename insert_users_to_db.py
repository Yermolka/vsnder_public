import psycopg
from dotenv import load_dotenv
import os
import pandas as pd

def insert(username: str, password: str, cursor):
    try:
        query = """
        INSERT INTO users (username, password, original_password) 
        VALUES (%s, crypt(%s, gen_salt('bf')), %s);
        """
        cursor.execute(query, (username, password, password))
    except Exception as e:
        print(f"Error inserting {username}: {e}")

load_dotenv('db.env')

connection = psycopg.connect(
    host=os.getenv('DB_HOST'), 
    dbname=os.getenv('DB_DATABASE'), 
    user=os.getenv('DB_USER'), 
    password=os.getenv('DB_PASSWORD')
)
connection.autocommit = True
cursor = connection.cursor()

df = pd.read_csv('VSNTinder_DataBase_csv.csv', delimiter=';')

for index, row in df.iterrows():
    if not pd.isna(row['Имя']) and not pd.isna(row['Фамилия']):
        username = f"{row['Имя']}_{row['Фамилия']}"
        password = row['Пароль']
        insert(username, password, cursor)

cursor.close()
connection.close()
