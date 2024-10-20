from flask import Blueprint, render_template, redirect, url_for
lab1 = Blueprint('lab1', __name__)

@lab1.route("/lab1")
def renderLab1():
    return render_template("lab1.html")


@lab1.route("/lab1/oak")
def renderOak():
    return render_template("oak.html")


@lab1.route("/lab1/student")
def renderStudent():
    return render_template("student.html")


@lab1.route("/lab1/python")
def renderPython():
    return render_template("python.html")


@lab1.route("/lab1/mycat")
def renderCat():
    return render_template("cats.html")


