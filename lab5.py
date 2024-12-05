from flask import Blueprint, render_template, redirect, url_for, request, make_response, session

lab5 = Blueprint('lab5', __name__)
import psycopg2


@lab5.route("/lab5/")
def lab5index():
    return render_template("lab5.html")


@lab5.route("/lab5/login")
def login():
    pass


@lab5.route("/lab5/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register_lab5.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('register_lab5.html', error="Заполните все поля")

    conn = psycopg2.connect(
        host='127.0.0.1',
        port='7400',
        database='synaru',
        user='synaru',
        password='synaru'
    )
    cur = conn.cursor()

    cur.execute(f"SELECT login FROM users WHERE login='${login}';")

    if cur.fetchone():
        cur.close()
        conn.close()
        return render_template('register_lab5.html', error="Такой пользователь уже есть")

    cur.execute(f"INSERT INTO users (login, password) VALUES ('{login}','{password}');")
    conn.commit()
    cur.close()
    conn.close()
    return render_template('register_succ.html')


@lab5.route("/lab5/list")
def getlist():
    pass


@lab5.route("/lab5/create")
def create():
    pass
