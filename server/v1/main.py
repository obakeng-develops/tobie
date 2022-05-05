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


@app.get("/v1/users")
async def get_users():
    return await User_Pydantic.from_queryset(UserLogin.all())


@app.post("/v1/users")
async def create_user(user: UserIn_Pydantic):
    user_obj = await UserLogin.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@app.get("/v1/users/{user_id}")
async def get_user(user_id: int):
    response = await User_Pydantic.from_queryset_single(UserLogin.get(id=user_id))
    return {
        "status": "OK",
        "data": response
    }


@app.patch("/v1/users/{user_id}")
async def update_user(user_id: int, update_details: UserIn_Pydantic):
    user = await UserLogin.get(id=user_id)
    update_details = update_details.dict(exclude_unset=True)
    user.first_name = update_details['first_name']
    user.last_name = update_details['last_name']
    user.email = update_details['email']
    await user.save()
    response = await User_Pydantic.from_tortoise_orm(user)
    return {
        "status": "OK",
        "data": response
    }


@app.delete("/v1/users/{user_id}")
async def delete_supplier(user_id: int):
    await UserLogin.get(id=user_id).delete()
    return {
        "status": "OK"
    }


@app.get("/v1/product/all")
async def get_products():
    return await Product_Pydantic.from_queryset(Product.all())


@app.post("/v1/product/{store_id}")
async def create_product(store_id: int, product_details: ProductIn_Pydantic):
    store = await Store.get(id=store_id)
    product = product_details.dict(exclude_unset=True)
    product_obj = await Product.create(**product, store_id=store)
    return await Product_Pydantic.from_tortoise_orm(product_obj)


@app.get("/v1/product/{product_id}")
async def get_product(product_id: int):
    response = await Product_Pydantic.from_queryset_single(Product.get(id=product_id))
    return {
        "status": "OK",
        "data": response
    }


@app.patch("/v1/product/{product_id}")
async def update_product(product_id: int, update_details: ProductIn_Pydantic):
    product = await Product.get(id=product_id)
    update_details = update_details.dict(exclude_unset=True)
    product.product_name = update_details['product_name']
    product.product_price = update_details['product_price']
    product.product_url = update_details['product_url']
    product.product_variant = update_details['product_variant']
    product.product_stock_level = update_details['product_stock_level']
    product.product_image = update_details['product_image']
    product.current_sale = update_details['current_sale']
    await product.save()
    response = await Product_Pydantic.from_tortoise_orm(product)
    return {
        "status": "OK",
        "data": response
    }


@app.get("/v1/store/all")
async def get_stores():
    return await Store_Pydantic.from_queryset(Store.all())


@app.post("/v1/store/")
async def create_store(store: StoreIn_Pydantic):
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
