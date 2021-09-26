import sqlalchemy
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE = declarative_base()

app = Flask(__name__)


class Admin(BASE):
    __tablename__ = 'admin'

    id = sqlalchemy.Column(sqlalchemy.String(64), primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(64))
    password = sqlalchemy.Column(sqlalchemy.String(64))
    create_at = sqlalchemy.Column(sqlalchemy.DateTime, server_default=sqlalchemy.func.now())


@app.route('/')
def create_admin_table():
    # Make sure that you are running a mysql and created the ntcuba database.
    engine = sqlalchemy.create_engine("mysql+pymysql://root:ntcuba@localhost:3306/ntcuba", echo=True)
    # Session will be a function for CRUD !!!
    Session = sessionmaker(bind=engine)
    BASE.metadata.create_all(engine)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
