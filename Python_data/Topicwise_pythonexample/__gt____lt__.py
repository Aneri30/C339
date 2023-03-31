# greaterthan and lessthan function in python
class Book:
    def __init__(self,title,author,pages,price):
        self.title=title
        self.author=author
        self.price=price
        self.pages=pages

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    
    #  greater than function
    def __ge__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book with a non book")
        
        return self.price >= value.price
    
    # less than function
    def __lt__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book with a non book")
        
        return self.price < value.price
    
b1 = Book("The Humans", "Ray", 200, 250.50)
b2 = Book("The World", "Bay", 400, 400.99)
b3 = Book("Moral", "Viv", 100, 55.55)
b4 = Book("Pride and Prejudice", "Jane Austen", 250, 66.99)

print(b1 == b3)

#first parameter is self and the second parameter is the value in __gt__ and __lt__
print(b2 >= b1)
print(b2 <= b1)
print(b2 < b1)
print(b4 >= b2)
print(b3 > b4)

books=[b1,b4,b3,b2]
books.sort(reverse=True) # to print the value in descending order and if we need in ascending no need to mention reverse= true
print([book.title for book in books ])