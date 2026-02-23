#Savings Account
class SavingsAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("After Deposit Balance: ",self.balance)

class Interest(SavingsAccount):
    def add(self):
        interest = self.balance * 0.10 #10%
        self.balance += interest
        print("interest: ",interest)
        print("After Interest", self.balance)

a=Interest(3000)
a.deposit(2000) #from parent class
a.add() #from child class

#Multi level
#parent
class SavingsAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("After Deposit Balance: ",self.balance)
#child
class Interest(SavingsAccount):
    def add(self):
        interest = self.balance * 0.10 #10%
        self.balance += interest
        print("interest: ",interest)
        print("After Interest", self.balance)
#grand child
class Bonus(Interest):
    def bonus(self):
        b_amount = 500
        self.balance += b_amount
        print("Final Balance: ", self.balance)

b = Bonus(10000)
b.deposit(5000)
b.add()
b.bonus()

#Represents shapes its Area , Perimeter
import math
#parent class
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    def perimeter(self):
        pass
#Child Circle
class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius
        self.c_area = math.pi * self.radius * self.radius
        self.c_perimeter = 2 * math.pi * self.radius

    def display(self):
        print(self.c_area)
        print(self.c_perimeter)
#Child Square
class Square(Shape):
    def __init__(self,side):
        self.side= side
        self.s_area = self.side * self.side
        self.s_perimeter = 4*self.side

    def display(self):
        print(self.s_area)
        print(self.s_perimeter)
#child Triangle
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.t_perimeter = self.a + self.b + self.c
        s = self.t_perimeter/2
        self.t_area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def display(self):
        print(self.t_perimeter)
        print(self.t_area)

C = Circle(5)
S = Square(4)
T = Triangle(3,4,5)
C.display()
S.display()
T.display()

#Vehicle
class Vehicle:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    def display(self):
        print(self.name)
        print(self.speed)
class Bus(Vehicle):
    pass
b = Bus("Travels",70)
b.display()

#Vehicle without Variable and method
class Vehicle2:
    pass
v =Vehicle2
print("Vehicle object was created")


