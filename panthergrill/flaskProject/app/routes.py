from flask import request, render_template, session, flash
from flask import current_app as app


@app.route("/")
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


@app.route("/regform.html", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("regform.html")
    if request.method == 'POST':
        return "Need to add user to db "
    return home()
