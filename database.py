from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Corrected the database URL to use the service name defined in docker-compose.yml
SQLALCHEMY_DATABASE_URL = "mysql://user:1234@mysql8/sila"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
