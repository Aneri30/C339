# Class
class Book:  

    def __init__(self, title): 
        self.title = title

    # if we need to access attribute we need get method
    def getTitle(self):  #getter method
        return self.title
    
    def setTitle(self,title): #setter method
        self.title = title

# TODO create book instance variable
b1 = Book("Title1")
print(b1.getTitle())
b1.setTitle("New Title")
print(b1.getTitle())
b2 = Book("Title2")
print(b2.getTitle())