from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.db import Database

app = Flask(__name__)
app.secret_key = 'my_clave_secreta'

db = Database()

@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/login/')
def login():

    return render_template('login.html')

@app.route('/crud', methods = ['POST', 'GET'])
def crud():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash('Resgistro guardado')
        else:
            flash('No se pudo guardar el registro')

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/register')
def register():

    return render_template('register.html')

if __name__ == __name__:
    app.run(debug=True, port=8000)
