"""
 Declaring 2D Array

 Two-dimensional array is an array within an array. It is an array of arrays.
 In this type of array the position of a data element is referred by two indices instead of one.
 So it represents a table with rows a columns of data.
"""

array1 = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
array2 = [[11, 12, 5, 2], ["djhbhjb", 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

"""
 print 2d array
"""
print(array1)
print(array1[0])
print(array1[0][2])
print(array2)

"""
 Insert element by index
"""
array1.insert(1, [0, 1, 2, 3, 4, 5])
print(array1)

"""
 Update element by index
"""
array1[1][0] = 1
print(array1)
array1[0] = ["a", "b"]
print(array1)

"""
 Deleting element by index
"""
del array1[0]
print(array1)

for x in array1:
    print(x)
    for y in x:
        print(y)
