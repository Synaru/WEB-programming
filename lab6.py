from flask import Blueprint, render_template, redirect, url_for, request, make_response, session, current_app
from werkzeug.security import check_password_hash, generate_password_hash

lab6 = Blueprint('lab6', __name__)
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path

@lab6.route("/lab6/")
def lab6index():
    return render_template("lab6.html")
