from config import config
from controller import *


if __name__ == "__main__":
    config()

    create_book("Livro", "Joao", 10.0, 1999)
    create_book("Livro2", "Joao", 12.0, 2009)
    create_book("Livro3", "Pedro", 14.0, 2077)

    books = get_books()
    joao_books = get_books("Joao")

    print("Livros:")
    print(books)

    print("Livros do joao:")
    print(joao_books)

    remove_book(books[0]["id"])
    update_price(books[1]["id"], 555.3)
    books = get_books()
    print("Livro (new list):")
    print(books)

    export_to_csv("test")






