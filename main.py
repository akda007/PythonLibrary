from config import config
from controller import *
import inquirer
import re


def menu():

    questions = [
      inquirer.List('value',
                    message="What size do you need?",
                    choices=[
                        'add  new book',
                        'show all registered books',
                        'Update the price of a book',
                        'remove a book',
                        'Search books by author',
                        'File handling',
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
            for book in books:
                print(book)



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
            for book in books_name:
                print(book)

            print("Search books by author...")

        elif choice == 'File handling':
            export_to_csv("test")
            print("File handling...")


        elif choice == 'close':
            print("Saindo do programa...")
            break

        input ("press enter to continue...")

   # create_book("Livro", "Joao", 10.0, 1999)
    #create_book("Livro2", "Joao", 12.0, 2009)
    #create_book("Livro3", "Pedro", 14.0, 2077)

    #books = get_books()
    #joao_books = get_books("Joao")

    #print("Livros:")
    #print(books)

    #print("Livros do joao:")
    #print(joao_books)

    #remove_book(books[0]["id"])
    #update_price(books[1]["id"], 555.3)
    #books = get_books()
    #print("Livro (new list):")
    #print(books)

    #export_to_csv("test")






