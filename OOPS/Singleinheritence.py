#single inheritance
#Parent  --> child class - properties from parent class to child class

#parent class
class Employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid =empid

    def empdetails(self):
        print(self.name,self.empid)

#child class
class Manager(Employee):

    def approve_leave(self):
        print("leave approved")

m = Manager("John", 7878)
m.empdetails() #from parent class
m.approve_leave()#from child class

