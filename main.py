from flask import Flask, render_template, request, redirect, url_for, flash
from flask_httpauth import HTTPBasicAuth
import psycopg
from psycopg import OperationalError
from dotenv import load_dotenv
import os

load_dotenv('db.env')
secret_key = os.get
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'aboba')

def get_db_connection():
    try:
        connection = psycopg.connect(
            host=os.getenv('DB_HOST'),
            dbname=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        connection.autocommit = True
        return connection
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None

connection = get_db_connection()
cur = connection.cursor() if connection else None

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    try:
        cur.execute("SELECT password = crypt(%s, password) AS password_matches FROM users WHERE username = %s", (password, username))
        row = cur.fetchone()
        if row is not None:
            return row[0]
    except (OperationalError, psycopg.errors.DatabaseError):
        reconnect_to_db()
        return verify_password(username, password)
    return False

def reconnect_to_db():
    global connection, cur
    connection = get_db_connection()
    if connection:
        cur = connection.cursor()

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    if request.method == 'POST':
        data = {
            'age': request.form['age'],
            'orientation': request.form['orientation'],
            'interests': request.form['interests'],
            'vsn_interests': request.form['vsn_interests'],
            'places_to_visit': request.form['places_to_visit'],
            'study_places': request.form['study_places'],
            'music': request.form['music'],
            'favorite_movies': request.form['favorite_movies'],
            'religion': request.form['religion'],
            'status': request.form['status'],
            'future_plans': request.form['future_plans'],
            'family_opinion': request.form['family_opinion'],
            'favorite_programming_language': request.form['favorite_programming_language'],
            'lizards_or_russians': request.form.get('lizards_or_russians') == 'on',
            'smoking': request.form['smoking'],
            'top_3_people': request.form['top_3_people'],
            'drinking': request.form['drinking']
        }
        try:
            cur.execute("""
                UPDATE users SET 
                    age = %(age)s,
                    orientation = %(orientation)s,
                    interests = %(interests)s,
                    vsn_interests = %(vsn_interests)s,
                    places_to_visit = %(places_to_visit)s,
                    study_places = %(study_places)s,
                    music = %(music)s,
                    favorite_movies = %(favorite_movies)s,
                    religion = %(religion)s,
                    status = %(status)s,
                    future_plans = %(future_plans)s,
                    family_opinion = %(family_opinion)s,
                    favorite_programming_language = %(favorite_programming_language)s,
                    smoking = %(smoking)s,
                    top_3_people = %(top_3_people)s,
                    drinking = %(drinking)s
                WHERE username = %(username)s
            """, {**data, 'username': auth.username()})
            flash('Информация успешно обновлена!')
        except (OperationalError, psycopg.errors.DatabaseError):
            reconnect_to_db()
            return index()
    try:
        cur.execute("""
            SELECT 
                age, orientation, interests, vsn_interests, places_to_visit, study_places, music, favorite_movies, religion, status, future_plans, family_opinion, favorite_programming_language, lizards_or_russians, smoking, top_3_people, drinking
            FROM users 
            WHERE username = %s
        """, (auth.username(),))
        user_info = cur.fetchone()
        return render_template('index.html', user_info=user_info)
    except (OperationalError, psycopg.errors.DatabaseError):
        reconnect_to_db()
        return index()

@app.route('/change_password', methods=['GET', 'POST'])
@auth.login_required
def change_password():
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        if new_password != confirm_password:
            flash('New passwords do not match!')
            return redirect(url_for('change_password'))
        
        try:
            cur.execute("SELECT password = crypt(%s, password) AS password_matches FROM users WHERE username = %s", (old_password, auth.username()))
            row = cur.fetchone()
            if row and row[0]:
                cur.execute("UPDATE users SET password = crypt(%s, gen_salt('bf')) WHERE username = %s", (new_password, auth.username()))
                flash('Пароль успешно изменен!')
            else:
                flash('Old password is incorrect!')
        except (OperationalError, psycopg.errors.DatabaseError):
            reconnect_to_db()
            return change_password()
        
        return redirect(url_for('index'))
    
    return render_template('change_password.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
