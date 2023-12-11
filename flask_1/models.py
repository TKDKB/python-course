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
    created_at = Column(DateTime, default=datetime.now())


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def add_users(connection, title: str, content: Text):
    # Создали объект python. В базе его нет!
    note = Note(title=title, content=content)
    # Добавим в таблицу запись через подключение
    connection.add(note)
    connection.commit()




