from sqlalchemy import Column, Integer, String, Float, ForeignKey, select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


dsn = "sqlite:///test.db"

engine = create_engine(dsn, echo=True)

session = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(200), unique=True, nullable=False)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    count = Column(Integer, nullable=False)
    seller_id = Column(Integer, ForeignKey("sellers.id"))


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    count = Column(Integer, nullable=False)


class Seller(Base):
    __tablename__ = "sellers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64), nullable=False)
    phone = Column(String(64), nullable=False, unique=True)


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def add_users(connection):
    # Создали объект python. В базе его нет!
    user = User(username="igor", password="<PASSWORD>", email="igor@mail.com")

    # Добавим в таблицу запись через подключение
    connection.add(user)
    connection.add(
        User(username="user123", password="<PASSWORD>", email="user123@mail.com")
    )
    connection.add(
        User(username="user111", password="<PASSWORD>", email="user111@mail.com")
    )
    connection.add(
        User(username="user999", password="<PASSWORD>", email="user999@mail.com")
    )
    # Подтверждаем добавление!
    connection.commit()


drop_tables()
create_tables()

with session() as conn:
    add_users(conn)  # Добавили пользователей
    conn.add(User(username="user333", password="<PASSWORD>", email="user333@mail.com"))
    conn.commit()





