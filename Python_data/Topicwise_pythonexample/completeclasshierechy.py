class Book:
    # define 3 count variable and increment it in instance method , 
    # static method and class method and print it

    #TODO properties defined at classs level shared by all instance variables
    __COUNT=0    #   STATIC and contsnat
    BOOK_TYPES=("HARDCOVER","PAPERBACK","EBOOK")    # STATIC contsnats
    BOOK_CLASSLEVEL_COUNT=0  # static constants
    #TODO __ properties are hidden from other classes
    __booklist = None
    def __init__(self,title,bookType):
        self.title=title
        self.instnce_count=0
        if (not bookType in Book.BOOK_TYPES):
            raise ValueError(f"We dont support the feature you are asking {bookType}")
        else:
            self.booktype=bookType
    
    @staticmethod
    def incrementCount():    #These is not asscoiated with b1 or b2 its asssociated with class name Book
        Book.__COUNT = Book.__COUNT+1
        return Book.__COUNT
        
    
    
    # static methods do not recieve class or instance argument
    @staticmethod
    def getBookList(arg1,arg2):    # these method is sto set something at class level
    
      #  print(Book.BOOK_TYPES)
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    
    @classmethod      # same like setter and getter
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    

    @classmethod
    def returnCount(cls):
        return cls.__COUNT
    
    def setTitle(self,newTitle):
        self.title=newTitle

    def setCount(self):    #   its asscoiated with that b1 instance variable ist not associated Book
        self.count=self.count+1
    

print("Book Types : ", Book.getBookTypes())
b1 = Book("title1","HARDCOVER")
b1.setCount()
b2= Book("title2","PAPERBACK")
b2.setCount()
theBook=Book.getBookList(1,2)
theBook.append(b1)
theBook.append(b2)
print(theBook)



Book.incrementCount()
print(b1.count)
Book.incrementCount()
print(b2.count)
Book.incrementCount()
Book.incrementCount()
print(b1.returnCount())
print(b1.incrementCount())



"""
class Book:
    #TODO properties defined at classs level shared by all instance variables
    BOOK_TYPES=("HARDCOVER","PAPERBACK","EBOOK")
    #TODO __ properties are hidden from other classes
    __booklist = None
    def __init__(self,title,bookType):
        self.title=title
        if (not bookType in Book.BOOK_TYPES):
            raise ValueError(f"We dont support the feature you are asking {bookType}")
        else:
            self.booktype=bookType
    # static methods do not recieve class or instance argument
    @staticmethod
    def getBookList(arg1,arg2):
        print(arg1,arg2)
      #  print(Book.BOOK_TYPES)
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    
    def setTitle(self,newTitle):
        self.title=newTitle
    
#
print("Book Types : ", Book.getBookTypes())
b1 = Book("title1","HARDCOVER")
b2= Book("title2","PAPERBACK")
theBook=Book.getBookList(1,2)
theBook.append(b1)
theBook.append(b2)
print(theBook)
"""