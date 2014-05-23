__author__ = 'subadmin'

from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sqla
Base = declarative_base()


class Tokens(Base):

    __tablename__ = 'tokens'
    id = sqla.Column(sqla.Integer, primary_key=True)
    token = sqla.Column(sqla.String(10))
    owner = sqla.Column(sqla.Integer)

    def __init__(self, token, owner):
        self.token = token
        self.owner = owner

    def __repr__(self):
        return "User: %s, token: %s" % (self.owner, self.token)
