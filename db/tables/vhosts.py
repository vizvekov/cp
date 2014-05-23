__author__ = 'subadmin'

from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sqla
Base = declarative_base()


class VHosts(Base):

    __tablename__ = 'vhosts'
    id = sqla.Column(sqla.Integer, primary_key=True)
    domain_name = sqla.Column(sqla.String(50))
    user_name = sqla.Column(sqla.String(10))
    user_group = sqla.Column(sqla.String(10))
    domain_alias = sqla.Column(sqla.String(200))
    owner_id = sqla.Column(sqla.Integer)

    def __init__(self, owner_id, domain_name, user_name, user_group, domain_alias=''):
        self.domain_name = domain_name
        self.user_name = user_name
        self.user_group = user_group
        self.domain_alias = domain_alias
        self.owner_id = owner_id


    def __repr__(self):
        return "Main Domain: %s, Owner: %s" % (self.domain_name, self.owner_id)
