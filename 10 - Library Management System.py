# ===========================================
# Project: Library Management System
# Description:
# A simple program to manage a library.
#
# Concepts Used:
# - Variables
# - Dictionaries
# - for and while loops
# - Functions
# - if / elif / else
# - input and int
# - try / except
# - continue, return and break
# ===========================================
library = {
    101: {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "available": True
    },
    102: {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "available": False
    }
}

def add_book():
    while True:
        try:
            book_id = int(input("Enter book ID: "))

            if book_id <= 0:
                raise ValueError("ID must be greater than 0.")
        except ValueError as error:
            print(f"Error: {error}")
            continue
        if book_id in library:
            print("Error: Book ID already exists.")
            continue
        book_title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()

        if not book_title or not author:
            print("Error: Title and author cannot be empty.")
            continue
        library[book_id] = {
            "title": book_title,
            "author": author,
            "available": True
        }

        print("Book added successfully!")
        break

def show_books():
    if not library:
        print("No books found.")
        return
    for book_id, book_info in library.items():
        status = (
            "Available"
            if book_info["available"]
            else "Borrowed"
        )
        print(f"\nID: {book_id}")
        print(f"Title: {book_info['title']}")
        print(f"Author: {book_info['author']}")
        print(f"Status: {status}")
        print("-" * 30)

def search_book():
    search_name = input("Enter book title: ").strip().lower()

    if not search_name:
        print("Error: Search title cannot be empty.")
        return
    found = False

    for book_id, book_info in library.items():
        title = book_info["title"].lower()

        if search_name in title:
            status = (
                "Available"
                if book_info["available"]
                else "Borrowed"
            )
            print(f"\nID: {book_id}")
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")
            print(f"Status: {status}")
            print("-" * 30)

            found = True
    if not found:
        print("Book not found.")

def borrow_book():
    while True:
        try:
            book_id = int(input("Enter book ID: "))

            if book_id <= 0:
                raise ValueError("ID must be greater than 0.")
        except ValueError as error:
            print(f"Error: {error}")
            continue
        if book_id not in library:
            print("Error: Book not found.")
            continue
        if library[book_id]["available"]:
            library[book_id]["available"] = False
            print("Book borrowed successfully!")
        else:
            print("Error: This book is already borrowed.")

        break

def return_book():
    while True:
        try:
            book_id = int(input("Enter book ID: "))

            if book_id <= 0:
                raise ValueError("ID must be greater than 0.")
        except ValueError as error:
            print(f"Error: {error}")
            continue
        if book_id not in library:
            print("Error: Book not found.")
            continue
        if not library[book_id]["available"]:
            library[book_id]["available"] = True
            print("Book returned successfully!")
        else:
            print("Error: This book has not been borrowed.")

        break

menu = [
    "1. Add a book",
    "2. Show all books",
    "3. Search for a book",
    "4. Borrow a book",
    "5. Return a book",
    "0. Exit"
]

def main():
    while True:
        print("\n===== Library Management System =====")

        for item in menu:
            print(item)
        try:
            user_selection = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue
        if user_selection == 0:
            print("Goodbye!")
            break
        elif user_selection == 1:
            add_book()
        elif user_selection == 2:
            show_books()
        elif user_selection == 3:
            search_book()
        elif user_selection == 4:
            borrow_book()
        elif user_selection == 5:
            return_book()
        else:
            print("Invalid choice. Select a number from 0 to 5.")

if __name__ == "__main__":
    main()