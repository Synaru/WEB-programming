from flask import Flask, render_template, redirect
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5

import os

app = Flask(__name__, template_folder='templates')
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)

app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')
app.config['DB_TYPE'] = os.environ.get('DB_TYPE', 'postgres')

app.secret_key = 'fnbhui3o27gf8o72379fgbh23gb8er02390hre028723h22'

@app.route("/")
def root():
    return redirect("/menu", code=302)


@app.route("/menu")
def renderMenu():
    return render_template("menu.html")


@app.route("/lab3")
def renderLab3():
    return render_template("lab3.html")

if __name__ == '__main__':
    app.run(debug=True)
