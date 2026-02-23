#Multiple inheritance is 2 parents and 1 child class
class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1,Parent2):
    pass

#example
class Father:
    def driving(self):
        print("Father has the skills to drive")

class Mother:
    def cooking(self):
        print("Mother has the skills to cook")

class Child(Father,Mother):
    def bothskills(self):
        print("child has the skills to study")
        print("Child has both skills of driving and cooking")

c = Child()
c.cooking()
c.driving()
c.bothskills()