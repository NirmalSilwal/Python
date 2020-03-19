# special methods

class Book(object):

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # string representation of object
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book is destroyed')


my_book = Book('Unlimited Power','Anthon Checkov',180)
print(my_book)
print(len(my_book))
del my_book
