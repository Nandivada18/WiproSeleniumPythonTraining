#variables - uses to store the data
#instance variables - global variables at class level
#local variables - inside the method only

#instance variables example
class Student:
    #class variables
    school ="St Joseph Convent"
    def __init__(self,name,marks):
        self.name = name #instance variables or global variables
        self.marks = marks

    def show(self):
        schoolcity = "Banglore" #local variables - scope inside the method
        print(self.name,self.marks)
        print(schoolcity)
        print(self.school)

s1 = Student("Harsha",85)
s2 = Student("Amit", 90)

s1.show()
s2.show()



