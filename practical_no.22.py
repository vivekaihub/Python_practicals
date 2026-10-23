#library management system
import json
import os

FILE_NAME = "library.json"

# Load books from file
def load_books():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error reading file. Starting with empty library.")
    return {}

# Save books to file
def save_books():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(books, file, indent=4)
    except OSError:
        print("Error saving library data.")

# Add a new book
def add_book():
    book_id = input("Enter Book ID: ")

    if book_id in books:
        print("Book ID already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

    save_books()
    print("Book added successfully!")

# Display all books
def display_books():
    if not books:
        print("No books available.")
        return

    print("\n--- Library Books ---")

    for book_id, book in books.items():
        status = "Available" if book["available"] else "Issued"

        print(f"ID: {book_id}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Status: {status}")
        print("-" * 30)

# Search for a book
def search_book():
    book_id = input("Enter Book ID to search: ")

    if book_id in books:
        book = books[book_id]
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", "Available" if book["available"] else "Issued")
    else:
        print("Book not found!")

# Issue a book
def issue_book():
    book_id = input("Enter Book ID to issue: ")

    if book_id not in books:
        print("Book not found!")
    elif not books[book_id]["available"]:
        print("Book is already issued!")
    else:
        books[book_id]["available"] = False
        save_books()
        print("Book issued successfully!")

# Return a book
def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id not in books:
        print("Book not found!")
    elif books[book_id]["available"]:
        print("This book has not been issued.")
    else:
        books[book_id]["available"] = True
        save_books()
        print("Book returned successfully!")

# Main program
books = load_books()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Thank you for using Library Management System!")
        break
    else:
        print("Invalid choice! Please try again.")
