#python function to sum all the numbers in a list
def sum(nums):
    total = 0
    for i in nums:
        total += i
    return total
print(sum([1,2,3,4,5,6]))

#python function find maximum of three numbers
def max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(max(18,22,44))

# for list of numbers
def max(nums):
    maximum =nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
    return maximum
print(max([1,5,8]))


