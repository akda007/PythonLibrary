from peewee import *
import datetime

db = SqliteDatabase('./database/library.db')


class BaseModel(Model):
    class Meta:
        database = db


class Book(BaseModel):
    id = PrimaryKeyField()
    title = TextField()
    author = TextField()
    pub_year = IntegerField()
    price = FloatField()



