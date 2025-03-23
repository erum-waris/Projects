# Library Manager in Python

# Ek dictionary banayein jisme books store honge
library = {}

# Functions define karein
def add_book():
    """
    Ye function book add karega library mein.
    """
    book_name = input("Book ka naam likhein: ")
    author_name = input("Author ka naam likhein: ")
    library[book_name] = author_name
    print(f"'{book_name}' library mein add ho gayi hai!")

def delete_book():
    """
    Ye function book delete karega library se.
    """
    book_name = input("Delete karne ke liye book ka naam likhein: ")
    if book_name in library:
        del library[book_name]
        print(f"'{book_name}' library se delete ho gayi hai!")
    else:
        print(f"'{book_name}' library mein nahi mili.")

def view_books():
    """
    Ye function library ki books ki list show karega.
    """
    if library:
        print("Library ki books:")
        for book, author in library.items():
            print(f"- {book} by {author}")
    else:
        print("Library khali hai.")

def search_book():
    """
    Ye function book search karega library mein.
    """
    book_name = input("Search karne ke liye book ka naam likhein: ")
    if book_name in library:
        print(f"'{book_name}' library mein mili hai. Author: {library[book_name]}")
    else:
        print(f"'{book_name}' library mein nahi mili.")

# Main program
def main():
    while True:
        print("\n--- Personal Library Manager ---")
        print("1. Book Add Karein")
        print("2. Book Delete Karein")
        print("3. Books Ki List Dekhein")
        print("4. Book Search Karein")
        print("5. Program Se Bahir Niklein")
        
        choice = input("Apna option chunein (1-5): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            view_books()
        elif choice == "4":
            search_book()
        elif choice == "5":
            print("Program se bahir nikle ja rahe hain. Shukriya!")
            break
        else:
            print("Galat option! Dobara try karein.")

# Program run karein
if __name__ == "__main__":
    main()