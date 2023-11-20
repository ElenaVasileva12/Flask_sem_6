from fastapi import FastAPI
import uvicorn
from db import database
import products
import orders
import users

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(products.router, tags=['Product'])
app.include_router(users.router, tags=['User'])
app.include_router(orders.router, tags=['Order'])


if __name__=='__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload = True)