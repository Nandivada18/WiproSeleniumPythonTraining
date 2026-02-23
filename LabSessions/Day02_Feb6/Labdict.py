students = {
    10:"kiran",
    11:"sai",
    12:"mani",
    13:"sidhu"
}
print(students)

#access values of a key
print(students[12])

#acces value which is not exist
print(students.get(19))

#update
students[13]="ravi"
print(students)

#delete
del students[11]
print(students)

#pop
students.pop(10)
print(students)

# Number of key value pairs
print(len(students))

#keys only
print(students.keys())

#values only
print(students.values())

#both key value pairs
print(students.items())

