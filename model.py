from pydantic import BaseModel, Field
from datetime import date
import sqlalchemy

class Product(BaseModel):
  #  __tablename__ = 'products'
    id: int
    title: str=Field(..., min_length=2)
    description: str = Field(default=None)
    price: float = Field(gt=0, le=100000)

class ProductIn(BaseModel):
    title: str=Field(..., min_length=2)
    description: str = Field(default=None, title="Description",max_length=1000)
    price: float = Field(title="Price", gt=0, le=100000)



class User(BaseModel):
   # __tablename__ = 'users'
    id: int
    firstname: str = Field(title="Firstname", max_length=50)
    lastname: str = Field(title="Lastname", max_length=50)
    email: str=Field(..., max_length=128)
    password: str=Field(..., min_length=5)

class UserIn(BaseModel):
    firstname: str=Field(..., min_length=2)
    lastname: str =Field(...,min_length=2)
    email: str=Field(..., max_length=128)
    password: str=Field(..., min_length=5)


class Order(BaseModel):
    id: int
    id_users: int
    id_prodects: int
    data_order: date = Field(..., format="%Y-%m-%d")
    status: str=Field(..., min_length=2)

class OrderIn(BaseModel):
    id_users: int
    id_prodects: int
    data_order: date = Field(..., format="%Y-%m-%d")
    status: str=Field(..., min_length=2)