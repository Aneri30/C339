class A:
    def __init__(self):
        super().__init__()
        self.foo="foo"
        self.name= "class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar="bar"
        self.name="class B"

class C(B,A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

c = C()
c.showprops()

"""
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(isinstance(d,Derived)) 

"""