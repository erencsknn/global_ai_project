from book import Book
class Libary:
    def __init__(self,file_name):
        self.file_name = file_name
        self.file = open(file_name, 'a+')
        self.all_books = []
        self.load_books_from_file()
        
    def load_books_from_file(self):
        self.all_books = []
        try:
            with open(self.file_name, 'r') as file: 
                for line in file:
                    title, author, release_date, number_of_pages, book_count = line.strip().split(',')
                    book = Book(title, author, release_date, int(number_of_pages),int(book_count))
                    self.all_books.append(book)
        except FileNotFoundError:
            pass 
               
    def list_all_books(self):
            self.load_books_from_file()
            if not self.all_books:  # Eğer kitap listesi boşsa
                return "No books available."
            books_list_md = "### Book List\n\n"  # Markdown başlığı
            for book in self.all_books:
                books_list_md += f"- **Title:** {book.title}, **Author:** {book.author}, **Book Count:** {book.book_count}\n"
            return books_list_md

                    
    def update_text_from_list(self):
        with open(self.file_name, 'w') as f:
            for book in self.all_books:
                f.write(f'{book.title},{book.author},{book.releasedate},{book.numberofpages},{book.book_count}\n')


    def add_book(self, book):
        if len(self.all_books) >= 300:  # Kütüphane sınırı kontrolü
            return "Library is full"
        for book_add in self.all_books:
            if book_add.title == book.title:
                book_add.book_count += book.book_count
                self.update_text_from_list()
                return f"Book count increased by {book.book_count}"
        self.all_books.append(book)
        self.file.write(f'{book.title},{book.author},{book.releasedate},{book.numberofpages},{book.book_count}\n')
        return "Book added to the list"
       
        
    def remove_book(self, book_value_title):
        book_found = False
        for book in self.all_books:
            if book.title == book_value_title:
                book_found = True
                if book.book_count > 1:
                    book.book_count -= 1
                    self.update_text_from_list()
                    return "The book missing from the list, book count decreased by 1"
                else:
                    self.all_books.remove(book)
                    self.update_text_from_list()
                    return "Book removed from the list"
        if not book_found:
            return 'Book not found or book name is wrong'
        
            
            
     
        
        
            
    
                    
               
        
            
   
            
        
        
    