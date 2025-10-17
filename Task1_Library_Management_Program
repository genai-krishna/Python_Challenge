# ================================================
# Simple Library Management System
# ================================================
# This program allows the user to:
# 1. Add a new book
# 2. View all books
# 3. Search for a book by title
# 4. Exit the program
# ================================================

# Create an empty list to store books
library = []

# Function to add a new book
def add_book():
    # Ask user for book details
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    # Create a dictionary for each book
    book = {"title": title, "author": author}
    
    # Add book to the library list
    library.append(book)
    
    print("Book added successfully!\n")

# Function to view all books
def view_books():
    if len(library) == 0:
        print("No books in the library.\n")
    else:
        print("Books in library:")
        # Loop through each book and display details
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book['title']} by {book['author']}")
        print()  # Blank line for spacing

# Function to search for a book by title
def search_book():
    search_title = input("Enter the book title to search: ")
    
    # Use a flag to check if book found
    found = False
    
    for book in library:
        if book["title"].lower() == search_title.lower():
            print(f"Book found: {book['title']} by {book['author']}\n")
            found = True
            break
    
    if not found:
        print("Book not found in library.\n")

# Main program loop
while True:
    # Display menu
    print("=== Library Management System ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")
    
    # Get user's choice
    choice = input("Enter your choice: ")
    
    # Match choice to functions
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
