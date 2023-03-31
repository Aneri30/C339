# Polymorphism
class Bikes:
    def __init__(self, name):
        self.name = name

    def max_speed(self):
        print('Bike maximum speed is 200')

    def seats(self):
        print('Bike has maximum two seats')

class Cars:
    def __init__(self, name):
        self.name = name

    def max_speed(self):
        print('Car maximum speed is 350')

    def seats(self):
        print('Car has maximum four seats')

def speciality(vehicle):
    vehicle.max_speed()
    vehicle.seats()


bike = Bikes("Ducati")
car = Cars("BMW")

speciality(bike)
speciality(car)

