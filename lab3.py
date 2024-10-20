from flask import Blueprint, render_template, redirect, url_for, request, make_response
lab3 = Blueprint('lab3', __name__)

@lab3.route("/lab3/")
def renderLab3():
    name = request.cookies.get('name')
    color = request.cookies.get('name_color')
    return render_template("lab3.html", name=name, name_color=color)


@lab3.route("/lab3/cookies/")
def renderCookies():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Synaru')
    resp.set_cookie('age', '23')
    resp.set_cookie('name_color', 'Red')
    return resp


@lab3.route("/lab3/clearCookies/")
def clearCookies():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    resp.delete_cookie('color')
    resp.delete_cookie('background-color')
    resp.delete_cookie('font-size')
    return resp


@lab3.route("/lab3/form1/")
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route("/lab3/order/")
def order():
    return render_template('order.html')

@lab3.route("/lab3/success/")
def paySuccess():
    total = request.args.get('total')
    return render_template('success.html', total=total)

@lab3.route("/lab3/pay/")
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)

@lab3.route("/lab3/settings/")
def settings():
    color = request.args.get('color')
    bg_color = request.args.get('background-color')
    font_size = request.args.get('font-size')
    if color or bg_color or font_size:
        resp = make_response(redirect("/lab3/settings/"))
        resp.set_cookie('color', color) if color else ''
        resp.set_cookie('background-color', bg_color) if bg_color else ''
        resp.set_cookie('font-size', font_size) if font_size else ''
        return resp

    color = request.cookies.get('color')
    bg_color = request.cookies.get('background-color')
    font_size = request.cookies.get('font-size')
    resp = make_response(render_template('settings.html', color=color, bg_color=bg_color, font_size=font_size))
    return resp

@lab3.route("/lab3/ticketOrder/")
def ticketOrder():
    default = request.args.get('default')
    if default == "default":
        return render_template('ticketForm.html', errors=[])

    errors = []
    name = request.args.get('name')
    if name == '':
        errors.append('Имя - Обязательное поле')
    surname = request.args.get('surname')
    if surname == '':
        errors.append('Фамилия - Обязательное поле')
    age = request.args.get('age')
    if age == '':
        errors.append('Возраст - Обязательное поле')
    if age:
        if int(age) > 120 or int(age) < 1:
            errors.append('Допустимый возраст 1-120 лет.')
    start = request.args.get('start')
    if start == '':
        errors.append('Пункт отправления - Обязательное поле')
    end = request.args.get('end')
    if end == '':
        errors.append('Пункт назначения - Обязательное поле')
    date = request.args.get('date')
    if date == '':
        errors.append('Дата отправления - Обязательное поле')
    seat = request.args.get('seat')
    if seat == '':
        errors.append('Место в вагоне - Обязательное поле')

    if len(errors) == 0:
        fullName = f'{surname} {name} {request.args.get("patronym")}'
        ensurance = request.args.get("ensurance")
        luggage = request.args.get("luggage")
        bedsheets = request.args.get("bedsheets")
        seat = request.args.get("seat")

        total = 1000
        if int(age) < 18:
            total -= 300
        if seat == 'bottom' or seat == 'bottom-side':
            total += 100
        if bedsheets == "on":
            total += 75
        if luggage == "on":
            total += 250
        if ensurance == "on":
            total += 150

        if start == 'Novosibirsk':
            start = 'Новосибирск'
        if start == 'Derevnevo':
            start = 'Деревнево'
        if start == 'Poselkovo':
            start = 'Поселково'

        if end == 'Novosibirsk':
            end = 'Новосибирск'
        if end == 'Derevnevo':
            end = 'Деревнево'
        if end == 'Poselkovo':
            end = 'Поселково'

        if seat == 'bottom':
            seat = 'Нижнее'
        if seat == 'top':
            seat = 'Верхнее'
        if seat == 'bottom-side':
            seat = 'Нижнее-Боковое'
        if seat == 'top-side':
            seat = 'Нижнее-Боковое'

        return render_template('ticket.html', fullName=fullName, age=int(age),
                               start=start, end=end, date=date, seat=seat,
                               ensurance=ensurance,
                               luggage=luggage,
                               bedsheets=bedsheets,
                               total=total)

    return render_template('ticketForm.html', errors=errors)

@lab3.route("/lab3/ticket/")
def ticket():
    return render_template('ticket.html')















