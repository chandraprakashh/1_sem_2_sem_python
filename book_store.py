# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:09:54 2019

@author: hp
"""

class BookStore:
    noOfBooks = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        BookStore.noOfBooks += 1

    def bookInfo(self):
        print("Book title:", self.title)
        print("Book author:", self.author,"\n")

# Create a book store
b1 = BookStore("Automate the Boring Stuff with Python", "Al Sweigart")
b2 = BookStore("Effective Python: 59 Specific Ways to Write Better Python", "Brett Slatkin")
b3 = BookStore("Learning Python", "Mark Lutz and David Ascher")
b4 = BookStore("Learn to Program with Python 3"," Irv Kalb")

# call member functions for each object
b1.bookInfo()
b2.bookInfo()
b3.bookInfo()
b4.bookInfo()
 
print("BookStore.noOfBooks:", BookStore.noOfBooks)