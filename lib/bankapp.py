from models import(Base,session,engine,datetime,
                   Customer, Account,customers_account)

def login():
    print("Welcome To Mckenzie's Banking! Please Login With Your Email If You Have An Account, Otherwise Please Sign Up!")
    currentuser = input(f"Email: {Customer}")
    if currentuser == True:
        return print(f"Hello {currentuser}")
    else:
        return print("This Email Isnt On File, Please Sign Up For An Account!")

def signup():
    pass









if __name__ == "__main__":
    Base.metadata.create_all(engine)