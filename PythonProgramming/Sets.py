#sets do not allow duplicate elements it contains only unique data
#unordered collection

#create a student_id set
stu_id = {112, 113, 114, 115, 115,8,9,56}
print(stu_id)

#create a string type set
letters = {'a', 'b', 'c', 'd', 'e'}
print(letters)

#create a  mixed set
mixed_set ={"Hello", 1,-7,8,9}
print(mixed_set)

#create an empty set
empty_set = set()

#add elements to set
s = {"apple", "banana", "cherry"}
s.add("mango")
print(s)

s.clear()
print(s)

ss ={1,2,3}
s=ss.copy()
print(s)

a={4,5,6}
print(a.difference(ss))#returns elemenmts prsnt in frst set

a.difference_update(ss)#removes common element in original set
print(a)

a.remove(6)
print(a)

a.discard(5)
print(a)

b={1,2,3,4,5}
b.pop()#remove any
print(b)

b.update({9,7})
print(b)

c={3,5,7,9,6,2}
print(b.union(c))

print(a.isdisjoint(c))#common elements or not

print(a.issubset(c))#all elements present in other or not

print(a.issuperset(c))#true if it contains all elements of other set

e = {1,2,3,4,5}
f = {3,4,5,7}
print(e.intersection(f))

g={1,2,3,4,5}
k={5,6,7}
g.intersection_update(k)#modify original set with common elements
print(g)