#Class is a blueprint or a template
#Which describes the state/ behaviour of its object
# data is put in variables
# behaviour is put in functions
class Student:
    #data or the properties
    studentname= "Ravi"
    studentID =677887
    #self is used to access the attributes of the class we have defined
    #it is automatically loaded
    #self represents the instance of the calss

    #create a function to access the data
    def displaystudentdetails(self):
        print(self.studentname)
        print(self.studentID)

#create the object  of the class
a = Student()
a.displaystudentdetails()

# class for a employee
class Employee:
    def data(self,emp_id,emp_name,emp_dept):
        print("emp_id: ", self.emp_id)
        self.emp_name = "Kiran"
        self.emp_dept = "sales"

