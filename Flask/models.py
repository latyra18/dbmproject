from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from Flask.myapp import db
#from Flask.database import Base

class Users(db.Model):
    __tablename__ = 'users'
    idUser = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String(50), nullable=False )
    lastName = Column(Float, nullable=False)
    fullName = Column(Float, default=fullnamedefault)
    createdOn = Column(Float, nullable=False)
    username = Column(Float, nullable=False)
    password = Column(Float, nullable=False)
    phonenumber = Column(String(45), nullable=False)

    def __init__(self, firstName=None, lastName=None, fullName=None, createdOn=None, username=None, password=None, phonenumber=None):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = fullName
        self.createdOn = createdOn
        self.username = username
        self.password = password
        self.phonenumber = phonenumber


    def __repr__(self):
        return '<User %r>' % (self.fullName)

def fullnamedefault(context):
        return context.get_current_parameters()['firstName','lastName']



class Menu(Base):
    #__tablename__ = 'menu'
    idItem = Column(Integer, primary_key=True, nullable=False)
    foodName = Column(String(50), nullable=False )
    price = Column(Float, nullable=False)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)