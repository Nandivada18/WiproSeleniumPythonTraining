nums = [1,2,3,4,5,6]
even = list(filter(lambda x:x%2 == 0,nums))
print(even)

#Square
square=list(map(lambda x:x*x ,nums))
print(square)

#find their sum
total = sum(nums)
print(total)


#Salaries
salaries = [25000, 40000,32000,18000]
filtered = list(filter(lambda x:x>30000,salaries))
print(filtered)

# add hike
hike = list(map(lambda x:x+(x*(10/100)),filtered))
print(hike)

#total payout
payout = sum(hike)
print(payout)

#1.program to sort a list of tuples using lambda
data = [(1,4),(3,1),(2,2)]
sort = sorted(data,key = lambda x:x[1])
print(sort)

#2. Extract year, month, date, time
from datetime import datetime
present = datetime.now()
time = lambda x:( x.year,x.month,x.day,x.strftime("%H:%M:%S"))
print(time(present))

#3. python script to concatenate dict to create a new one
a={'a':1,'b':2}
b={'c':3,'d':4}
new=a|b
print(new)
