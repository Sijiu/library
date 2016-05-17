# -*- coding: utf-8 -*-

import sqlalchemy as SA
from model.session import sessionCM
from model.base import Base
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


class Amazon_errcode(Base):
    __tablename__ = "amazon_errcode"
    id = SA.Column(SA.INTEGER, primary_key=True, autoincrement=True)
    err_code = SA.Column(SA.INTEGER)
    err_desc = SA.Column(SA.String(1024))  # max = 21845
    err_solution = SA.Column(SA.TEXT)

    @classmethod
    def create(cls, session, err_code, err_desc, err_solution):
            amazon_err = Amazon_errcode()
            amazon_err.err_code = err_code
            amazon_err.err_desc = err_desc
            amazon_err.err_solution = err_solution
            session.add(amazon_err)
            session.commit()
            return amazon_err

    @classmethod
    def find_errcode(cls, session, err_code):
        return session.query(cls).filter(
            SA.and_(
                cls.err_code == err_code
            )
        ).all()


    @classmethod
    def find_errcode(cls, session, err_code):
        try:
            return session.query(cls).filter(cls.err_code == err_code).one()
        except MultipleResultsFound:
            return None
        except NoResultFound:
            return None
