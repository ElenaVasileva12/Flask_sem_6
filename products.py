# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

from fastapi import APIRouter
from model import Product,ProductIn
from db import products, database

router = APIRouter()

@router.get("/products/", response_model=list[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{product_id}", response_model=Product | None)
async def one_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.post("/products/", response_model=str)
async def creat_product(product: ProductIn):
    query = products.insert().values(
        title=product.title,
        description=product.description,
        price=product.price,
    )
    await database.execute(query)
    return f"Товар добавлен"


@router.put("/products/{product_id}")
async def edit_product(product_id: int, new_product: ProductIn):
    query = (
        products.update()
        .where(products.c.id == product_id)
        .values(
            title=new_product.title,
            description=new_product.description,
            price=new_product.price,
        )
    )
    await database.execute(query)
    return f"Пользователь изменен"


@router.delete("/products/{product_id}")
async def del_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return f"Пользователь удален"


