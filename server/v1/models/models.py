from tortoise.models import Model
from tortoise import fields, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator


class UserLogin(Model):
    """
    The user login model
    """
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
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


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(
    User, name="User", exclude_readonly=True)
