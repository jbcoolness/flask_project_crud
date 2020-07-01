from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.db import Database

app = Flask(__name__)
app.secret_key = 'my_clave_secreta'

db = Database()

@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/login')
def login():
    #data = db.read(None)

    return render_template('login.html')

@app.route('/crud')
def crud():
    #data = db.read(None)

    return render_template('crud.html')

@app.route('/register')
def register():
    #data = db.read(None)

    return render_template('register.html')

if __name__ == __name__:
    app.run(port=8000, host= "127.0.0.1")
