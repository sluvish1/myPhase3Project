from models import(Base,session,engine,
                   Customer, Account,customers_account)

def login():
    print("Welcome To Mckenzie's Banking! Please Login With Your Email If You Have An Account, Otherwise Please Sign Up!")
    currentuser = input(f"Email: ")
    if currentuser == Customer.email:
       myaccount()
    else:
        print("This Email Isnt On File, Please Sign Up For An Account!")
        signup()

def signup(self):
    print("Please Fill In The Form To Sign Up For An Account")
    new_user_email = input("What is your email?")


def myaccount():
    print("""Hello How May We Assit You Today?
          1.VIEW CHECKING ACCOUNT
          2.VIEW SAVINGS ACCOUNT
          3.VIEW CREDIT CARD
          4.VIEW LOAN
          5.OPEN AN ACCOUNT
          """)
    customer_answer=input()
    if customer_answer == "1":
        checkingaccount()
    elif customer_answer == "2":
        savingaccount()
    elif customer_answer == "3":
        creditcard()
    elif customer_answer == "4":
        loans()
    elif customer_answer == "5":
        openacc()
    else:
        print("The Number You've Entered Is Invalid, Please Select a Number 1-5.")

def checkingaccount():
    pass

def savingaccount():
    pass

def creditcard():
    pass

def loans():
    pass

def openacc():
    pass



"""
What do i want my app to do?

1. Allow users that are already customers who already have an account to login, so verifiy the user by email
2. Users without and accout will need to signup
3. Show all of the accounts the user has along with the balance 
5. Allow users to open a new account
6. Allow users to close accounts they no long want 
7.Users should be allowed to transfer money between accounts

a customer can have many types of accounts and many accounts can belong to many users

"""

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    myaccount()