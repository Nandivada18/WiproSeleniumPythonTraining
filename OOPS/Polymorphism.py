#poly morphism means taking forms
#same method / function name will behave differently depending on the object type

#class implementation
#object type
print(len("python"))
print(len([1,2,3]))#list
print(len({1,2,3}))

#input arguments no of data types

class calculator:
    def add(self, a,b=0,c=0):
        return a + b+ c

c = calculator()
print(c.add(5))
print(c.add(5,10.5))
print(c.add(5,10,15))

#runtime polymosrphism
#achieved method overriding - child class method will override the parent class method

class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")

a = Dog()
a.sound()