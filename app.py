import os

from flask import Flask, render_template, request, session, flash, redirect, url_for
import secrets
import database

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass,
                                                                                 secrets.dbhost, secrets.dbname)
app.config['SECRET_KEY'] = os.urandom(24)
# 'SuperSecretKey'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False


@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template("home.html")
    else:
        if session.get('employee'):
            return redirect(url_for('employee'))
        return redirect(url_for('landpage'))


@app.route('/employee.htm')
def employee():
    start = database.startdate_employee(session['user'])
    position = database.position_employee(session['user'])
    wage = database.wage_employee(session['user'])
    return render_template("employee.html", user=session['user'], start=start, position=position, wage=wage)


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        session['logged_in'] = False
        return render_template("login.html")
    if request.method == 'POST':
        if request.form['account'] == 'customer':
            correctpass = database.userpass(request.form['uname'])
            if correctpass == request.form['psw']:
                session['logged_in'] = True
                session['user'] = database.fullname_fromuser(request.form['uname'])
                session['uname'] = request.form['uname']
                return home()
            else:
                flash('wrong username/password')

        elif request.form['account'] == 'employee':
            correctpass = database.userpassemployee(request.form['uname'])
            if correctpass == request.form['psw']:
                session['logged_in'] = True
                session['employee'] = True
                session['user'] = database.fullname_fromuseremployee(request.form['uname'])
                session['uname'] = request.form['uname']
                return home()
            else:
                flash('wrong username/password')

    return redirect(url_for('login'))


@app.route("/regform.html", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("regform.html")
    if request.method == 'POST':
        # add user to db
        database.new_user(request.form['fname'], request.form['lname'], request.form['uname'],
                          request.form['psw'], request.form['pn'])
        return render_template("landpage.html")


@app.route("/landpage.html")
def landpage():
    userid = database.id_fromuser(session['uname'])
    orders = database.past_orders(userid)
    orderlist = []
    for x in orders:
        orderlist.append(x)

    return render_template("landpage.html", fullname=session['user'], orders=orderlist)


@app.route("/order.html", methods=['GET', 'POST'])
def order():
    if request.method == 'GET':
        return render_template("order.html")


@app.route("/menu.html")
def menu():
    return render_template("menu.html")


@app.route("/location.html")
def location():
    return render_template("location.html")


@app.route("/profile.html")
def logout():
    return render_template("profile.html", user=session['user'])


if __name__ == '__main__':
    database.init_db()
    app.run()
