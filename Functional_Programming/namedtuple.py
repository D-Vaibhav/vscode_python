import collections

People = collections.namedtuple('People', ['name', 'age'])

peoples = (People("vaibhav", 23), People(name='dwivedi', age=32))
print(peoples)

# can be sliced
print(peoples[0])
print(peoples[1].name)
