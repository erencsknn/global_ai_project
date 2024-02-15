class Book:
    def __init__(self,title,author,releasedate,numberofpages,book_count=1):
        self.title = title
        self.author = author
        self.releasedate = releasedate
        self.numberofpages = numberofpages
        self.book_count = book_count
    def __str__(self):
        return f'{self.title} by {self.author} released in {self.releasedate} with {self.numberofpages} pages'
    
    
    
    
        
