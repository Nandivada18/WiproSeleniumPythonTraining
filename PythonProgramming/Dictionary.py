#dictionary items key value pairs
country = {
    "India": "Delhi",
    "canada": "Ottawa",
    "England": "London"
}
print(country)
#access the values with keys
print(country["canada"])

#add elements
country["Italy"]="rome"
print(country)

#remove elements
del country["India"]
print(country)

#clear elements
#country.clear()
#print(country)

#iterate among the dict
for coun in country:
    print(coun)

print(len(country))

#integers as a key
my_dict ={1:"one",2:"two",3:"three"}
print(my_dict)

my_dict={1:"four",2:"two",3:"three",1:"one"}
print(my_dict)

#for integers keys must be immutable

#tuples as a key
my_dict = {(1,2):"one two", 3:"three"}
my_dict = {(1,2):"one two", 3:"three", 3:"four"}
print(my_dict)

#list as a key
#my_dict={1:"hello",[1,2]:"bye"} Error cannot use list

#pop - removes the item with spec key
a = {1:'a',2:'b',3:'c'}
a.pop(3)
print(a)

#update() - adds or changes the dict
a.update({3:'d'})
print(a)

#keys()
print(a.keys())

#values()
print(a.values())

#popitem() return the last
print(a.popitem())
print(a)

#copy returns the copy of dict
b = a.copy()
print(b)

#dict inside the list
employees = [
    {"id":1,"name":"Harsha", "role":"QA"},
    {"id":2,"name":"Anil","role":"dev"},
    {"id":3,"name":"karan","role":"test"}
]
print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"], emp["role"])

employees.append({"id": 4, "name":"sita", "role":"tester"})
print(employees)

employees.pop(0)
print(employees)

#search a item in list
for emp in employees:
    if emp["name"]=="Harsha":
        print(emp)





