from sqlalchemy import Column, Integer, String, Date, Enum, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Table users

class Users(Base):
    __tablename__ = 'users'
    idUser = Column(Integer, primary_key=True)
    firstName = Column(String(45), nullable=False)
    lastName = Column(String(45), nullable=False)
    fullName = Column(String(45), default=firstName + " " + lastName)
    createdOn = Column(Date, nullable=False)
    username = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    phonenumber = Column(String(45), nullable=False)


# Table employee


class Employee(Base):
    __tablename__ = 'employee'
    idemployee = Column(Integer, primary_key=True)
    firstName = Column(String(45), nullable=False)
    lastName = Column(String(45), nullable=False)
    fullName = Column(String(45), default=firstName + " " + lastName)
    startDate = Column(Date, nullable=False)
    title = Column('title', Enum('team member', 'manager'))
    wage = Column(Float, nullable=False)
    phoneNumber = Column(String(45), nullable=False)
    endDate = Column(Date, nullable=True)

# Table fooditems
