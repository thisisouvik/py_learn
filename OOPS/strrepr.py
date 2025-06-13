class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"

    def __str__(self):
        return f"{self.title} by {self.author}"

e=Book("Estacacy Fantasy", "Subhranil")
print(str(e))
print(repr(e))