#Handle FileNotFoundError Exception when opening a file
import json
try:
    with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//employee.json", 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error file not found")
finally:
    print("all done")

#Handling invalid user input
try:
    num = int(input("Enter the number: "))
    print(num+num)
except ValueError:
    print("Enter the valid integer")
finally:
    print("Completed")

#Program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length
import random
import string
char = random.choice(string.ascii_letters)
print(char)
# random string
randomstring = ""
for i in range(5):
    randomstring += random.choice(string.ascii_letters)
print(randomstring)

# random string with fixed length
length = 4
fixedlen = ""
for i in range(length):
    fixedlen += random.choice(string.ascii_letters)
print(fixedlen)


