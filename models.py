from sqlalchemy import Column, Integer, String, Date, Enum, Float, Time, ForeignKey, func, DateTime
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

    def __repr__(self):
        return {'name': self.fullName, 'username': self.username, 'password': self.password,
                'phonenumber': self.phonenumber}


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
    username = Column(String(45), default=fullName)
    password = Column(String(45), default=phoneNumber)

    def __repr__(self):
        return self.fullName


# Table fooditems


class Fooditems(Base):
    __tablename__ = 'fooditems'
    fooditemsID = Column(Integer, primary_key=True)
    idOrder = Column(Integer, ForeignKey("orders.idOrder"))
    idItem = Column(Integer, ForeignKey("menu.idItems"))


# Table location
class Location(Base):
    __tablename__ = 'location'
    idLocation = Column(Integer, primary_key=True)
    address = Column(String(776), nullable=False)
    hoursOpen = Column(Time, nullable=False)
    hoursCLose = Column(Time, nullable=False)

    def __repr__(self):
        return self.address


# Table menu
class Menu(Base):
    __tablename__ = 'menu'
    idItem = Column(Integer, primary_key=True)
    foodName = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return self.foodName


# Table shifts
class Shifts(Base):
    __tablename__ = 'shifts'
    idShift = Column(Integer, primary_key=True)
    shiftType = Column('shiftType', Enum('breakfast', 'lunch', 'dinner', 'late'))
    shiftStart = Column(Time, nullable=False)
    shiftEnd = Column(Time, nullable=False)
    shiftHours = Column(Time, nullable=False)

    def __repr__(self):
        return self.shiftType


# Table orders
class Order(Base):
    __tablename__ = 'orders'
    idOrder = Column(Integer, primary_key=True)
    idLocation = Column(Integer, ForeignKey('location.idlocation'))
    time = Column(DateTime, default=func.current_timestamp())
    idUser = Column(Integer, ForeignKey('users.idUser'))
    total = Column(Integer, nullable=False)

    def __repr__(self):
        return {'order id': self.idOrder, 'date': self.time, 'total': self.total}


# Table schedule
class Schedule(Base):
    __tablename__ = 'schedule'
    idschedule = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    idShift = Column(Integer, ForeignKey('shifts.idShifts'))
    idEmployee = Column(Integer, ForeignKey('employee.idemployee'))
    idLocation = Column(Integer, ForeignKey('location.idLocation'))

    def __repr__(self):
        return self.date
