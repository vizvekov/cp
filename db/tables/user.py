__author__ = 'subadmin'

from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sqla
Base = declarative_base()


class User(Base):

    __tablename__ = 'users'
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(10))
    password = sqla.Column(sqla.String(10))
    uid = sqla.Column(sqla.Integer)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return "User: %s, UID: %s" % (self.name, self.uid)
