class Book:
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.discount =0.1

    def __str__(self):
        return f"{self.title} {self.author} {self.price}"
    
    # call() function
    def __call__(self,title,author,pages,price):
        self.title=title
        self.author=author
        self.price=price
        self.pages=pages
    
b1 = Book("ware and peace","leo tolsty",32332,39.65)
b2 = Book("the catcher in rye","JD",322,29.65)

print(b1)
b1("new ware and peace","new leo tolsty",1,15)
b1("1new ware and peace","1new leo tolsty",11,115)

print(b1)  