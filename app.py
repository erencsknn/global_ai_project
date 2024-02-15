from book import Book
from libary import Libary
import streamlit as st

book_3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", 180, 1)
book_4 = Book("The Catcher in the Rye", "J.D. Salinger", "1951", 224, 1)
book_5 = Book("To Kill a Mockingbird", "Harper Lee", "1960", 281, 1)
book_6 = Book("1984", "George Orwell", "1949", 328, 1)
book_7 = Book("Brave New World", "Aldous Huxley", "1932", 311, 1)
class App:
    def __init__(self):
        
        self.libary_1 = Libary('books.txt')
        self.run()

    def run(self):
        st.write("*** MENU ***")
        menu_options = ["List Books", "Add Book", "Remove Book"]
        choice = st.selectbox("Choose an option:", menu_options)

        if choice == "List Books":
            self.list_books()
        elif choice == "Add Book":
            self.add_book_form()
        elif choice == "Remove Book":
            self.remove_book()

    def list_books(self):
        submitted = st.button("List Books")
        if submitted:
            books_list_md = self.libary_1.list_all_books()
            st.markdown(books_list_md, unsafe_allow_html=True)


    def add_book_form(self):
        with st.form("add_book_form"):
            title = st.text_input("Title")
            author = st.text_input("Author")
            release_date = st.date_input("Release Date")
            number_of_pages = st.number_input("Number of Pages", min_value=1)
            book_count = st.number_input("Book Count", min_value=0)
            submitted = st.form_submit_button("Add Book")
            if submitted:
                book = Book(title, author, release_date, number_of_pages, book_count)
                st.write(self.libary_1.add_book(book))
               

    def remove_book(self):
        with st.form("remove_book_form"):
            title = st.text_input("Title")
            submitted = st.form_submit_button("Remove Book")
            if submitted:
                st.write(self.libary_1.remove_book(title))
            
