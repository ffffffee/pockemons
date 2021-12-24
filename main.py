class Library:
    def __init__(self):
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
    def removeBook(self,name):
        for i in range(len(self.books)):
            if self.books[i].name==name:
                self.books.remove(self.books[i])
                break
    def printAllBooks(self):
        if len(self.books)==0:
            print("No books")
        else:
            for book in self.books:
                print("book's name: {}".format(book.name))
                print("book's autor: {}".format(book.autor))
                print("book's price: {}".format(book.price))
                print("book's number of pages: {}".format(book.number_of_pages))
                if self.books.index(book)!=len(self.books)-1:
                    print()

class Book:
    def __init__(self,name, autor, price, number_of_pages):
        self.name=name
        self.autor = autor
        self.price = price
        self.number_of_pages = number_of_pages


class Autor:
    def __init__(self):
        self.autors_books={}
    def AddBook(self,autors_name, books_name):
        if autors_name not in self.autors_books:
            self.autors_books[autors_name]=[books_name]
        else:
            self.autors_books[autors_name].append(books_name)
    def ShowAutorsBooks(self,autor_name):
        print(" ".join(self.autors_books[autor_name]))



library=Library()
autors=Autor()
while True:
    command = input("Enter a command: ")
    if command == "exit":
        break
    elif command=="add book":
        name=input("Enter book's name: ")
        autor=input("Enter book's autor: ")
        price=input("Enter book's price: ")
        number_of_pages=input("Enter number of pages: ")
        book=Book(name,autor,price,number_of_pages)
        library.addBook(book)
        autors.AddBook(autor,name)
        print("Book was added successfully")
    elif command=="remove book":
        name=input("Enter book's name: ")
        library.removeBook(name)
        print("Book was removed successfully")
    elif command=="print all books":
        library.printAllBooks()
    elif command=="print autor's books":
        autors_name=input("Enter autor's name: ")
        autors.ShowAutorsBooks(autors_name)
    else:
        print("This is not a command")


