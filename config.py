import os
from models import db, Book

def config():
    if not os.path.exists("backups"):
        os.mkdir("backups")

    if not os.path.exists("data"):
        os.mkdir("data")

    if not os.path.exists("exports"):
        os.mkdir("exports")

    db.connect()
    db.create_tables([Book])



