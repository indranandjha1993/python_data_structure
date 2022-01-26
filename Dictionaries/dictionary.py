"""
 Declaring dictionary

 In Dictionary each key is separated from its value by a colon (:), the items are separated by
 commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just
 two curly braces, like this − {}.

 Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type,
 but the keys must be of an immutable data type such as strings, numbers, or tuples.
"""

dictionary1 = {'Name': 'Indra Nand Jha', 'Age': 29, 'Skill': 'Python Developer'}
dictionary2 = {'Name': 'Joker', 'Age': 25, 'Skill': "Acting", 1: "Int key", (1, 5): "Tuple key"}

"""
 print dictionary
"""
print(dictionary1)
print(dictionary2)
print(dictionary2[(1, 5)])
print(dictionary2[1])
print(dictionary1['Name'])

"""
 Updating dictionary
"""
dictionary1['Name'] = "Indra Jha"
print(dictionary1)

"""
 Deleting dictionary
"""
del dictionary2['Age']  # delete element from dictionary
# print(dictionary2['Age'])  # it will throw an error because Age has been deleted

dictionary2.clear()  # clear all elements from diction
print(dictionary2)

del dictionary2
# print(dictionary2)  # it will throw an error because whole dictionary has been deleted


