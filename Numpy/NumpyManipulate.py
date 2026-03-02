import numpy as np
#Changing Shape

#reshape
a = np.arange(1,7)
print("Original array", a)

#reshape the array
reshaped = a.reshape(2,3)
print(reshaped)

#flat = return 1D iterator over the array
arr = np.array([[1,2],[3,4]])
for x in arr.flat:
    print(x)

#flatten - Returns a copy of the array collapsed into one dimension
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

#ravel() = Returns a flattened array
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)

#pad() - Returns a padded array with shape increased according to pad_width
arr = np.array([1,2,3])
padded = np.pad(arr, 3,mode = 'constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards
arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)
# (3 ,4 2)

#joining Arrays
#concatenate() - joing 2 arrays

a = np.array([[1,2],[3,4]])
b= np.array([[5,6],[7,8]])

print(np.concatenate((a,b),axis = 1))

#stack - join the arrays along the new axis

a = np.array([1,2,3])
b= np.array([4,5,6])
print(np.stack((a,b),axis = 0))
print(np.stack((a,b),axis = 1))

#hstack - stacks arrays horizontally (column - wise)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.hstack((a,b)))
print(np.concatenate((a,b),axis = 1))

#vstack() - stacks arrays vertically (row-wise)
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis = 0))

#column_stack() - Stacks 1D arrays as columns into a 2D array.
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))

#row_stack() -stacks arrays row wise
print(np.vstack((a,b)))

#splitting arrays
#array must be divisible equally
arr = np.array([1,2,3,4,5,6])
result = np.split(arr,3)
print(result)

#hsplit() - Splits array horizontally (column-wise)
#works on 2D arrays
arr2 = np.array([[1,2,3,4],
                 [5,6,7,8]])
print(np.hsplit(arr2,2))

#vsplit() splits array vertically
arr2 = np.array([[1,2],
                 [3,4],
                 [5,6],
                 [7,8]])
print(np.vsplit(arr2,2))

#array.spilt()
arr = np.array([1,2,3,4,5])
print(np.array_split(arr,3))

#adding / removing elements
#resize() - Returns a new array with a specified shape

arr = np.array([1,2,3,4])
new_arr = np.resize(arr,(2,3))
print(new_arr)
#the elements will repeat in the new array
#returns a new array

#append()
arr = np.array([1,2,3])
new_arr = np.append(arr, [4,5])
print(new_arr)

#2D array
a = np.array([[1,2],[3,4]])
b= np.array([[5,6]])
np.append(a,b,axis=0)

#Inserts value before given index
arr = np.array([10,20,30])
new_arr = np.insert(arr,2,15)
print(new_arr)

#Deletes element along a specified axis
arr = np.array([10,20,30])
new_arr = np.delete(arr,2)
print(new_arr)

#unique()
arr = np.array([1,2,2,3,4,4,5])
print(np.unique(arr))

#repeating
#repeat is used to repeat each element of an array a specified number of times

arr = np.array([1,2,3])
print(np.repeat(arr,3))

#Different repeats for each element
arr2 = np.array([[1,2],
                 [3,4]])
print(np.repeat (arr2,2,axis = 0))

#title()
my_array = np.array([1,2,3])
tiled_array = np.tile(my_array,2)
print("Original Array:", my_array)
print("Tiled Array:", tiled_array)

#Rearranging the elements
#flip() - reverse the order of the elements  along the given axis
#axis = none ,reverse the entire flatten
#axis =0 reverse along the rows
#axis =1 reverse along the columns
arr = np.array([1,2,3,4,5,6])
print(np.flip(arr))
#2D array
arr1 = np.array([[1,2],
                 [3,5]])
print(np.flip(arr1))
print(np.flip(arr1,axis=0))
print(np.flip(arr1,axis=1))

#fliplr() - flip left to right(axis=1)
arr2 = np.array([[1,2,3],[4,5,6]])
print(np.fliplr(arr2))

#flipud() - flip up and down (axis=0)
print(np.flipud(arr2))

#roll() - rotates the elements along the axis
arr3 =np.array([[1,2,3],[4,5,6]])
print(np.roll(arr3,2,axis=None))

#Sorting and Searching
#sort() - Returns the sorted copy of the array
arr = np.array([1,5,6,8,4,3,9])
print(np.sort(arr))

#argsort() - Returns the indicies that would sort the array return the index position
arr =np.array([1,3,6,2,8,4,9])
print(np.sort(arr))
print(np.argsort(arr))

#lexsort() - Used for sorting for multiple columns(like sorting lastname then first name)
#sort by a first
#sort b by then
#sorting happens from right to left
a = np.array([1,0,1,0])
b=np.array([0,1,0,1])
result = np.lexsort((b,a))
print(result)
