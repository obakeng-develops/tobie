from typing import Optional, List
from fastapi import FastAPI, HTTPException
from models.models import User_Pydantic, UserIn_Pydantic, UserLogin
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()

# User Routes


@app.get("/v1/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(UserLogin.all())


@app.post("/v1/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await UserLogin.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)

# Product Routes

# Store Routes

# Notification Routes
# AuditLog Routes

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={"models": ["models.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
