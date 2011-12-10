from basemodel import BaseModel
from peewee import CharField, PrimaryKeyField, TextField

class Example(BaseModel):
    id = PrimaryKeyField(auto_increment=True)
    title = CharField()