class Book:
    def __init__(self, title):
        self.title=title
    
class NewsPaper:
    def __init__(self,name):
        self.name=name

b1= Book("The catcher in rye")
b2=Book("The Grapes of Wrath")
n1 =NewsPaper("The washington post")
n2= NewsPaper("The new yourk times")

print(type(b1))
print(type(b2))

print(type(b1) == type(b2))

print(type(n1) == type(n2))

print(isinstance(b1,Book))
print(isinstance(n1,NewsPaper))

print(isinstance(n2,object))