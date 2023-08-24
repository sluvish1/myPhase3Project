from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mybank.db, echo=True")

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = "customers"

    customerid = Column("id",Integer(), primary_key=True, autoincrement=True)
    firstname = Column(String())
    lastname = Column(String())
    dob = Column(datetime())
    phonenumber = Column(String(),unique=True)
    email = Column(String(),unique=True)

    accounts = relationship("Account", secondary=customers_accounts, back_populates="customers")
    customeraccount = relationship("CustomerAccount", backref=backref("customer") )
# my reason for making the phonenumber a string instead of an int is because i wont be doing any math with it.

    def __repr__(self):
      return f"<Customer(firstname={self.accounttype}, lastname={self.lastname}, dob={self.dob}, phonenumber={self.phonenumber}, email={self.email})>"
    

    if __name__ == '__main__':
     Base.metadata.create_all(engine)


class Account(Base):
    __tablename__ = 'accounts'

    accountid = Column("id",Integer, primary_key=True , autoincrement=True)
    accounttype = Column(String())

    customers = relationship("Customers", secondary=customers_accounts, back_populates="accounts")
    customeraccount = relationship("CustomerAccount", backref=backref("account") )
    def __repr__(self):
      return f"<Account(account_type={self.accounttype})>"
    
# this creates the database
    if __name__ == '__main__':
     Base.metadata.create_all(engine)




class CustomerAccount(Base):
  __tablename__ = "customers_accounts"

  idd= Column("id",Integer,primary_key=True)

  customer_id=Column(Integer(),ForeignKey(customers.id))
  accoutn_id=Column(Integer(),ForeignKey(accounts.id))
  def __repr__(self):
    return f"<CustomerAccount(customer_id={self.customer_id})>"


"""
What do i want my app to do?

1. Allow users that are already customers who already have an account to login
2. Users without and accout will need to signup
3. Show all of the accounts the user has along with the balance 
5. Allow users to open a new account
6. Allow users to close accounts they no long want 

a customer can have many types of accounts and many accounts can belong to many users

"""