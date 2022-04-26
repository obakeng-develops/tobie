from typing import Optional
from fastapi import FastAPI, HTTPException
from models.models import User_Pydantic, UserIn_Pydantic, User
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/v1/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1/users", response_modelList[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())


@app.get("/v1/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/v1/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={"models": ["models.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
