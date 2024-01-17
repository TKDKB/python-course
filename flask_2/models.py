from sqlalchemy import Column, Integer, String, Float, ForeignKey, select, Text, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import uuid
from datetime import datetime


dsn = "sqlite:///test.db"

engine = create_engine(dsn, echo=True)

session = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(64), unique=False, nullable=False)
    content = Column(Text, unique=False, nullable=False)
    created_at = Column(DateTime)

    def __str__(self):
        return f"Note: {self.uuid}"


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)




