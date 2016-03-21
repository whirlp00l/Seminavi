from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE),echo=True)

def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Company(DeclarativeBase):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    companyid = Column('companyid', Integer)
    name = Column('name', String)
    detial = Column('detial', String, nullable= True)
    url = Column('url', String)

class Seminar(DeclarativeBase):
    __tablename__ = "seminar"

    id = Column(Integer,primary_key=True)
    companyid = Column('companyid', Integer)
    name = Column('name', String)
    date = Column('date', DateTime, nullable=True)
    time = Column('time', String, nullable=True)
    area = Column('area', String, nullable=True)
    place = Column('place', String, nullable=True)
    loc_n = Column('loc_n', String, nullable=True)
    loc_e = Column('loc_e', String, nullable=True)
    target = Column('target', String, nullable=True)
    submit = Column('submit', String, nullable=True)