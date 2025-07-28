from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from backend.core.config import settings


engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


def create_tables():
    Base.metadata.create_all(bind=engine)
