"""
 Declaring a tuple

 A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between
 tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square
 brackets.
"""

tuple1 = ('physics', 'chemistry', 6465, 'biology')
tuple2 = (1, 2, 3, 4, 5, 6)
tuple3 = "a", "b", "c", "d", 5
tuple4 = ()  # empty tuple
tuple5 = (
    4,)  # To write a tuple containing a single value you have to include a comma, even though there is only one value

"""
 print tuples
"""
print(tuple1)
print(tuple2[2])
print(tuple2[2:5])
print(tuple3[:2])
print(tuple3[2:])

"""
 Deletion from tuple
"""
# del tuple1[0]  # it will through an error, because tuple doesn't support item deletion
del tuple3

"""
 Tuple operations
"""
print("Length of tuple: %i" % len(tuple1))
tuple5 = tuple1 + tuple2
print(tuple5)
tuple6 = tuple1 * 3
print(tuple6)

"""
 print thorough for loop
"""
for x in tuple1:
    print(x)

"""
 Find element in tuple
"""
if 'history' in tuple1:
    print(True)
else:
    print(False)

