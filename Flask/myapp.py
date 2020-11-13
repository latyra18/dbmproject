#from flask import Flask, render_template 
import secrets
from flask import Flask, render_template
#db import
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.dialects.mysql.pymysql

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:april2000@localhost/panthergrill'
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("pgrillhome.html")

@app.route("/regform.html")
def registration():
    return render_template("regform.html")



if __name__ =="__main__":
    app.run()


