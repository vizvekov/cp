__author__ = 'subadmin'


from sqlalchemy.orm import sessionmaker
import uuid
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from tables.user import User
from tables.tokens import Tokens
from tables.vhosts import VHosts


class SqlWork():

    def __init__(self):
        self.Tables = {}
        self.engine = sqla.create_engine('sqlite:////tmp/sql.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.Tables['users'] = User
        self.Tables['users'].metadata.create_all(self.engine)
        self.Tables['tokens'] = Tokens
        self.Tables['tokens'].metadata.create_all(self.engine)
        self.Tables['vhosts'] = VHosts
        self.Tables['vhosts'].metadata.create_all(self.engine)

    def get_table_object(self, table_name):
        if table_name in self.Tables:
            return True, self.Tables[table_name]
        else:
            return False, False

    def get_new_token(self, uid):
        stat, token_object = self.get_table_object('tokens')
        if stat:
            newToken = token_object(uuid.uuid4().hex, uid)
            self.add_line(newToken)
            return True, newToken.token
        else:
            return False, False

    def validate_token(self, token):
        uid = self.get_session().query(self.Tables['tokens'].owner).filter_by(token=token)[0]
        if uid:
            return True, uid
        return False, False

    def get_vhosts_by_owner(self, user_name='', uid=''):
        table_name = 'vhosts'
        vhosts = []
        if user_name != '':
            for vhost, in self.get_session().query(self.Tables[table_name]).filter_by(user_name=user_name):
                vhosts.append(vhost)
        elif uid != '':
            for vhost, in self.get_session().query(self.Tables[table_name]).filter_by(owner_id=id):
                vhosts.append(vhost)
        else:
            return False, False
        return True, vhosts

    def get_user_by(self, user_id = '', user_name = ''):
        if user_id != '':
            name = self.get_session().query(self.Tables['users'].name).filter_by(id=user_id)[0]
            if name:
                return True, name
        elif user_name != '':
            user_id = self.get_session().query(self.Tables['users'].id).filter_by(user_name=user_name)[0]
            if user_id:
                return True, user_id
        else:
            return False, 'no user name/id getting'
        return False, 'no user'

    def get_session(self):
        return self.Session()

    def add_line(self, TableObject):
        session = self.Session()
        session.add(TableObject)
        self.__db_commit(session)

    def __db_commit(self, session):
        session.commit()
        session.close()

