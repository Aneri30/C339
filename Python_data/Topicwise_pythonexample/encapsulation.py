"""
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
"""
#Encapsulation 
class Logincredentials:
    def __init__(self):
        self.username = "Aneri"
        self.__password = "abcd123"

    def newpass(self):
        print(format(self.__password))

    def setnewpassword(self, newpassword):
        self.__password = newpassword

lc = Logincredentials()
print(lc.username)
lc.newpass()

lc.__password="abcde123"
lc.newpass()

lc.setnewpassword("aneri123")
lc.newpass()
