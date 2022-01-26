"""
Declaring lists
Note: thing about a list is that items in a list need not be of the same type.
"""

list1 = ['physics', 'chemistry', 545, 878]  # with mix element types
list2 = [1, 2, 3, 4, 5, 6]  # with single element type

# update list by index
list1[2] = "mathematics"

# deleting element by list index
del list1[2]

# print whole list
print(list1)
print(list2)

# print list by index
print(list1[0])

# print element with range of data
print(list2[2:4])  # print from index 2nd to 4th
print(list2[:3])  # print from 0th (start) index to 3rd
print(list2[2:])  # print from 2nd index to end index

"""
 List operation
 
 Lists respond to the + and * operators much like strings; they mean concatenation and repetition 
 here too, except that the result is a new list, not a string.
"""

print("Length of list: %i" % len(list2))  # get length of the list
list3 = list1 + list2  # concatenate lists
print(list3)

# Multiplication operation can be only done integer with list
list4 = list1 * 3  # multiply lists
print(list4)

"""
 Find element in list
"""
print(3 in list2)

"""
 print list through for loop
"""
for x in list2:
    print(x)
