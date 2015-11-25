import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Table

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Donors (Base):
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(80))
    last_name = Column(String(80))
    address = Column(String(180))
    dob = Column(String(10))
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

class Storage (Base):
    __tablename__ = 'storage'
    id = Column(Integer, primary_key=True)
    location = Column(String(20))


products_storage = Table('products_storage', Base.metadata,
    Column('products_id', Integer, ForeignKey('products.id')),
    Column('storage_id', Integer, ForeignKey('storage.id'))
)


class Products (Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    bcode = Column(String(20))
    product_code = Column(String(10))
    type = Column(String(6))
    exp_date = Column(String(10))
    donors_id = Column(Integer, ForeignKey('donors.id'))
    donors = relationship(Donors)
    storage_id = Column(Integer, ForeignKey('storage.id'))
    storage = relationship(Storage, secondary=products_storage)



engine = create_engine('sqlite:///newBlood.db')


Base.metadata.create_all(engine)
