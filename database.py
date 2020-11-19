import sqlalchemy as db
from sqlalchemy import create_engine, text
from sqlalchemy.dialects.mysql import SET

from sqlalchemy.orm import sessionmaker, Session
import secrets
from models import Base, Users, Order, Employee, Menu, Fooditems

engine = db.create_engine("mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass,
                                                                   secrets.dbhost, secrets.dbname))
conn = engine.connect()

session = sessionmaker(bind=conn)


# session = Session()
def init_db():
    Base.metadata.create_all(bind=engine)


# queries
'''''
with engine.connect() as conn:
    orders = list(conn.execute('SELECT * FROM orders'))
    for x in orders:
        print(x)
'''
# All orders
allOrders = db.select([Order])
ReseltHandle = engine.execute(allOrders)
ResultSet = ReseltHandle.fetchall()
print(ResultSet)

# All users
allUsers = db.select([Users])
ReseltHandle = engine.execute(allUsers)
ResultSet = ReseltHandle.fetchall()


# get user id
def id_fromuser(username_given):
    query = db.select([Users.idUser]).where(Users.username == username_given)
    resulthandler = engine.execute(query)
    resultset = resulthandler.first()
    userid = resultset[0]
    return userid


# Username and Password search
def userpass(username):
    query = text("select users.password from users where username = :user")
    rs = conn.execute(query, user=username).first()
    password = rs[0]
    if password:
        return password
    else:
        return

print(userpass('spaty4'))

def userpassemployee(username):
    query = text("select employee.password from employee where username = :user")
    rs = conn.execute(query, user=username).first()
    password = rs[0]
    if password:
        return password
    else:
        return

# Employee start date
def startdate_employee(name):
    query = text("select employee.startDate from employee where username = :user")
    rs = conn.execute(query, user=name).first()
    date = rs[0]
    return date

# Position of employee
def position_employee(name):
    query = text("select employee.title from employee where username = :user")
    rs = conn.execute(query, user=name).first()
    position = rs[0]
    return position

# Wage of employee
def wage_employee(name):
    query = text("select employee.wage from employee where username = :user")
    rs = conn.execute(query, user=name).first()
    wage = rs[0]
    return wage


# Find full name of user from username
def fullname_fromuser(username_given):
    query = text("select users.fullname from users where username = :user")
    rs = conn.execute(query, user=username_given).first()
    fullname = rs[0]
    return fullname


def fullname_fromuseremployee(username_given):
    query = text("select employee.fullname from employee where username = :user")
    rs = conn.execute(query, user=username_given).first()
    fullname = rs[0]
    return fullname


# past orders

def past_orders(iduser):
    query = text("select orders.idOrder, orders.time, orders.idLocation, orders.total "
                 "from orders join fooditems ON orders.idOrder = fooditems.idOrder "
                 "join menu on fooditems.idItem = menu.idItem where orders.idUser = :user group by idOrder")
    rs = conn.execute(query, user=iduser).fetchall()
    return rs


# insert new user

def new_user(firstname, lastname, username, password, phonenumber):
    query = text("INSERT INTO users(firstName, lastName, username, password, phoneNumber) "
                 "VALUES (:first, :last, :user, :psw, :phone)")
    trans = conn.begin()
    conn.execute(query, first=firstname, last=lastname, user=username, psw=password, phone=phonenumber)
    trans.commit()
    conn.close()
    return
