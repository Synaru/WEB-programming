from flask import Blueprint, render_template, redirect, url_for, request, make_response, session
lab5 = Blueprint('lab5', __name__)

@lab5.route("/lab5/")
def lab5index():
    return render_template("lab5.html")

@lab5.route("/lab5/login")
def login():
    pass

@lab5.route("/lab5/register")
def register():
    pass

@lab5.route("/lab5/list")
def getlist():
    pass

@lab5.route("/lab5/create")
def create():
    pass

























