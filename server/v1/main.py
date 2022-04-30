from typing import Optional, List
from fastapi import FastAPI, HTTPException
from models.models import (
    User_Pydantic,
    UserIn_Pydantic,
    UserLogin,
    Product_Pydantic,
    ProductIn_Pydantic,
    Product,
    Store_Pydantic,
    StoreIn_Pydantic,
    Store,
    Notifications_Pydantic,
    NotificationsIn_Pydantic,
    Notifications,
    AuditLog_Pydantic,
    AuditLogIn_Pydantic,
    AuditLog
)
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()


@app.get("/v1/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(UserLogin.all())


@app.post("/v1/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await UserLogin.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@app.get("/v1/product/all", response_model=List[Product_Pydantic])
async def get_products():
    return await Product_Pydantic.from_queryset(Product.all())


@app.post("/v1/product/", response_model=Product_Pydantic)
async def create_product(product: Product_Pydantic):
    product_obj = await Product.create(**product.dict(exclude_unset=True))
    return await Product_Pydantic.from_tortoise_orm(product_obj)


@app.get("/v1/store/all", response_model=List[Store_Pydantic])
async def get_stores():
    return await Store_Pydantic.from_queryset(Store.all())


@app.post("/v1/store/", response_model=Store_Pydantic)
async def create_store(store: Store_Pydantic):
    store_obj = await Store.create(**store.dict(exclude_unset=True))
    return await Store_Pydantic.from_tortoise_orm(store_obj)

# Notification Routes
# AuditLog Routes

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={"models": ["models.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
