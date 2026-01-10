class Person:
    def __init__(self, name,    salary):
        self.name = name
        self.salary = salary

peter = Person("Peter", 2700)
john = Person("John", 3000)

peter.salary = 2700
print(peter.salary)
print(john.salary)