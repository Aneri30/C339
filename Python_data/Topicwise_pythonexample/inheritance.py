"""
class Book:
    def __init__(self,title,author,pages,price):
        self.title=title
        self.author=author
        self.price=price
        self.pages=pages
class Magzine:
    def __init__(self,title,publisher,period,price):
        self.title=title
        self.price=price
        self.publisher=publisher
        self.period=period

class NewsPaper:
    def __init__(self,title,publisher,period,price):
        self.title=title
        self.price=price
        self.publisher=publisher
        self.period=period

b1= Book("a,sadhkjs",12,12)
m1= Magzine("123sa","132sad",21,"Montly")
n1= NewsPaper("123sa","132sad",21,"Montly")
print (b1.__dict__)
print (m1.__dict__)
print (n1.__dict__)
"""


class Publication:
    def __init__(self,title,price):
        self.title=title
        self.price=price

class Periodical(Publication):
    def __init__(self,title,publisher,period,price):
        super(). __init__(title,price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self,title,price,author,pages):
        super() .__init__(title,price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, publisher, period, price)

class NewsPaper(Periodical):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, publisher, period, price)

b1= Book("Dark", 12, "sadhkjs",12)
m1= Magazine("123sa","132sad","Monthly",200)
n1= NewsPaper("123sa","132sad","Monthly",200)
print(issubclass(Magazine,Publication))   #like transitivity property
print(issubclass(Magazine,object)) 
print(isinstance(m1,object))

print (b1.__dict__)
print (m1.__dict__)
print (n1.__dict__)