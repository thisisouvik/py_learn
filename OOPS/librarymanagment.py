class Library:
    def __init__(self):
        self.books=[]
        self.nobooks=0

    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def show(self):
        print(f"Name of book {self.books} and number of book {self.nobooks}")

l1=Library()
l1.addbook("Harry Potter")
l1.addbook("King")
l1.addbook("Harry 2")
l1.show()