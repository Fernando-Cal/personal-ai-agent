from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base 

# where the DB lives 
SQLALCHEMY_DATABASE_URL = "sqlite:///./conversation.db"

# the engine (connection) connects python to the db 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# session factory, creates short lived db sessions 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for models, lets us define tables using python classes
Base = declarative_base()

def get_db():
    db = SessionLocal() # open connection 
    try:
        yield db
    finally:
        db.close() # close session after route finishes