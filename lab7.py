from flask import Blueprint, render_template, redirect, url_for, request, make_response, session, current_app

lab7 = Blueprint('lab7', __name__)
import random

@lab7.route("/lab7/")
def lab6index():
    return render_template("lab7.html")


