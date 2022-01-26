import collections

"""
 Creating a ChainMap / Map

 Python Maps also called ChainMap is a type of data structure to manage multiple dictionaries together as one unit. 
 The combined dictionary contains the key and value pairs in a specific sequence eliminating any duplicate keys. The 
 best use of ChainMap is to search through multiple dictionaries at a time and get the proper key-value pair mapping. 

"""

dictionary1 = {'day1': 'Mon', 'day2': 'Tue'}
dictionary2 = {'day3': 'Wed', 'day1': 'Thu'}

map1 = collections.ChainMap(dictionary1, dictionary2)

"""
 print maps
"""
print(map1)
print(map1.maps)

print('Key = {}'.format(list(map1.keys())))
print('Value = {}'.format(list(map1.values())))

# print all elements with for loop
for key, value in map1.items():
    print('{} = {}'.format(key, value))

# search element in map
print('day1 in map: {}'.format(('day1' in map1)))
print('day in map: {}'.format(('day' in map1)))

"""
 updating map
"""

dictionary2['day1'] = 'Fri'
print(map1)
