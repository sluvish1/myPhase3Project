from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from datetime import datetime

engine = create_engine("sqlite:///myproject.db, echo=True")
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"


    customer_id = Column(Integer(), primary_key=True, autoincrement=True)

    firstname = Column(String())
    lastname = Column(String())
    dob = Column(String())
    phonenumber = Column(String(),unique=True)
    email = Column(String(),unique=True)
# my reason for making the phonenumber a string instead of an int is because i wont be doing any math with it.

    def __init__(self, customer_id, firstname, lastname, dob, phonenumber, email):
        self.customer_id = customer_id
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.phonenumber = phonenumber
        self.email = email

    def customerlogin(self,email):
        pass
        # logincustomer = [Customer() ]

    def customersignup(self):
        pass
        
    def __repr__(self):
        return f"<Coustomer( customerdid={self.customer_id}, firstname={self.firstname}, lastname={self.lastname}, dob={self.dob}, phonenumber={self.phonenumber}, email={self.email})>"

 # this creates the database
    if __name__ == '__main__':
     engine = create_engine('sqlite:///:memory:')
     Base.metadata.create_all(engine)




# class CustomerAccount(Base):
#     __tablename__ = "customer_account"

#     balance = Column("balance",Integer)

#     customer_id = relationship()

#     def __init__(self,customer_foreign,account_foreign_key,balance):
#         pass

#     def custaccbal(self):
#         #  i think i should make a dicti to store all to the data for the customer accounts 
#         #  the acc type would be the "key" and the balance would bethe "value" for the money thats in the acc
#         # if
#         # 
#         # accbal = {
#         # saving : customer.id.
#         # 
#         # 
#         #           }
#         pass     

#  # this creates the database
#     if __name__ == '__main__':
#      engine = create_engine('sqlite:///:memory:')
#      Base.metadata.create_all(engine)


class Account(Base):
    __tablename__ = 'accounts'

    account_id = Column(Integer, primary_key=True)
    account_type = Column("accouttype", String())

    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type

    def __repr__(self):
      return f"Account type {self.account_type}"
    
# this creates the database
    if __name__ == '__main__':
     engine = create_engine('sqlite:///:memory:')
     Base.metadata.create_all(engine)


# Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
