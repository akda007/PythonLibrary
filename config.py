import os
from models import db, Book

def config():
    db.connect()
    db.create_tables([Book])

    if not os.path.exists("database"):
        os.mkdir("database")

    if not os.path.exists("exports"):
        os.mkdir("exports")


