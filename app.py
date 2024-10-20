from flask import Flask, render_template, redirect
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4

app = Flask(__name__, template_folder='templates')
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

@app.route("/")
def root():
    return redirect("/menu", code=302)


@app.route("/menu")
def renderMenu():
    return render_template("menu.html")


@app.route("/lab3")
def renderLab3():
    return render_template("lab3.html")

if __name__ == '__main__':
    app.run(debug=True)
