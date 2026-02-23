#generators - special type of functions - return one value at a time, on demand
#yield
#memory efficient
#use full large set of data
#files, retries, batching

#normal function
def numbers():
    return[1,2,3,4]
print(numbers())

#genrator
def generator():
    print("printing 1")
    yield 1

    print("printing 2")
    yield 2

    print("printing 3")
    yield 3

    print("printing 4")
    yield 4
ret_value = generator()
print(next(ret_value))
print(next(ret_value))
print(next(ret_value))
print(next(ret_value))