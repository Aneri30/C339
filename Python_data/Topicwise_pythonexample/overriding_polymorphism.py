class Person:
      def __init__(self, firstname='Jinesh', lastname='Ranawat', age=96, country='England', city='London'):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            self.country = country
            self.city = city
            self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
            self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('Python')
p1.add_skill('MATLAB')
p1.add_skill('R')
p2 = Person('Ben', 'Doe', 30, 'Finland', 'Tampere')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
class Student(Person):
    def __init__ (self, firstname='Jinesh', lastname='Ranawat',age=96, country='England', city='London', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
        
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Arthur', 'Curry', 33, 'England', 'London','male')
s2 = Student('Emily', 'Carter', 28, 'England', 'Manchester','female')
print(s1.person_info())
s1.add_skill('HTML')
s1.add_skill('CSS')
s1.add_skill('JavaScript')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)