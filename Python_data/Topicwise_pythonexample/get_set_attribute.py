class Book:
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.discount =0.1

    def __str__(self):
        return f"{self.title} {self.author} {self.price}"
    
    # getattribute method
    def __getattribute__(self, name: str):
        if(name == "price"):
            p= super().__getattribute__("price")
            d= super().__getattribute__("discount")
            return p-(p * d)
        return super().__getattribute__(name)
    
    # setattr method
    def __setattr__(self, name: str, value: str):
        if(name == "price"):
            if type(value) is not float:
                raise ValueError("value must be a float")
        return super().__setattr__(name, value)

    # getattr method
    def __getattr__(self, name):
        return  name + " is not a variable in class book."
    


b1 = Book("The Humans", "Ray", 200, 250.50)
b2 = Book("The World", "Bay", 400, 400.99)

b1.price = 99.99
print(b1.price)

b2.price = 199.89
print(b2.price)

print(b1.author)
    