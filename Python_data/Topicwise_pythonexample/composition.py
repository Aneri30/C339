# Importing Author function from the folder and file name author 
from author import Author
class Book:
    def __init__(self,title,price,author=None):
        self.title = title
        self.price = price
        self.author = author

        self.chapter=[]
    def add_chapter(self,chapterName,pages):
        self.chapter.append((chapterName,pages))

a1= Author("Ray", "Bay")
b1= Book("Dreams", 200, a1)
b2= Book("Joy", 500, a1)
b1.add_chapter("abc",100)
b1.add_chapter("gbc",100)

print(b1.title)
print(a1.fname, a1.lname)