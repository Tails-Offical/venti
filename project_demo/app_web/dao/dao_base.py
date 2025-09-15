# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

metadata = MetaData()
Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)

class DaoBase:
    def __init__(self):
        self.engine = engine

    def get_session(self):
        return Session()

    def create_table(self):
        Base.metadata.create_all(self.engine)
