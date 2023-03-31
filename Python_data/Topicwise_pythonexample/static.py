class Employee:
    COMPANY_NAME = "Wiley"
    def __init__(self, name,age,id):
        self.name = name
        self.age = age
        self.id = id

    @classmethod
    def setTitle(self,newTitle):
        self.title=newTitle

e1 = Employee("Aneri", 25, 132)
print(e1.COMPANY_NAME)
print(e1.__dict__) # dictionary of instance variable 
print(Employee.__dict__) 