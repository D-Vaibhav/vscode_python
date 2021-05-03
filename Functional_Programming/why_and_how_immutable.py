'''
    WHY: mutable objects are very much prone to typo and modifications
'''

import collections

list_of_dict = [{"name": "vaibhav dwivedi", "age": 23, "single": True}, {
    "name": "deadpool", "age": 32, "single": False}]

print(list_of_dict)

# problem 1 : any new dict can get added to this list and let to adulteration of data(no control over consistency)
list_of_dict.append({"name": "Ram", "age": 23, "isMarried": True})
print(list_of_dict)

# problem 2 : typo
list_of_dict.append({"name": "Sita", "ige": 23, "single": True})
print(list_of_dict)

'''
    HOW: use collection module
'''
# defining subclass: People
People = collections.namedtuple('People', ['name', 'age', 'single'])

people1 = People("vaibhav dwivedi", 23, True)
print(people1)
