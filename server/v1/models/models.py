from tkinter import TRUE
from tortoise.models import Model
from tortoise import fields, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator


class UserLogin(Model):
    """
    The user login model
    """
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=100, null=True)
    last_name = fields.CharField(max_length=100, null=True)
    email = fields.CharField(max_length=80)
    password_hash = fields.CharField(max_length=128, null=True)
    join_date = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now_add=True)

    def full_name(self) -> str:
        """
        Returns the full name of the user
        """
        return self.first_name + " " + self.last_name

    class PydanticMeta:
        computed = ['full_name']
        exclude = ['password_hash']


User_Pydantic = pydantic_model_creator(UserLogin, name="UserLogin")
UserIn_Pydantic = pydantic_model_creator(
    UserLogin, name="UserLogin", exclude_readonly=True)


class Store(Model):
    """
    Product keeps all information about the saved product
    """
    id = fields.IntField(pk=True)
    store_name = fields.CharField(max_length=255, null=True)
    store_url = fields.CharField(max_length=200, null=True)


Store_Pydantic = pydantic_model_creator(Store, name="Store")
StoreIn_Pydantic = pydantic_model_creator(
    Store, name="Store", exclude_readonly=True)


class Notifications(Model):
    """
    Notifications modeling all notifications to the user
    """
    notification_type = fields.CharEnumField(str, max_length=2)
    notification_priority = fields.CharEnumFiled(str, max_length=2)
    notification_date = fields.DatetimeField(auto_now_add=True)
