from config import config
from controller import *
import inquirer
from tabulate import tabulate
import re


def menu():

    questions = [
      inquirer.List('value',
                    message="Select a option:",
                    choices=[
                        'add  new book',
                        'show all registered books',
                        'Update the price of a book',
                        'remove a book',
                        'Search books by author',
                        'Export database',
                        'close'
                    ],
                ),
    ]

    return  inquirer.prompt(questions)

if __name__ == "__main__":
    config()


    while True:
        choice = menu()['value']

        if choice == 'add  new book':
            title = input("Book title: ")
            author = input("Author: ")
            price = float(input("Price: "))
            year = int(input("Year of publication: "))
            create_book(title, author, price, year)
            print("Added new book...")


        elif choice == 'show all registered books':
            books = get_books()

            rows = [x.values() for x in books]
            print(tabulate(rows, headers=["Id", "Title", "Author", "Price", "Pub Year"]))


        elif choice == 'Update the price of a book':
            book_id = int(input('Book ID: '))
            new_price = float(input('What is the new price?'))
            update_price(book_id, new_price)
            print("Update the price of a book...")


        elif choice == 'remove a book':
            book_id = int(input('Book ID: '))
            remove_book(book_id)
            print("remove a book...")


        elif choice == 'Search books by author':
            author = input("Author: ")
            books_name = get_books(author)

            rows = [x.values() for x in books_name]
            print(tabulate(rows, headers=["Id", "Title", "Author", "Price", "Pub Year"]))

        elif choice == 'Export database':
            file = export_to_csv()
            print(f'Database exported to: {file}')


        elif choice == 'close':
            print("Saindo do programa...")
            break

        input("\n\npress enter to continue...")
