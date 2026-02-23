# 3 different books
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author =author

    def display(self):
        print(self.title, self.author)
        print(self.title, self.author)

book1 =Book("Slayer","Arjun")
book2 = Book("Potter", "Harry")

book1.display()
book2.display()

#Class Rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length =length
        self.width = width
        self.area = length*width
        self.perimeter = 2*(length+width)

    def display(self):
        print(self.area)
        print(self.perimeter)

rectangle = Rectangle(11,8)
rectangle.display()

#Representing a Circle
import math
class Circle:
    def __init__(self,radius):
        self.radius =radius
        self.area = math.pi*self.radius*self.radius
        self.perimeter = 2*math.pi*self.radius

    def display(self):
        print(self.area)
        print(self.perimeter)

c = Circle(6)
c.display()

#Person class and age
from datetime import date
class Person:
    def __init__(self,name,countrty,dob):
        self.name =name
        self.country = countrty
        self.dob = dob
    def age(self):
        present = date.today().year
        self.p_age = present-self.dob
    def display(self):
        self.age()
        print(self.name)
        print(self.country)
        print(self.p_age)
a = Person("Prasad", "india", 2001)
a.display()

