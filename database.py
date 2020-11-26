import sqlalchemy as db
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

import secrets
from models import Base

engine = db.create_engine("mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass,
                                                                   secrets.dbhost, secrets.dbname))
conn = engine.connect()

session = sessionmaker(bind=conn)


def init_db():
    Base.metadata.create_all(bind=engine)


# All queries


# get user id
def id_fromuser(username_given):
    query = text("select users.idUser from users where username = :user")
    rs = conn.execute(query, user=username_given).first()
    return rs[0]


# get employee id
def id_fromemployee(username_given):
    query = text("select employee.idemployee from employee where username = :user")
    rs = conn.execute(query, user=username_given).first()
    return rs[0]


# Username and Password search
def userpass(username):
    query = text("select users.password from users where username = :user")
    rs = conn.execute(query, user=username).first()
    password = rs[0]
    if password:
        return password
    else:
        return


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
    query = text("select * from twoweek_schedule")
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


# get menu item
def menu_item(itemnumber):
    query = text("select foodName, price from menu where idItem = :idnum;")
    rs = conn.execute(query, idnum=itemnumber).first()
    return rs


# get location by id
def location_byid(idnumber):
    query = text("select address from location where idlocation = :idnum;")
    rs = conn.execute(query, idnum=idnumber).first()
    return rs[0]


# get menu item price
def menu_item_price(itemnumber):
    query = text("select price from menu where idItem = :idnum;")
    rs = conn.execute(query, idnum=itemnumber).first()
    return rs[0]


# insert new user

def new_user(firstname, lastname, username, password, phonenumber):
    query = text("INSERT INTO users(firstName, lastName, username, password, phoneNumber) "
                 "VALUES (:first, :last, :user, :psw, :phone)")
    trans = conn.begin()
    conn.execute(query, first=firstname, last=lastname, user=username, psw=password, phone=phonenumber)
    trans.commit()
    return


# insert order
def new_order(location, user, total):
    query = text("insert into orders(idLocation, idUser, total) VALUES (:location, :user,:price);")
    trans = conn.begin()
    conn.execute(query, location=location, user=user, price=total)
    trans.commit()
    return


# get orderid
def orderid_lastinsert(user):
    query = text("select max(idOrder) from orders where idUser = :user;")
    rs = conn.execute(query, user=user).first()
    return rs[0]


# insert fooditems
def insert_fooditems(order, item):
    query = text("insert into fooditems(idOrder, idItem) VALUES (:order, :item);")
    trans = conn.begin()
    conn.execute(query, order=order, item=item)
    trans.commit()
    return


# Business Questions
# 1
def working_lastwk_nov():
    query = text("select employee.fullname, location.address, shifts.shiftType, date from schedule s "
                 "join shifts on shifts.idShift = s.idShift  join location on location.idlocation = s.idlocation "
                 "join employee on employee.idemployee = s.idemployee "
                 "where date >= '2020-11-23' and date <= '2020-11-30' order by date;")
    rs = conn.execute(query)
    return rs


# 2
def user_orders_msc(userid):
    query = text("select count(*) as customers from orders "
                 "join users on orders.idUser = users.idUser "
                 "where users.idUser = :user and idLocation = 1;")
    rs = conn.execute(query, user=userid).first()
    return rs[0]


# 3
def most_locations_lunch():
    query = text(
        "select l.address, Max(o.idlocation) as location from location l join orders o on l.idlocation = o.idLocation"
        " where CAST(o.time as time ) >= '12:00:00' and CAST(o.time as time ) <= '17:00:00';")
    rs = conn.execute(query).first()
    return rs


# 4
def sum_past_orders(iduser):
    orders = past_orders(iduser)
    return len(orders)


# 5
def user_orders_zone():
    query = text("select users.fullName from orders "
                 "join users on orders.idUser = users.idUser "
                 "where idLocation = 2;")
    rs = conn.execute(query).fetchall()
    return rs


# 6
def zone_fishorders():
    query = text("select count(fooditemsID) from orders join fooditems f on orders.idOrder = f.idOrder "
                 "join location l on orders.idLocation = l.idlocation where l.idLocation = 2 and f.idItem = 1;")
    rs = conn.execute(query).first()
    return rs[0]


# 7
def most_locations_breakfast():
    query = text(
        "select l.address, Max(o.idlocation) as location from location l join orders o on l.idlocation = o.idLocation"
        " where CAST(o.time as time ) >= '08:00:00' and CAST(o.time as time ) <= '13:00:00';")
    rs = conn.execute(query).first()
    return rs


# 8
def locations_revenues():
    query = text("Select l.address, sum(total) "
                 "from orders o join location l on l.idlocation = o.idLocation "
                 "group by address;")
    rs = conn.execute(query).fetchall()
    return rs


# 9
def most_locations_diner():
    query = text(
        "select l.address, Max(o.idlocation) as location from location l join orders o on l.idlocation = o.idLocation"
        " where CAST(o.time as time ) >= '16:00:00' and CAST(o.time as time ) <= '21:00:00';")
    rs = conn.execute(query).first()
    return rs


# 10
def user_twentytwo_total_orders():
    query = text("select fullName, COUNT(o.idUser) as count from orders o "
                 "join users on users.idUser = o.idUser where users.idUser = 22;")
    rs = conn.execute(query).first()
    return rs
