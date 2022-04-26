from tortoise.models import Model
from tortoise import fields, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    """
    The user model
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    def full_name(self) -> str:
        return self.name

    class PydanticMeta:
        computed = ['full_name']


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(
    User, name="User", exclude_readonly=True)


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schema()
