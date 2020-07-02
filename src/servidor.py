from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.db import Database

app = Flask(__name__)
app.secret_key = 'my_clave_secreta'

db = Database()

@app.route('/', methods=["GET", "POST"])
def index():
    data = db.read(None)
    return render_template('index.html', data = data)



@app.route('/login')
def login():

    return render_template('login.html')

# Se define para agregar registros en la base de datos
@app.route('/insert', methods=["GET", "POST"])
def insert():
    print('Entro al insert')
    if request.method == 'POST':
        print('Entro al request.method')
        if db.insert(request.form):
            flash('Resgistro guardado', 'alert-success')
        else:
            flash('No se pudo guardar el registro', 'alert-warning')

        return redirect(url_for('index'))
    else:
        print('Entro al insert y salio de una')
        return redirect(url_for('index'))


@app.route('/register')
def register():

    return render_template('register.html')

if __name__ == __name__:
    app.run(debug=True, port=8000)
