"""
 Declaring set

 Mathematically a set is a collection of items not in any particular order.
 A Python set is similar to this mathematical definition with below additional conditions.

 The elements in the set cannot be duplicates.

 The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.

 There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

 A set is created by using the set() function or placing all the elements within a pair of curly braces.
"""

days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"])  # declaring with set function
months = {"January", "February", "March", "April", "May", "June", "July", "august", "September", "October", "November",
          "December"}  # declaring with curly braces
date = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}

"""
 print sets
 
 We cannot access individual values in a set. We can only access all the elements together as shown above.
 But we can also get a list of individual elements by looping through the set.
"""
print(days)
print(months)
print(date)

for x in months:
    print(x)

"""
 Adding element to set
"""
date.add(31)
print(date)

"""
 Removing element from set
"""
date.discard(31)
print(date)

"""
 Set operations
"""
date1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}

union_set = date | date1  # union of sets
print(union_set)

intersection_sets = date & date1  # intersection of sets
print(intersection_sets)

difference_sets = date-date1  # difference of sets
print(difference_sets)

# comparing sets
compare_set = date > date1
compare_set1 = date < date1
compare_set2 = date == date1
compare_set3 = date >= date1
compare_set4 = date <= date1
print("date is greater then date1:", compare_set)
print("date is less then date1:", compare_set1)
print("date is equal to date1:", compare_set2)
print("date is greater then or equal to date1:", compare_set3)
print("date is less then or equal to date1:", compare_set4)

