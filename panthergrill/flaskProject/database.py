from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Employee

metadata = MetaData()
engine = create_engine('mysql+pymysql://root:april2000@localhost/panthergrill', pool_recycle=3600)

db_session = sessionmaker(bind=engine)()


def get_employees():
    return db_session.query(Employee)


data = get_employees()
