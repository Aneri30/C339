from abc import ABC,abstractmethod
#here abc is abstract base class
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    #a method with an empty body , if you dont know the logice you declare method 
    # abstract and the class inherit the abstract method would have to impement it
    @abstractmethod
    def calcArea(self):
        pass

# JSON example
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape,JSONify):
    def __init__(self,radius):
        super().__init__()
        self.radius =radius
    
    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{\"Circle\" :{str(self.calcArea())} }}"
    
class Square(GraphicShape,JSONify):
    def __init__(self,side):
        super().__init__()
        self.side =side
    
    def calcArea(self):
        return (self.side ** 2)
    
    def toJSON(self):
        return f"{{\"Square\" :{str(self.calcArea())} }}"

c =Circle(10)
s =Square(8)
print(c.calcArea())
print(s.calcArea())
print(c.toJSON())
print(s.toJSON())