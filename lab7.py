from flask import Blueprint, render_template, redirect, url_for, request, make_response, session, current_app

lab7 = Blueprint('lab7', __name__)
import random

films = [
    {
        "title": "Inception",
        "title_ru": "Преодоление",
        "year": 2010,
        "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea instead into the mind of a CEO."
    },
    {
        "title": "Interstellar",
        "title_ru": "Космический разлад",
        "year": 2014,
        "description": "A team of astronauts travel through a wormhole in search of a new home for humanity."
    },
    {
        "title": "The Matrix",
        "title_ru": "Матрица",
        "year": 1999,
        "description": "A computer hacker accidentally hooks into the mind of the main character of a simulated reality game."
    },
    {
        "title": "Pulp Fiction",
        "title_ru": "Бешеные пули",
        "year": 1994,
        "description": "The lives of two mob hitmen, a boxer, and a gangster's wife intersect as each prepares to meet his maker."
    },
    {
        "title": "The Shawshank Redemption",
        "title_ru": "Освобождение Ридли Скотта",
        "year": 1994,
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    }
]

@lab7.route("/lab7/")
def lab6index():
    return render_template("lab7.html")

@lab7.route("/lab7/rest-api/films/", methods=['GET'])
def get_films():
    return films

@lab7.route("/lab7/rest-api/films/<int:id>", methods=['GET'])
def get_film(id):
    if id < 0 or id > len(films) - 1:
        return "", 404
    return films[id]

@lab7.route("/lab7/rest-api/films/<int:id>", methods=['DELETE'])
def delete_film(id):
    if id < 0 or id > len(films) - 1:
        return "", 404
    del films[id]
    return '', 204


