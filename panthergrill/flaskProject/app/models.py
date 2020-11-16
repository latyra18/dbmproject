from sqlalchemy import Column, Integer, String, Date, Enum, Float, Time
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


class Fooditems(Base):
    __tablename__ = 'fooditems'
    fooditemsID = Column(Integer, primary_key=True)
    idOrder = Column(Integer, nullable=False)
    idItem = Column(Integer, nullable=False)


# Table location
class Location(Base):
    __tablename__ = 'location'
    idLocation = Column(Integer, primary_key=True)
    address = Column(String(776), nullable=False)
    hoursOpen = Column(Time, nullable=False)
    hoursCLose = Column(Time, nullable=False)


# Table menu
class Menu(Base):
    __tablename__ = 'menu'
    idItem = Column(Integer, primary_key=True)
    foodName = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)


# Table shifts
class Shifts(Base):
    __tablename__ = 'shifts'
    idShift = Column(Integer, primary_key=True)
    shiftType = Column('shiftType', Enum('breakfast', 'lunch', 'dinner'))
    shiftStart = Column(Time, nullable=False)
    shiftEnd = Column(Time, nullable=False)
    shiftHours = Column(Time, nullable=False)


# Table orders

# Table schedule
