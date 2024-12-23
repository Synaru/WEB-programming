from flask import Blueprint, render_template, redirect, url_for, request, make_response, session, current_app

lab6 = Blueprint('lab6', __name__)
import random

offices = []
for i in range(1, 11):
    offices.append({
        "number": i,
        "tenant": "",
        "price": 1000 + random.randint(0, 1000) // 100 * 100
    })


@lab6.route("/lab6/")
def lab6index():
    return render_template("lab6.html", login=session.get('login'))


@lab6.route("/lab6/json-rpc-api/", methods=['POST'])
def api():
    data = request.json
    id = data['id']

    login = session.get('login')
    if not login:
        return {
            "jsonrpc": '2.0',
            "error": {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }

    if data['method'] == 'info':
        return {
            "jsonrpc": '2.0',
            "result": offices,
            "login": login,
            'id': id
        }

    if data['method'] == 'book':
        officeNumber = data['params']
        for office in offices:
            if office['number'] == officeNumber:
                if office['tenant'] != '':
                    return {
                        "jsonrpc": '2.0',
                        "error": {
                            'code': 2,
                            'message': 'Already booked'
                        },
                        'id': id
                    }
                office['tenant'] = login
                return {
                    "jsonrpc": '2.0',
                    "result": "success",
                    'id': id
                }

    if data['method'] == 'cancel':
        officeNumber = data['params']
        for office in offices:
            if office['number'] == officeNumber:
                if office['tenant'] != login:
                    return {
                        "jsonrpc": '2.0',
                        "error": {
                            'code': 2,
                            'message': 'Нельзя снять чужую аренду'
                        },
                        'id': id
                    }
                office['tenant'] = ''
                return {
                    "jsonrpc": '2.0',
                    "result": "success",
                    'id': id
                }

    return {
        "jsonrpc": '2.0',
        "error": {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }
