from flask import Blueprint, render_template, redirect, url_for
lab2 = Blueprint('lab2', __name__)

@lab2.route("/lab2/")
def renderLab2():
    return render_template("lab2.html")

flower_list = ['Ромашка', 'Одуванчик', 'Пион', 'Роза', 'Фиалка']

@lab2.route("/lab2/flowers/<int:flower_id>")
def renderFlower(flower_id: int):
    if flower_id > len(flower_list) - 1:
        return "Цветок не найден", 404
    else:
        return "Цветок: " + flower_list[flower_id]

@lab2.route("/lab2/flowers/add_flower/<name>")
def add_flower(name):
    if name:
        flower_list.append(name)
        return render_template("addFlowers.html", name=name, flower_list=flower_list)
    else:
        return "Не задано имя цветка", 400

@lab2.route("/lab2/flowers/list")
def flowerList():
        return render_template("flowerList.html", flowers=flower_list, total=len(flower_list))

@lab2.route("/lab2/flowers/clear")
def flowerClear():
    flower_list.clear()
    return render_template("flowerClear.html")

@lab2.route("/lab2/student")
def renderStudent2():
    return render_template("student.html",
                           studentName="Сынару Эжеровна",
                           studentGroup="ФБИ-23",
                           university="НГТУ", labNum="Лаб. 2")

@lab2.route("/lab2/math")
def renderMath():
    return render_template("math.html")



@lab2.route("/lab2/fruits/")
def renderFruits():
    fruits = [
        {'name': 'Яблоки', 'price': 100},
        {'name': 'Груши', 'price': 300},
        {'name': 'Апельсины', 'price': 770},
        {'name': 'Мандарины', 'price': 15},
        {'name': 'Манго', 'price': 230}
    ]
    return render_template("fruits.html",fruits=fruits)

@lab2.route("/lab2/filters")
def renderFilters():
    phrase = "О <b>открытия</b> <u>чудные</u> мои <i>открытия</i>..."
    return render_template("filters.html", phrase=phrase)

@lab2.route("/lab2/calc/")
def calcReroute():
    return redirect("/lab2/calc/1/1")
@lab2.route("/lab2/calc/<int:a>/<int:b>")
def renderCalc(a , b):
    return render_template("calc.html", a=a, b=b)

books = [
    {"name": 'Внутри убийцы', "genre": 'криминал', "pages": 150, "author": 'Денисов Тимофей Леонидович'},
    {"name": 'Синий крот', "genre": 'боевик', "pages": 30, "author": 'Савельев Андрей Константинович'},
    {"name": 'Закад над Гогитамом', "genre": 'приключения', "pages": 179, "author": 'Афанасьева Евдокия Павловна'},
    {"name": 'Рататуй, возвращение легенды', "genre": 'исторический роман', "pages": 330, "author": 'Терехова Кира Семёновна'},
    {"name": 'Как жить со сверхразумом', "genre": 'фэнтези', "pages": 200, "author": 'Лукьянов Кирилл Романович'},
    {"name": 'Породы жаб', "genre": 'приключения', "pages": 890, "author": 'Алексеева София Елисеевна'},
    {"name": 'Энциклопедия сварочных инструментов', "genre": 'любовный роман', "pages": 3013, "author": 'Дроздов Роман Маркович'},
    {"name": 'История Копибар', "genre": 'драма', "pages": 37, "author": 'Болдырев Лука Михайлович'},
    {"name": 'Жаргон Амазонских Племен', "genre": 'фэнтези', "pages": 130, "author": 'Щукин Егор Романович'},
    {"name": 'Розовый завтрак', "genre": 'любовный роман', "pages": 45, "author": 'Соколов Иван Михайлович'},
]
@lab2.route("/lab2/library/")
def renderBooks():
    return render_template("books.html", books=books)

catalogue = [
    {"name": 'GONIK', "desc": 'Мягкий и стильный'},
    {"name": 'ABBUTA', "desc": 'Жесткий и суровый'},
    {"name": 'TUTEL', "desc": 'Вообще топ за свои деньги'},
    {"name": 'ROTLUB', "desc": 'Ну я бы такое не купила конечно'},
    {"name": 'CRINKEL', "desc": 'Ну просто диван, что тут еще сказать'}
]

@lab2.route("/lab2/shop/")
def renderShop():
    return render_template("shop.html", catalogue=catalogue)



