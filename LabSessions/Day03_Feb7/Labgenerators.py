#Numbers from 1 to N
def even_numbers(n):
    for i in range(1,n+1):
        yield i

for num in even_numbers(5):
    print(num)

#even numbers only
def even(n):
    for i in range(2, n+1,2):
        yield i

for num in even(10):
    print(num)

#Write a generator to read a file line by line.
import csv
def linebyline(n):
    with open(n,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row

for row in linebyline("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//data.csv"):
    print(row)

 #Create a generator for Fibonacci series.
def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)

#Write a generator that simulates retry attempts (max 3 tries).
def retry_attempts(max_tries=3):
    for attempt in range(1, max_tries + 1):
        yield attempt
for attempt in retry_attempts():
    print(f"Attempt {attempt}")
    num=input("Enter password: ")
    if num == "123":
        print("Login")
else:
    print("All retries failed.")
