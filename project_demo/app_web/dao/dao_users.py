# -*- coding: UTF-8 -*-
from sqlalchemy import text
from .dao_base import DaoBase
from sqlalchemy import Table, Column, Integer, String
from project_demo.app_web.dao.dao_base import metadata, Base

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, comment="id"),
    Column("name", String, comment="name"),
    comment="user table"
)

class ModelUsers(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

class DaoUsers(DaoBase):
    def add_user(self):
        session = self.get_session()
        try:
            user = ModelUsers(name="venti")
            session.add(user)
            session.commit()
        except Exception as e:
            session.rollback()
            return None
        finally:
            session.close()

    def get_user_by_id(self, id):
        session = self.get_session()
        try:
            result = session.query(ModelUsers.name).filter_by(id=id).all()
            return [{"name": r[0]} for r in result]
        except Exception as e:
            session.rollback()
            return None
        finally:
            session.close()

    def get_user_by_id2(self, id):
        session = self.get_session()
        try:
            result = session.execute(text("SELECT name FROM users WHERE id = :id"), {"id": id})
            return result.mappings().all()
        except Exception as e:
            session.rollback()
            return None
        finally:
            session.close()
