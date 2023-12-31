from sqlalchemy import create_engine, Column, Integer, String,Table,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mybank.db", echo=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


customers_account = Table(
  "customers_accounts",
  Base.metadata,
  Column("customers_id",ForeignKey("customers.id"), primary_key=True),
  Column("accounts_id",ForeignKey("accounts.id"), primary_key=True),
  Column("balance",Integer()),
  extend_existing=True,
)

class Customer(Base):
    __tablename__ = "customers"

    id = Column("id",Integer(), primary_key=True, autoincrement=True)
    firstname = Column(String())
    lastname = Column(String())
    dob = Column(String())
    phonenumber = Column(String(),unique=True)
    email = Column(String(),unique=True)

    accounts= relationship("Account",secondary=customers_account,back_populates="customers")
# my reason for making the phonenumber a string instead of an int is because i wont be doing any math with it.

    def __repr__(self):
      return f"<Customer(firstname={self.firstname}, lastname={self.lastname}, dob={self.dob}, phonenumber={self.phonenumber}, email={self.email}, account={self.accounts})>"
    


class Account(Base):
    __tablename__ = "accounts"

    id = Column("id",Integer, primary_key=True , autoincrement=True)
    types = Column("accounttype",String())

    customers = relationship("Customer", secondary=customers_account, back_populates="accounts")

    def __repr__(self):
      return f"<Account(account={self.types})>"
