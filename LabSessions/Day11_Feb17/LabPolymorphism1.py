#1.Create a Shape class with method area(). Implement Circle and Rectangle.
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [Circle(4),Rectangle(4, 6)]
for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.area()}")

#2. Demonstrate method overloading using default arguments.
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    def sub(self,a, b=0, c=0):
        return a - b - c
cal = Calculator()
print("Add 1 number:", cal.add(5))
print("Add 2 numbers:", cal.add(5, 10))
print("Add 3 numbers:", cal.add(5, 10, 15))
print("Sub 2 numbers:", cal.sub(15, 5))
print("Sub 3 numbers:", cal.sub(20, 15, 5))

#3.Demonstrate operator overloading (__add__).
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, Account):
            return self.balance + other.balance
        else:
            return NotImplemented

    def display(self):
        print(f"Holder: {self.holder}, Balance: {self.balance}")

a1 = Account("Prasad", 10000)
a2 = Account("Rahul", 5000)
a1.display()
a2.display()
total_balance = a1 + a2
print("Total Balance:", total_balance)

#4.Create Engine class and use it inside Car class.
class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type
    def display_engine(self):
        print(f"Engine Type: {self.engine_type}, Horsepower: {self.horsepower} HP")

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine
    def display_car(self):
        print(f"Car: {self.brand} {self.model}")
        self.engine.display_engine()

engine = Engine(150, "Petrol")
car = Car("Hyundai", "Creta", engine)
car.display_car()

#5.Create Team class that contains multiple Player objects.
class Player:
    def __init__(self, name, Style):
        self.name = name
        self.Style = Style

    def display_player(self):
        print(f"Player: {self.name}, Style: {self.Style}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_team(self):
        print(f"Team: {self.team_name}")
        print("Players:")
        for player in self.players:
            player.display_player()

p1 = Player("Prasad", "Right hand batting")
p2 = Player("Ravi", "bowler")
p3 = Player("Karthik", "left hand batting")

team1 = Team("Eagles")
team1.add_player(p1)
team1.add_player(p2)
team1.add_player(p3)

team1.display_team()
