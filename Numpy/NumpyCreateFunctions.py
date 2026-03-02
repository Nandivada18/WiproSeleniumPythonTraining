'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
    Using numpy.eye()
    numpy.identity
    numpy.diag
'''

import numpy as np
#1D array
#This function creates a Numpy array filled with zeros
#By default, the data type is float64
a = np.zeros(5)
print(a)

#2D array of zeros
a_2D = np.zeros((4,3))
print(a_2D)

#using numpy.ones() Function
a = np.ones(5)
print(a)

#2D array of ones
a_2D = np.ones((4,3))
print(a_2D)

##using numpy.arrange() Function
#The numpy.arrange() function creates an array by generating a sequence of numbers based on specified start stop step
#It is similar to pythons built in range() function

#with only the stop
a = np.arange(10)
print(a)

#providing the start , stop and step values
a = np.arange(1,10,2)
print(a)

#using numpy.linespace() Function
#linespace() is used to  generate evenly spaced over a specified interval.
a = np.linspace(0,10,num=5,endpoint=True)
print(a)

#exclued the last number when endpoint false
a = np.linspace(0,10,num=5,endpoint=False)
print(a)

#using numpy.random.rand() Function
#generates an array of the specified shape with  random values between 0 and 1
#if no argument is provided, it returns a single random float value
 #1D
a = np.random.rand(5)
print(a)

#2D
a = np.random.rand(2,3)
print(a)

#3D
a = np.random.rand(2,3,4)
print(a)

#using numpy.empty() Function
#2D
#This function initializes an array without initializing its elements
#the content of the array is arbitrary
a = np.empty((2,3))
print(a)

#using numpy.full() Function
#In the following example, we are using the numpy.full() function
a = np.full((2,3),5)
print(a)

#numpy.eye() function used to create a 2D array eith ones on
# the diagonal and zeros in all other positions

identity_matrix = np.eye((4))
print(identity_matrix)

#numpy.identity - function is used generate a square identity matrix
identity_matrix = np.identity((5))
print(identity_matrix)

#numpy.diag
Matrix = ([[10,20,30],[40,50,60],[70,80,90]])
print("Original matrix" , Matrix)
Diagonal_elements = np.diag(Matrix)
print("Diagonal elements",Diagonal_elements)


