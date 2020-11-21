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
    query = text("select users.idUser from users where username = :user")
    rs = conn.execute(query, user=username_given).first()
    return rs


# get employee id
def id_fromemployee(username_given):
    query = text("select employee.idemployee from employee where username = :user")
    rs = conn.execute(query, user=username_given).first()
    return rs[0]


print(id_fromemployee("Sal Kuhl"))


# Username and Password search
def userpass(username):
    query = text("select users.password from users where username = :user")
    rs = conn.execute(query, user=username).first()
    password = rs[0]
    if password:
        return password
    else:
        return


print(userpass('tuser20'))


def userpassemployee(username):
    query = text("select employee.password from employee where username = :user")
    rs = conn.execute(query, user=username).first()
    password = rs[0]
    if password:
        return password
    else:
        return


# Current employee Schedule for next 2 weeks
def userschedule(username):
    query = text("select  date, location.address, shifts.shiftType from schedule "
                 "join shifts on shifts.idShift = schedule.idShift "
                 "join location on location.idlocation= schedule.idlocation "
                 "join employee on employee.idemployee = schedule.idemployee "
                 "where employee.idemployee = :user and schedule.date >= curdate() "
                 "and schedule.date < curdate()+14 order by date;")
    rs = conn.execute(query, user=username)
    return rs


# All employee schedules for next 2 weeks
def schedule():
    query = text("select employee.fullname, date, location.address, shifts.shiftType from schedule "
                 "join shifts on shifts.idShift = schedule.idShift "
                 "join location on location.idlocation= schedule.idlocation "
                 "join employee on employee.idemployee = schedule.idemployee "
                 "where schedule.date >= curdate() "
                 "and schedule.date < curdate()+14 order by date;")
    rs = conn.execute(query)
    return rs


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
                 "join menu on fooditems.idItem = menu.idItem where orders.idUser = :user group by idOrder;")
    rs = conn.execute(query, user=iduser).fetchall()
    return rs


# insert new user

def new_user(firstname, lastname, username, password, phonenumber):
    query = text("INSERT INTO users(firstName, lastName, username, password, phoneNumber) "
                 "VALUES (:first, :last, :user, :psw, :phone)")
    trans = conn.begin()
    conn.execute(query, first=firstname, last=lastname, user=username, psw=password, phone=phonenumber)
    trans.commit()
    return


# Business Questions
# 4
def sum_past_orders(iduser):
    orders = past_orders(iduser)
    return len(orders)


# 10
def user_twentytwo_total_orders():
    query = text("select fullName, COUNT(o.idUser) as count from orders o "
                 "join users on users.idUser = o.idUser where users.idUser = 22;")
    rs = conn.execute(query).first()
    return rs


# 9
def most_locations_diner():
    query = text(
        "select l.address, Max(o.idlocation) as location from location l join orders o on l.idlocation = o.idLocation"
        " where CAST(o.time as time ) >= '16:00:00' and CAST(o.time as time ) <= '21:00:00';")
    rs = conn.execute(query).first()
    return rs


# 8
def locations_revenues():
    query = text("Select l.address, sum(total) "
                 "from orders o join location l on l.idlocation = o.idLocation "
                 "group by address;")
    rs = conn.execute(query)
    return rs

# 1
# def working_lastwk_nov():
