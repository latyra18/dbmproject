from flask import request, render_template, make_response, session, flash
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User

app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template("home.html")
    else:
        return 'Logged in'  # replace with landing page


@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        if request.form['psw'] == 'password' and request.form['uname'] == 'username':
            session['logged_in'] = True
        else:
            flash('wrong username/password')
    return home()
