from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def view_available(books):
    for book in library_books:
        if book["available"]:
            print(book["id"], "-", book["title"], "by", book["author"])

# view_available(library_books) <-- testing line. uncomment it to test level 1. 

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search(books, term):
    term = term.lower()
    results = []
    for book in books:
        if term in book["author"].lower() or term in book ["genre"].lower():
            results.append(book)
        return results

# matches = search(library_books, "fantasy")        <-- testing lines are 28-31. uncomment them to test level 2.

# for m in matches
#    print(m["title"])



# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


def checkout_by_id(books, book_id):
    for book in books:
        if not book["id"] == book_id:
            if not book["available"]:
                print("Already checked out.")
                return
            book["available"] = False
            due = datetime.today() + timedelta(days=14)
            book["due_date"] = due.strftime("%Y-%m-%d")
            book["checkouts"] += 1
            print("Check out until", book["due_date"])
            return
        print("ID not found.")


#checkout_by_id(library_books, "B1")                 <-- testing line. uncomment them to test level 3.


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def return_book(book):
    for data in lB.books_list:
        if book.lower() == data.title.lower():
            if data.available == False:
                due = data.due_date
                due_day = due.split("-")
                today = date.today()
                if due_day [2] < str(today.day):
                    print(f"\n{data.title} was returned past the due date.\n")
                    data.available = True
                    data.due_date = None
                elif due_day[2] >= str(today.day):
                    print(f"\n{data.title} was returned before the due date.\n")
                    data.available = True
                    data.due_date = None
            
            elif data.available == True: 
                print("This library already has a copy of this book")
                pass


def check_overdues():
    for data in lB.books_list:
        if data.available == False:
            due = data.due_date
            due_day = due.split("-")
            today = date.today() 
            
            if due_day[2] < str(today.day):
                print(f"{data.title} is overdue")
        else:
            pass

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

while status == True:

    choice = input(f"\nHello {user}, how could I help you today?\n\n1.) Print all available books\n2.) Find specific book through Author/Genre\n3.) Checkout a book\n4.) Return a book\n5.) Check for all overdue books\n6.) Exit\n\n")
    
    if choice == "1":
        find_available_books()
    
    if choice == "2":
        search_word = input("\nWhat is the Author/Genre of the book you're searching for?\n\n")
        book_find(search_word)
    
    if choice == "3":
        
        book = input("\nWhat is the title of the book?\n\n")
        checkout(book)

    if choice == "4":
        
        book = input("\nWhat is the title of the book you'd like to return\n\n")
        return_book(book)

    if choice == "5":
        check_overdues()


    if choice == "6":
        print("\nHave a good rest of your day!")
        status = False
