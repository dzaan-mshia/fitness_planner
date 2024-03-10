from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Define the database URL with username and password
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345678@localhost:5433/fitness_planner"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for ORM models
Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_session():
    db_session: Session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
