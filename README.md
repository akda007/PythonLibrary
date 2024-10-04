# Book Library Management System Documentation

## Overview
This project is a command-line book management system built with Python. It allows users to manage a database of books, including features like adding new books, viewing registered books, updating book prices, searching books by author, and exporting the database to CSV. The database is implemented using **SQLite** and managed through **Peewee ORM**.

---

## Dependencies

### Python Libraries
- **peewee**: ORM for interacting with SQLite.
- **inquirer**: For command-line interactive menus.
- **tabulate**: For displaying tabular data in a human-readable format.
- **pandas**: For data manipulation and exporting to CSV.
- **datetime**: For handling date operations, used for CSV file naming.

You can install the dependencies using:

### Option (venv)

- **Create a venv** 
```bash
python -m venv .venv
```
**Activate the venv**

- **CMD:**
```bash
.venv\Scripts\activate
```
- **Powershell:**
```bash
.\.venv\Scripts\activate
```

**Install the dependencies:**
```bash
pip install -r requirements.txt
```

---

## How to Run

1. Ensure you have the required dependencies installed.
2. Run the main script:

```bash
python main.py
```

This will initialize the database and prompt you with the menu to start managing books.

---

## Project Structure

```plaintext
.
├── config.py
├── controller.py
├── main.py
├── models.py
└── database
    └── library.db (auto-created)
```

- **config.py**: Contains the setup logic for initializing the project, including creating directories and database setup.
- **controller.py**: Contains the core logic for managing books in the database (CRUD operations) and exporting data to CSV.
- **main.py**: The main entry point of the application with the user interface logic, using inquirer to prompt for actions.
- **models.py**: Defines the structure of the database using Peewee ORM with a `Book` model.
- **database**: This folder contains the SQLite database file (`library.db`).

---

## config.py

### Purpose
This script handles the initial configuration of the project, ensuring that necessary directories exist and initializing the SQLite database.

### Functions
- **config()**:
  - Creates two directories if they don't already exist:
    - `database/`: stores the SQLite database.
    - `exports/`: stores exported CSV files.
  - Connects to the SQLite database and creates the `Book` table if it doesn't exist.

---

## controller.py

### Purpose
This file contains the core logic for managing the book records in the database and exporting the data to CSV files.

### Functions
- **create_book(title: str, author: str, price: float, year: int)**:
  - Adds a new book to the database.
  
- **get_books(author=None)**:
  - Fetches all books from the database. If an author is provided, it returns only the books matching the author's name.

- **update_price(book_id: int, price: float)**:
  - Updates the price of a book by its `id`.

- **remove_book(book_id: int)**:
  - Deletes a book from the database by its `id`.

- **export_to_csv()**:
  - Exports all book records into a CSV file inside the `exports/` directory. If the number of exported files exceeds 5, it deletes the oldest one.

---

## main.py

### Purpose
The main script that acts as the user interface, where users can interact with the system through a command-line menu.

### Functions
- **menu()**:
  - Uses `inquirer` to display a menu for users to select options such as adding, viewing, updating, or removing books, as well as exporting the database.
  
### Available Options
1. **Add New Book**: Prompts for book details and adds a new entry to the database.
2. **Show All Registered Books**: Displays all books in a table format.
3. **Update the Price of a Book**: Prompts for book `id` and updates its price.
4. **Remove a Book**: Prompts for book `id` and removes it from the database.
5. **Search Books by Author**: Searches and displays books matching the given author.
6. **Export Database**: Exports the database to a CSV file in the `exports/` folder.
7. **Close**: Exits the program.

---

## models.py

### Purpose
This file defines the structure of the database using the Peewee ORM. It contains the `Book` model representing the books in the library.

### Models
- **Book**:
  - `id`: Primary key (auto-incrementing).
  - `title`: Title of the book (text field).
  - `author`: Author of the book (text field).
  - `pub_year`: Year of publication (integer field).
  - `price`: Price of the book (float field).

---

## Database

The SQLite database is stored in the `database/` folder as `library.db`. The database is automatically created when the application is first run if it doesn't already exist.

---

## CSV Export

- When exporting data, the application saves a CSV file in the `exports/` directory. 
- The CSV files are named with the current date and a version number (e.g., `03-10-2024_1.csv`).
- Only 5 CSV files are kept at any time; older files are automatically deleted.

---

