#number falls in given range
num = 7
for i in range(1,10):
    if i==num:
        print(i)
        break

#even numbers
for i in range(0,50,2):
    print(i)

#sum of numbers
sum=0
for i in range(1,101):
    sum+=i
print(sum)

#divisible by 5 between 1 to 100
for i in range(1,101):
    if i%5==0:
        print(i)

#50 t0 100 with step 5
print(range(50,100,5))

#square of number 1 to 10
for i in range(1,11):
    print(i*i)

#numbers between -10 to 10
for i in range(-10,11):
    print(i)