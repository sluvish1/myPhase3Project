from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime 

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column("id", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    dob = Column("dob", datetime())
    phonenumber = Column("phonenumber", String)
    email = Column("email", String)
# my reason for making the phonenumber a string instead of an int is because i wont be doing any math with it.

    def __init__(self, customer_id, firstname, lastname, dob, phonenumber, email):
        self.customer_id = customer_id
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.phonenumber = phonenumber
        self.email = email

        
    def __repr__(self):
        return f"({self.customer_id}{self.firstname}{self.lastname} {self.dob} {self.phonenumber}{self.email})"


# class CustomerAccount(Base):
#     __tablename__ = "customer_account"

#     customer_foreignkey = Column(Integer)
#     account_foreignkey = Column("id",Integer,ForeignKey())



class Account(Base):
    __tablename__ = 'accounts'

    account_id = Column("id", Integer, primary_key=True)
    account_type = Column("accouttype", String)

    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type

engine = create_engine("sqlite:///myptoject.bd, echol=Ture")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


customer = Customer()