#07/03/23
from dataclasses import dataclass,field

@dataclass
class Person:

    name:str 
    height:float
    gender:str  
    weight:float
    age:int = field(default=20) # to set default value

p1 = Person("Anna","female",50)
print(p1.__dict__)


"""
from dataclasses import dataclass,field
import random

def pages_check(e):
#write a code to connect database or get input from cache
#sql query to connect databade and get the output and push it back to the default_factory 
    return e + int(random.randint(0,5))

#Immutable class cannot be alter by anyone
@dataclass(frozen=True)
class Book:

    title:str
    author:str
    pages:int = field(default_factory= lambda: pages_check(5))
    price:float= field(default=20)
    def __post_init__(self): #if we use frozen = true we have to remove this __post_init__ function
        self.description = f"{self.title} by {self.author}"

b1 = Book("asas","asa",32,21.2)
b2 = Book("asas","asa",32,21.2)

print(b1 ==b2)
print(b1.__dict__)

"""