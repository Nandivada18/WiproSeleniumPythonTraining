class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    print("Class D")

d= D()
d.show()
print(D.mro())
#methods from thr left to right
#D,B,C,A

