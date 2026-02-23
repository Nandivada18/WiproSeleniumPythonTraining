#Constructors - first function of the class when an object of the class is created
#Syntax __init__()
#we can parametrized the constructors
#self is mandatory
#constructive overloading is not supporting directly we can do it using *args
#construc are used

class Student:
    def __init__(self):
        print("Constructor is called")

    def addsum(self):
        print("Adding 2 numbers")
s1 = Student()
s1.addsum()

#parametrized constructors
#self.name is a instance variable or a global variable (belongs to object)
#if we dont assign it to the self.name object will not remember the value
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name,self.salary)

e1 = Employee("Harsha", 50000)
e2 = Employee("Ravi", 656776)
e1.display()
e2.display()

#usinf * args in constructors
#constructors overloading is supported by *args keyword
#we can any number of parameters to the constructor using *args

class Numbers:
    def __init__(self, * args):
        self.values = args

n = Numbers(10,20,30)
print(n.values)

m = Numbers(3,4)
print(m.values)

p = Numbers(3)
print(m.values)

#parent and child constructors
#super keyword for accessing parent constructor

class Parent:
    def __init__(self):
        print("I am the Parent constructor")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child1 contructor")

c = Child1()

class Child2(Child1):
    def __init__(self):
        super().__init__()
        print("I am the child2 contructor")

c = Child2()