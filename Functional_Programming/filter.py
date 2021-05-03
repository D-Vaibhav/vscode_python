peoples = [{"name": "vaibhav", "age": 23}]
peoples.append({"name": "deadpool", "age": 32})

twenties = filter(lambda people: people.age < 30, peoples)
print(twenties)

# twenties_list = tuple(filter(lambda people: people.age < 30, peoples))

# Errors
# twentiesList = list(twenties)
# twentiesTuple = tuple(twenties)
