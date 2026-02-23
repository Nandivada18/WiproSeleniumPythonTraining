#1.Method Overriding with inheritance
#parent
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print("Emp salary: ",self.salary)

class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def calculate_salary(self):
        total = self.salary + self.bonus
        print("Salary: ", total)
employee = Manager(50000, 10000)
employee.calculate_salary()

#2.Polymorphism animal sound
class Dog:
    def speak(self):
        print("Dog barks bow bow")

class Cat:
    def speak(self):
        print("Cat sounds Meow")

class Cow:
    def speak(self):
        print("Cow sounds Amba")

def animal_sound(obj):
    obj.speak()

dog = Dog()
cat = Cat()
cow = Cow()
animal_sound(dog)
animal_sound(cat)
animal_sound(cow)

#3. Multilevel inheritance with polymorphism create vehicle
class Vehicle:
    def fuel_type(self):
        print("Vehicle uses fuel")
class Car(Vehicle):
    def fuel_type(self):
        print("Car uses petrol / diesel")
class ElectricCar(Car):
    def fuel_type(self):
        print("Electric Car uses electricity")

v = Vehicle()
c = Car()
e = ElectricCar()
v.fuel_type()
c.fuel_type()
e.fuel_type()

#4.Operator Overloading create Bank Account
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, add):
        return self.balance + add.balance

    def __gt__(self, add):
        return self.balance > add.balance

acc1 = BankAccount(5000)
acc2 = BankAccount(8000)

total_balance = acc1 + acc2
print("Total Balance:", total_balance)

if acc2 > acc1:
    print("Account 2 has more balance")
else:
    print("Account 1 has more balance")

#6.Multiple inheritance and MRO (diamond structure)\
class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        print("class B")
class C(A):
    def show(self):
        print("class C")
class D(B, C):
    pass
d = D()
d.show()
print(D.mro())


#7.Polymorphism with Exception handling Calculator handles zeroDivision error
class Calculator:
    def divide(self, a, b):
        print( a / b)
class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            print( a / b)
        except ZeroDivisionError:
            print("Cannot divide by zero")

Cl = Calculator()
safe_Cl = SafeCalculator()
Cl.divide(10, 2)
safe_Cl.divide(10, 0)

#8.Real tym Payment System
class Payment:
    def pay(self, amount):
        print("payment of", amount)
class CreditCard(Payment):
    def pay(self, amount):
        print(amount, "paid using Credit Card")
class UPI(Payment):
    def pay(self, amount):
        print( amount, "paid using UPI")
class Netbanking(Payment):
    def pay(self, amount):
        print(amount, "paid using Netbanking")

def process_payment(payment_method, amount):
    payment_method.pay(amount)

a = CreditCard()
b = UPI()
c= Netbanking()
process_payment(a, 1000)
process_payment(b, 1000)
process_payment(c, 2000)
