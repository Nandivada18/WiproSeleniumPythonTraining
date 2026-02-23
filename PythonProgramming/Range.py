#range does not create a list, it creates a object (memory efficiency)
a = range(5)
print(a[1])

a = range(2,5)
for i in a:
    print(i)

a = range(2,5,3)
for i in a:
    print(i)

a = range(15,2,-1)
for i in a:
    print(i)

for attempt in range(3):
    pin = input("Enter the pin: ")
    if pin == "1234":
        print("Access granted")
        break
    else:
        print("Try Again")

prices = [100,200,300,400]
for i in range(len(prices)):
    if i % 2==0:
        print("Discount applied on item{1}")
        print(i)

import time
for second in range(10):
    print("checking the status at {second} sec")
    time.sleep(1)

