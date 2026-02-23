#Exceptions - runtime errors which will disrupt thr normal program flow
#benefits
#helps in debugging
#prevents program crashing
#handling errors and exceptions in the code more effectively

#try except
#try - code to be executed
#except - exceptions details catching
#finally - mandated code
#custom exceptions

try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number:  "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("please enter valid number")

#generic exception
try:
    a = 5/0
except Exception as e:
    print(e)
#runs only if no exception occurs
else:
    print("Division successful")
#mandatory code
finally:
    print("close the browser")

#custom exceptions - creating a own exception
age = int(input("Enter the age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")