#1. Create a base class Vehicle and derived class Bike.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine
    def display(self):
        super().display()
        print("Engine CC:", self.engine)

b = Bike("Royal Enfield", "Classic 350", 349)
b.display()

#2. Create Person - Employee - Manager (multilevel inheritance).
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary
    def display_emp(self):
        self.display_person()
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, role):
        super().__init__(name, age, emp_id, salary)
        self.role = role
    def display_manager(self):
        self.display_emp()
        print("Role:", self.role)

c = Manager("Prasad", 25, 21271, 30000, "Tester")
c.display_manager()

#3. Override a method in child class and call parent method using super().
# Parent
class Animal:
    def speak(self):
        print("Animal makes  sound")
# Child
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks") 
d = Dog()
d.speak()
