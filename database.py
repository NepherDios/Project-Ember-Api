from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#Loads in the variables from .env file
load_dotenv()

#Database Data
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

#Connection url to Database
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL) #Makes the connection between postgresql and sqlalchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Makes the object to be used to communicate with the database
Base = declarative_base() #The base class for the database models and identifies the class as a table

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()