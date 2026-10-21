# 📚 Library Management System

A simple, menu-driven **Library Management System** built with Python. This project allows users to manage books, search for titles, and handle borrowing and returning operations through a command-line interface.

## ✨ Features

- ➕ **Add Books:** Add new books with a unique ID, title, and author.
- 📖 **View All Books:** Display the complete book collection and its availability status.
- 🔍 **Search Books:** Find books by title using case-insensitive partial matching.
- 📥 **Borrow Books:** Borrow a book if it is available.
- 📤 **Return Books:** Return previously borrowed books.
- ✅ **Input Validation:** Handle invalid IDs, duplicate book IDs, and empty book information.
- 🛡️ **Error Handling:** Use `try` and `except` to handle invalid numeric input.
- 🔄 **Interactive Menu:** Navigate through the program using a continuous menu.

## 🛠️ Technologies & Concepts

- **Language:** Python
- Variables and dictionaries
- Functions and function calls
- `for` and `while` loops
- Conditional statements (`if`, `elif`, `else`)
- User input with `input()` and type conversion with `int()`
- Exception handling with `try` and `except`
- `break`, `continue`, and `return`
- The `if __name__ == "__main__":` entry-point pattern

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your computer.

- Python: [Download Python](https://www.python.org/downloads/)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/narges-developer/library_management_system.py.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 10 - Library Management System
   ```

3. Run the program:

   ```bash
   python "10 - Library Management System.py"
   ```


## 💻 How to Use

When you run the program, an interactive menu appears:

```text
===== Library Management System =====
1. Add a book
2. Show all books
3. Search for a book
4. Borrow a book
5. Return a book
0. Exit
```

Enter the number corresponding to the operation you want to perform.

| Option | Action |
|---|---|
| 1 | Add a new book |
| 2 | Display all books |
| 3 | Search for a book by title |
| 4 | Borrow an available book |
| 5 | Return a borrowed book |
| 0 | Exit the program |

## 📋 Sample Output

```text
ID: 101
Title: Python Crash Course
Author: Eric Matthes
Status: Available
------------------------------
```

## 📂 Project Structure

```text
10 - Library Management System/
│
├── 10 - Library Management System.py
└── README.md
```


## 🎯 Project Goal

This project was created as a Python programming practice project to strengthen my understanding of functions, dictionaries, loops, input validation, and exception handling through a practical application.

## 🔮 Future Improvements

- Save book data to a file or database.
- Load saved books when the program starts.
- Add a graphical user interface (GUI).
- Track borrowers and borrowing dates.
- Add automated tests for core functions.

## 👩‍💻 Author

**Narges**

- GitHub: [@narges-developer](https://github.com/narges-developer)

---

⭐ If you find this project useful, feel free to explore the code and share your feedback.