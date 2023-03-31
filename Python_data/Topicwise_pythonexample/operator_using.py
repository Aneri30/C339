class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    #these function is created by me

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)
    
    def multiply(self,other):
        x= self.x * other.x
        y = self.y * other.y 
        return Point(x,y)
    
    def divide(self,other):
        x= self.x / other.x
        y= self.y / other.y
        return Point(x,y)
    
  
p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1-p2)   
print(p1==p2)

print(p1.multiply(p2))
print(p2.divide(p1))