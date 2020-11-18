import sqlalchemy as db
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, session
import secrets
from models import Base, Users, Order

engine = db.create_engine("mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass,
                                                                   secrets.dbhost, secrets.dbname))
conn = engine.connect()

session = sessionmaker(bind=conn)


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


# Username and Password search
def userpass(username):
    usernamepassword = db.select([Users.password]).where(Users.username == username)
    resulthandler = engine.execute(usernamepassword)
    passwordall = resulthandler.first()
    password = passwordall[0]
    if password:
        return password
    else:
        return


# Find full name of user from username
def fullname_fromuser(username_given):
    query = db.select([Users.fullName]).where(Users.username == username_given)
    resulthandler = engine.execute(query)
    resultset = resulthandler.first()
    fullname = resultset[0]
    return fullname


# insert new user
'''
def new_user(firstname, lastname, username, password, phonenumber):
    user = Users(firstName=firstname, lastName=lastname, username=username, password=password, phonenumber=phonenumber)
    trans = conn.begin()
    conn.execute(db.insert[user].into(Users))
    trans.commit()
    conn.close()
'''