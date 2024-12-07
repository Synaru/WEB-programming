from flask import Blueprint, render_template, redirect, url_for, request, make_response, session, current_app
from werkzeug.security import check_password_hash, generate_password_hash

lab5 = Blueprint('lab5', __name__)
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path

@lab5.route("/lab5/")
def lab5index():
    return render_template("lab5.html", name=session.get('login'), db=current_app.config['DB_TYPE'])


@lab5.route("/lab5/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login_lab5.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('login_lab5.html', error="Заполните все поля")

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login = $s;", (login,))
    else:
        cur.execute("SELECT * FROM users WHERE login = ?;", (login,))

    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('login_lab5.html', error="Логин и\или пароль не верны")

    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('login_lab5.html', error="Логин и\или пароль не верны")

    session['login'] = login
    db_close(conn, cur)
    return render_template('login_succ.html', login=login)


@lab5.route("/lab5/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register_lab5.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('register_lab5.html', error="Заполните все поля")

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users WHERE login=$s;", (login,))
    else:
        cur.execute("SELECT login FROM users WHERE login=?;", (login,))

    if cur.fetchone():
        db_close(conn, cur)

        return render_template('register_lab5.html', error="Такой пользователь уже есть")

    password_hash = generate_password_hash(password)
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO users (login, password) VALUES ($s,$s);", (login, password_hash))
    else:
        cur.execute("INSERT INTO users (login, password) VALUES (?,?);", (login, password_hash))

    db_close(conn, cur)
    return render_template('register_succ.html')


@lab5.route("/lab5/list")
def getlist():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=$s;", (login, ))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (login, ))

    login_id = cur.fetchone()["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM articles WHERE user_id=$s;", (login_id, ))
    else:
        cur.execute("SELECT * FROM articles WHERE login_id=?;", (login_id, ))
    articles = cur.fetchall()
    db_close(conn, cur)

    return render_template('lab5_articles.html', articles=articles)


@lab5.route("/lab5/create", methods=['GET', 'POST'])
def create():
    login=session.get('login')
    if not login:
        return redirect('/lab5/login')

    if request.method == 'GET':
        return render_template('lab5_create_article.html')

    title = request.form.get('title')
    article = request.form.get('article')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=$s;", (login, ))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (login, ))

    login_id = cur.fetchone()["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES ($s,$s,$s);", (login_id, title, article))
    else:
        cur.execute("INSERT INTO articles (login_id, title, article_text) VALUES (?,?,?);", (login_id, title, article))

    db_close(conn, cur)
    return redirect('/lab5')

def db_connect():

    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            port='7400',
            database='synaru',
            user='synaru',
            password='synaru'
        )
        cur = conn.cursor(cursor_factory = RealDictCursor)
    else:
        dir_path = path.dirname(path.relpath(__file__))
        db_path = path.join(dir_path, 'database.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(connection, cursor):
    connection.commit()
    cursor.close()
    connection.close()
