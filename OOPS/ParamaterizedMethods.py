#default methods - built in methods, user define methods - method name , method body

#parametrized methods
#it allows the same method to behave differently for diff inputs

#paramterized methods (multiple parameters)
class Calculator:
    def add(self,a,b):
        print(a+b)

c = Calculator()
c.add(19,30)
c.add(8,9)

#default parameters
class Test:
    def run(self,browser = "chrome"):
        print("Running on", browser)

t = Test()
t.run()
t.run("Firefox")

#*args parametrized methods
class Numbers:
    def total(self,*args):
        print(sum(args))

n = Numbers()
n.total(10,20,30)
n.total(10)
n.total(10,20)