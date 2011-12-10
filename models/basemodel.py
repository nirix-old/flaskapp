from db import Db
from peewee import Model, PrimaryKeyField

class BaseModel(Model):
    class Meta:
        database = Db.database