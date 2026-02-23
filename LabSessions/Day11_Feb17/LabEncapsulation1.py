#1. Create a class BankAccount with private balance.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

account = BankAccount("Prasad", 10000)
account.deposit(2000)
account.withdraw(5000)

print("Current Balance:", account.get_balance())
account.set_balance(15000)
print("Updated Balance:", account.get_balance())

#2. Use getter and setter methods to update balance safely.
#same in above

#3.Prevent negative salary using property decorators.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
            print(f"Salary updated to {self.__salary}")
        else:
            print("Salary cannot be negative")

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
e = Employee("Prasad", 50000)
e.display()
e.salary = -1000
e.display()


