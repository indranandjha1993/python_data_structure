from array import *
import sys

# Declare a signed integer array with 2 bytes
array1 = array('B', [54, 54, 5, 45, 5, 4, 5, 4, 2])

# Insert in array
array1.insert(0, 69)

# Remove value from array
array1.remove(2)


# Update array by index
array1[0] = 7

# Search array by value
# print(array1.index(4))

# Print all array element by loop
for x in array1:
    print(x)

# print array element by index
# print(array1[6])

# get size of array
print("Size of the array is: %i" % sys.getsizeof(array1))