from flask import Blueprint, render_template, redirect, url_for, request, make_response, session
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

users = [
    {'login': 'admin', 'password': 'admin', 'sex': 'male', 'name': 'Системный Администратор'},
    {'login': 'user', 'password': 'user', 'sex': 'female', 'name': 'Сынару'}
]

@lab4.route("/lab4/logout/", methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login/')

@lab4.route("/lab4/login/", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
        else:
            authorized = False
            login = ''

        name = ''
        for user in users:
            if login == user['login']:
                name = user['name']
        return render_template("login.html", authorized=authorized, login=login, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    if login == '':
        return render_template("login.html", error='Не введен логин', authorized=False, login=login)
    if password == '':
        return render_template("login.html", error='Не введен пароль', authorized=False, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')

    return render_template("login.html", error='Не верный логин или пароль', authorized=False, login=login)

@lab4.route("/lab4/fridge/", methods = ['GET','POST'])
def fridge():
    if request.method == 'GET':
        return render_template('fridge.html')

    message = ''
    temp = request.form.get('temp')
    temp = int(temp) if temp else None
    if temp is None:
        message = 'Ошибка: не задана температура'
        color = "color: red;"
    else:
        if int(temp) < -12:
            message = 'Ошибка: не удалось установить температуру — слишком низкое значение'
            color = "color: red;"
        if int(temp) > -1:
            message = 'Ошибка: не удалось установить температуру — слишком высокое значение'
            color = "color: red;"
        if -12 <= int(temp) < -9:
            message = f'Установлена температура: {temp}°С ❄❄❄'
            color = "color: blue;"
        if -8 <= int(temp) < -5:
            message = f'Установлена температура: {temp}°С ❄❄'
            color = "color: blue;"
        if -4 <= int(temp) < -0:
            message = f'Установлена температура: {temp}°С ❄'
            color = "color: blue;"
    return render_template('fridge.html', message=message, style=color, temp=temp)


grains = [
    {'name': 'yachmen', 'price': 12345, 'nameRu': 'Ячмень'},
    {'name': 'oves', 'price': 8522, 'nameRu': 'Овес'},
    {'name': 'pshenicca', 'price': 8722, 'nameRu': 'Пшеница'},
    {'name': 'roz', 'price': 14111, 'nameRu': 'Рожь'}
]

@lab4.route("/lab4/grain/", methods = ['GET','POST'])
def grain():
    if request.method == 'GET':
        return render_template('grain.html')

    item = request.form.get('item')
    weight = request.form.get('weight')

    if item == '':
        error = 'Выберите зерно'
        return render_template('grain.html', error=error)

    if weight is None or weight == '' or weight == "0":
        error = 'Введите кол-во'
        return render_template('grain.html', error=error)

    if float(weight) > 500:
        error = 'Такого объёма сейчас нет в наличии.'
        return render_template('grain.html', error=error)

    total = float(weight)

    for _grain in grains:
        if _grain['name'] == item:
            total *= _grain['price']

    if float(weight) > 50:
        total *= 0.9
        return render_template('grain.html', error='',
                               message=f'Заказ успешно сформирован. Вы заказали зерно.Вес: {weight} т. Сумма к оплате: {total} руб. Скидка за объем - 10%')

    return render_template('grain.html', error='',
                           message=f'Заказ успешно сформирован. Вы заказали зерно.Вес: {weight} т. Сумма к оплате: {total} руб')
























