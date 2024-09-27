from models import Book, db
from playhouse.sqliteq import *
import pandas as pd
import os


def create_book(title: str, author: str, price: float, year: int):
    book = Book.create(title=title, author=author, price=price, pub_year=year)
    return book


def get_books(author=None):
    if author is None:
        data = [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "price": book.price,
                "pub_year": book.pub_year
            } for book in Book.select()
        ]
    else:
        data = [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "price": book.price,
                "pub_year": book.pub_year
            } for book in Book.select().where(Book.author.contains(author))
        ]

    return data


def update_price(book_id: int, price: float):
    book = Book.get_by_id(book_id)

    book.price = price

    book.save()

    return book


def remove_book(book_id: int):
    Book.delete_by_id(book_id)


def export_to_csv(filename: str):
    filename = filename.replace(".csv", "")
    books = get_books()

    df = pd.DataFrame(books)

    files = [f for f in os.listdir("./exports/") if os.path.isfile(f'./exports/{f}')]

    num = 0

    if len(files) > 0:
        last_file = files[-1]
        ending = last_file.split("_")[-1]
        num = int(ending.split(".")[0])

    df.to_csv(f"./exports/{filename}_{num + 1}.csv", index=False, sep=';')

    if len(files) > 5:
        os.remove(f"./exports/{files[0]}")

