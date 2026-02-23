#syntax lambda arguments: expression
#lambda functions - anonymous (nameless) functions, one line, simple operations
#function - function name, arguments, return type,m code
#it can have any number of arguments
#must have only one expression
#the expression is automatically return the value
# normal function for add two numbers
def add(a,b):
    return a+b

print(add(5,3))

#lambda function
# add
add = lambda a,b:a+b
print(add(5,3))

#square of a number
square = lambda x:x*x
print(square(5))

#Even or odd
even=lambda a: "even" if a%2==0 else "odd"
print(even(5))

#find the max of 2 numbers
max = lambda a,b : a if a>b else b
print(max(10,30))

#filter - select data - filtering the data
#map - transform the data
#reduce - aggregate the data

#filter
numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x:x%2==0, numbers))
print(evens)

#filter the failed test cases
status = ['Pass', 'Fail', 'Pass', 'Fail']
failed = list(filter(lambda s:s=='Fail', status))
print(failed)

#positive numbers
nums = [-5,10,-3,7,0,2]
positive= list(filter(lambda n:n>0, nums))
print(positive)

#non-empty strings
data = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x!="", data))
print(non_empty)

#reduce - aggregate - combining many values to a one single result
from functools import reduce
nums = [10,20,30,40]
#adding
print(reduce(lambda x,y:x+y,nums))

#multiply
print(reduce(lambda x,y:x*y,nums))

#maximum value
print(reduce(lambda x, y: x if x > y else y, nums))

#minimum value
print(reduce(lambda x, y: x if x < y else y, nums))

#Map - transform the data - the function is applied to every element
nums = [10,20,30,40]
squares = list(map(lambda x:x*x,nums))
print(squares)

#Sorting in lambda
data = [(1,3),(4,1),(2,2)]
sorteddata = sorted(data, key = lambda x:x[0])
print(sorteddata)

#sorting the dict data
marks = {"A": 75, "B": 90, "C": 60}
sorted_marks  = dict(sorted(marks.items(), key = lambda x:x[1]))
print(sorted_marks)