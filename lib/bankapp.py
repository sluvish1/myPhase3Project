from models import Base,session,engine,Customer , Account, CustomerAccount











if __name__ == "__main__":
    Base.metadata.create_all(engine)