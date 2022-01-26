from numpy import array as matrix, append, insert, delete

"""
 Declaring Matrix

 Matrix is a special case of two-dimensional array where each data element is of strictly same size. So every matrix
 is also a two dimensional array but not vice versa.
"""

matrix = matrix([
    ['Monday', 18, 20, 22, 17],
    ['Tuesday', 11, 18, 21, 18],
    ['Wednesday', 15, 21, 20, 19],
    ['Thursday', 11, 20, 22, 21],
    ['Friday', 18, 17, 23, 22],
    ['Saturday', 12, 22, 20, 18],
    ['Sunday', 13, 15, 19, 16]
])

"""
 Print matrix elements
"""
print(matrix)
print(matrix[0])
print(matrix[0][0])

"""
 Adding row to matrix
"""
matrix1 = append(matrix, [['New day', 13, 15, 19, 16]], 0)
print(matrix1)

"""
 Adding column to matrix
"""
matrix2 = insert(matrix, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)
print(matrix2)

"""
 Deleting row of matrix
"""
matrix3 = delete(matrix1, [7], 0)
print(matrix3)

"""
 Deleting column of matrix
"""
matrix4 = delete(matrix, [1], 1)
print(matrix4)

"""
 Updating row of matrix
"""
matrix1[7] = ['New Day', 54, 545, 454, 54]
print(matrix1)
