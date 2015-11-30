import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


# products_storage = Table('products_storage', Base.metadata,
#     Column('products_id', Integer, ForeignKey('products.id')),
#     Column('storage_id', Integer, ForeignKey('storage.id'))
# )


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

# def __init__(self, name):
#               self.name = name

# def __repr__(self):
#         return "<Users('%s')>" % (self.name)


class Donors (Base):
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(80))
    last_name = Column(String(80))
    address = Column(String(180))
    dob = Column(String(10))
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

# def __init__(self, first_name, last_name,address, dob, users):
#               self.name = name
#               self.last_name

# def __repr__(self):
#         return "<Users('%s')>" % (self.name)d


class Medication(Base):
    __tablename__ = 'medication'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    sideffects = Column(String(200), nullable=False)
    donors_id = Column(Integer, ForeignKey('donors.id'))
    donors = relationship(Donors)


class Products (Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    bcode = Column(String(20))
    product_code = Column(String(10))
    type = Column(String(6))
    exp_date = Column(String(10))
    donors_id = Column(Integer, ForeignKey('donors.id'))
    donors = relationship(Donors)
    # storage_id = Column(Integer, ForeignKey('storage.id'))
    # storage = relationship("Storage", backref='products', secondary=products_storage)


engine = create_engine('sqlite:///newBlood.db')


Base.metadata.create_all(engine)
