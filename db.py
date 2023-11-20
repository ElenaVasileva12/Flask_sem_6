import databases
import sqlalchemy
from fastapi import FastAPI


DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(32)),
    sqlalchemy.Column("description",sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Float(20))
)

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(32)),
    sqlalchemy.Column("lastname",sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password",sqlalchemy.String(256))
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("id_users", sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column("id_products", sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column("data_order", sqlalchemy.Date()),
    sqlalchemy.Column("status", sqlalchemy.String(128))
)


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)