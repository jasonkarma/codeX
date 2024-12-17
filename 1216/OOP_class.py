#Create a class called Book with the following attributes: title author year.
#Encapsulation
class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title
    def get_author(self):
        return self.__author
    def set_author(self, author):
        self.__author = author
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year

#Add a method display_info() that prints the book details using f strings.
    def display_info(self):
        print(f"{self.get_title()}, Author: {self.get_author()}, Year: {self.get_year()}")

#Create Objects: Create 2 book objects with sample data.
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

#Call the display_info() method on both objects.
book1.display_info()
book2.display_info()

book1.set_title("The Great Gatsby")
book1.set_year(1931)

book2.get_author()

print("\nAfter updating book1:")
book1.display_info()


