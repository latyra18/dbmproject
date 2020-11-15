#from flask import Flask, render_template 
import secrets
from flask import Flask, render_template,request, redirect, flash, session, abort
#db import
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.dialects.mysql.pymysql
#from myapp import db_session

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:april2000@localhost/panthergrill'
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

'''
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
'''


@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template("home.html")
    else:
        return 'Logged in' #replace with landing page

@app.route("/login.html", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        if request.form['psw']=='password' and request.form['uname']=='username':
            session['logged_in'] = True
        else:
            flash('wrong username/password')
    return home()

@app.route("/regform.html", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("regform.html")
    if request.method == 'POST':
        return "Need to add user to db "
    return home()



if __name__ =="__main__":
    app.run()


