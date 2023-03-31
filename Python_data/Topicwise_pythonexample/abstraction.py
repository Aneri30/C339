from abc import ABC,abstractmethod
#abc is a Abstract Base Class
class GraphicsShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicsShape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def calcArea(self):
        return 3.14 *(self.radius ** 2)
    
c = Circle(10)
print(c.calcArea)