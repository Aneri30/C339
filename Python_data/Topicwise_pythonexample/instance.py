# Class
class Book:  

    def __init__(self, title,pages,author,price,secret): # with secret parameter
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        # self.__secret = "This is the book"  #This the one way to declare without passing parameter
        self.__secret = secret + "has" + author # using secret parameter (It is bad practice to use __secret)

    def __str__(self):
        #return f"{self.title} by {self.pages} {self.price}"
        print("the object with name %s has: \ntitle: %s \nprice: %d" %(self.__name__, self.title, self.price))

    def __reprr__(self):
        return f"{self.title} by {self.author} has {self.pages} pages and the cost is {self.price}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, {self.pages}, {self.author}, {self.price}, {self.__secret})"

    def display(self):
       print("title %s\n pages %s \n author %s \n price %d \n " %(self.title,self.pages,self.author,self.price))

    #Optional attribute
    def setDiscount(self,amount):
        self._discount = amount # if we don't want an attribute to be defined as default in init method we can use _variablename for that

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else: 
            return self.price

    # if we need to access attribute we need get method
    def getTitle(self):  #getter method
        return self.title
    
    def setTitle(self,title): #setter method
        self.title = title

    def __eq__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Can\'t compare a non book object to a book object")
        else:
            return (self.title == value.title and self.author == value.author)

class Car:
    def __init__(self,name):
        self.name= name

# TODO create book instance variable
b1 = Book("Title1", 156, "Anna", 150, "Book")
#print(b1.getTitle())
#b1.setTitle("New Title")
#print(b1.getTitle())
#print(b1.getPrice())
#b1.setDiscount(0.05)
#print(b1.getPrice())
b2 = Book("Title2", 200, "Daina", 250, "Books")
b3 = Book("Title1", 156, "Anna", 250, "Book")
c1 = Car("BMW")
print("Comparision is ", b1 == b3)
#print(b2.getTitle())
#print(b2.getPrice())
#print(b1._Book__secret)

# deleting the attribute from instance variable
# del b1.price

#deleting the object itself
# del b1

#b2.display() # To display variable name and value

#print(str(b2)) # to display values using __str__ function

print(repr(b2))


