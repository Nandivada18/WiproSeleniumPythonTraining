#1
print(list(enumerate(['a','b','c'])))

#2
for i,v in enumerate([10,20,30]):
    print(i,v)

#3 print index,value
colors = ['red','green','blue']
for i,v in enumerate(colors,start=1):
    print(i,v)

#4
print(list(enumerate("PYTHON",start=1)))

#5 find index of value 50
nums=[10,20,30,40,50,60]
for i,v in enumerate(nums):
    if v==50:
        print(i)

#6
for i,n in enumerate(range(10,60,10)):
    print(i,n)

#7 convert
data = ['red','green','blue']
for i,v in enumerate(data):
    print(i,v)

#8
items = ['a','b','c']
for i in enumerate(items):
    print(i)

#9
print(enumerate([],start=5))

#10
for i,v in enumerate([100,200,300],start=-1):
    print(i,v)

#11
#i,v =enumerate(['x','y','z'])

#12 differences
#enumerate(data) here index starts from 0 by default
#enumerate(data,start=1) here index start from 1

