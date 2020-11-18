
import secrets

import app


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass,
                                                                                 secrets.dbhost, secrets.dbname)
app.config['SECRET_KEY'] = 'SuperSecretKey'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False


def databaseuri():
    return "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass,
                                                    secrets.dbhost, secrets.dbname)
