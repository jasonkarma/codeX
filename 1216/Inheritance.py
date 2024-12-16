class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"{self.title}, Author: {self.author}, Year: {self.year}")

class Ebook(Book):
    def __init__(self, title, author, year, file_size, file_format):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.file_format = file_format

    def display_ebook_info(self):
        print(f"{self.title}, Author: {self.author}, Year: {self.year}, File Size: {self.file_size}MB, File Format: {self.file_format}")

book=Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
ebook= Ebook("To kill a mockingbird", "Harper Lee", 1960, 2.5, "PDF")

book.display_info()
print()
ebook.display_ebook_info()
