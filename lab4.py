from flask import Blueprint, render_template, redirect, url_for, request, make_response
lab4 = Blueprint('lab4', __name__)

@lab4.route("/lab4/")
def renderLab4():
    return render_template("lab4.html")

@lab4.route("/lab4/posttest")
def posttest():
    return render_template("posttest.html")

@lab4.route("/lab4/div", methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '' or x2 == '0':
        return render_template("div.html", error="Числа заполни + второе не должно быть равно 0")

    result = int(x1) / int(x2)
    return render_template("div.html", x1=x1, x2=x2, result=result)


@lab4.route("/lab4/sumStart")
def sumStart():
    return render_template("sumStart.html")


@lab4.route("/lab4/sum", methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 0
    if x2 == '':
        x2 = 0

    result = int(x1) + int(x2)
    return render_template("sum.html", x1=x1, x2=x2, result=result)

@lab4.route("/lab4/multStart")
def multStart():
    return render_template("multStart.html")

@lab4.route("/lab4/multi", methods = ['POST'])
def mult():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 1
    if x2 == '':
        x2 = 1

    result = int(x1) * int(x2)
    return render_template("multi.html", x1=x1, x2=x2, result=result)

@lab4.route("/lab4/subtrStart")
def subtrStart():
    return render_template("subtrStart.html")

@lab4.route("/lab4/subtr", methods = ['POST'])
def subtr():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template("subtr.html", error="Числа заполни!")

    result = int(x1) - int(x2)
    return render_template("subtr.html", x1=x1, x2=x2, result=result)

@lab4.route("/lab4/powStart")
def powStart():
    return render_template("powStart.html")

@lab4.route("/lab4/pow", methods = ['POST'])
def pow():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template("pow.html", error="Числа заполни!")
    if x1 == '0' and x2 == '0':
        return render_template("pow.html", error="Оба не могут быть 0")
    result = int(x1) ** int(x2)
    return render_template("pow.html", x1=x1, x2=x2, result=result)

tree_count = 0
@lab4.route("/lab4/tree", methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template("tree.html", tree_count=tree_count)

    operation = request.form.get('operation')

    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count += 1

    return redirect('/lab4/tree')

@lab4.route("/lab4/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html", authorized=False)

    login = request.form.get('login')
    password = request.form.get('password')

    return render_template("login.html", error='Успешная авторизация', login=login, authorized=True)
    return render_template("login.html", error='Не верный логин или пароль', authorized=False)




















