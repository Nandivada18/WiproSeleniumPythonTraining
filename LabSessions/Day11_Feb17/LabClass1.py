#1. Create a Car class with attributes brand, model, price.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)
a = Car("Hyundai", "Creta", 30000)
a.display()

#2. Create a Student class with method get_grade() based on marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.get_grade())
s = Student("Prasad", 82)
s.display()

#3. Create a BankAccount class with deposit() and withdraw() methods.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)
a = BankAccount("Prasad", 10000)
a.deposit(2000)
a.withdraw(5000)
a.display()

#4. Write a class Employee that initializes name, id, salary using __init__.
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.id = emp_id
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.id)
        print("Salary:", self.salary)
e = Employee("Prasad", 21271, 30000)
e.display()

#5.Create a class that counts how many objects are created.
class Counts:
    count = 0
    def __init__(self):
        Counts.count += 1
    def display(self):
        print("Total objects created:", Counts.count)
a = Counts()
b = Counts()
a.display()

#6.Create a class Company with a class variable company_name.
class Company:
    company_name = "Wipro"
    def __init__(self, emp_name):
        self.emp_name = emp_name
    def display(self):
        print("Employee Name:", self.emp_name)
        print("Company Name:", Company.company_name)
e1 = Company("Prasad")
e2 = Company("Rahul")
e1.display()
e2.display()

#7. Implement a static method to validate email format.
import re

class User:
    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return "Valid Email"
        else:
            return "Invalid Email"
print(User.validate_email("prasad@gmail.com"))
print(User.validate_email("Joe@email"))



