import streamlit as st  # type: ignore
import base64
import json
import os

# Function to convert local image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set background image using local image
def set_bg_image(image_path):
    base64_image = get_base64_of_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image (replace 'book.png' with your local image path)
set_bg_image("book.png")

# Load library data from a JSON file
def load_library():
    if os.path.exists("library.json"):
        with open("library.json", "r") as file:
            return json.load(file)
    return {}

# Save library data to a JSON file
def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file)

# Initialize session state for the library
if "library" not in st.session_state:
    st.session_state.library = load_library()

# Functions define karein
def add_book():
    """
    This function will add a book to the library.
    """
    st.header("➕ Add Book Here")
    book_name = st.text_input("Enter Book Name:")
    author_name = st.text_input("Enter Author Name:")
    book_image = st.file_uploader("Upload Book Cover Image", type=["jpg", "jpeg", "png"])
    if st.button("Add Book"):
        if book_name and author_name:
            # Save the image file if uploaded
            image_path = None
            if book_image:
                image_path = f"images/{book_name}_{book_image.name}"
                os.makedirs("images", exist_ok=True)
                with open(image_path, "wb") as f:
                    f.write(book_image.getbuffer())
            
            st.session_state.library[book_name] = {"author": author_name, "image": image_path}
            save_library(st.session_state.library)
            st.success(f"'{book_name}' Book has been added in Library 🎉")
        else:
            st.error("Must enter both Book Name and Author Name.")

def delete_book(book_name):
    """
    This function will delete a book from the library.
    """
    if book_name in st.session_state.library:
        # Delete the associated image file if it exists
        if st.session_state.library[book_name]["image"] and os.path.exists(st.session_state.library[book_name]["image"]):
            os.remove(st.session_state.library[book_name]["image"])
        
        del st.session_state.library[book_name]
        save_library(st.session_state.library)
        st.success(f"'{book_name}' Book has been Deleted from Library 🗑️")
    else:
        st.error(f"'{book_name}' Book is not in Library.")

def deleted_book():
    """
    This function will delete a book from the library.
    """
    st.header("🗑️ Delete Book from Here")
    book_name = st.text_input("Delete karne ke liye book ka naam likhein:")
    if st.button("Delete Book"):
        if book_name in st.session_state.library:
            del st.session_state.library[book_name]
            st.success(f"'{book_name}' Book has been Deleted from Library 🗑️")
        else:
            st.error(f"'{book_name}' Book is not in Library.")

def view_books():
    """
    This function will show all the books in the library.
    """
    st.title("📚 Personal Library Manager")
    st.header("📖 View Book List")
    if st.session_state.library:
        st.write("Library books:")
        for book, details in list(st.session_state.library.items()):  # Use list() to avoid runtime modification issues
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"- Book Name: {book} \n - Author Name: {details['author']}")
                if details["image"] and os.path.exists(details["image"]):
                    st.image(details["image"], caption=book, width=100)
            with col2:
                if st.button(f"🗑️Delete {book}"):
                    delete_book(book)
                    st.session_state.library = load_library()  # Reload library after deletion
                    st.rerun()  # Rerun the app to reflect changes
    else:
        st.write("Library is Empty.")

def search_book():
    """
    Search a book in the library.
    """
    st.header("🔍 Search Book Here")
    book_name = st.text_input("Enter Book Name For Searching:")
    if st.button("Search Book"):
        if book_name in st.session_state.library:
            st.success(f"   {book_name}' Book is Here \n  Author: {st.session_state.library[book_name]['author']} 🎉")
            if st.session_state.library[book_name]["image"] and os.path.exists(st.session_state.library[book_name]["image"]):
                st.image(st.session_state.library[book_name]["image"], caption=book_name, width=100)
        else:
            st.error(f"'{book_name}' Book Not Found in Library.")

# Sidebar mein options
st.sidebar.header("Options")
option = st.sidebar.radio(
    "Choose an option:",
    ("📖 View Book List", "➕ Add Book Here", "🔍 Search Book Here","🗑️ Delete Book From Here")
)

# Option ke hisab se function call karein
if option == "📖 View Book List":
    view_books()
elif option == "➕ Add Book Here":
    add_book()
elif option == "🔍 Search Book Here":
    search_book()
elif option == "🗑️ Delete Book From Here":
    deleted_book()