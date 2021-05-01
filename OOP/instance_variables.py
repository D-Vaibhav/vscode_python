# instance variable: self
# what is self: self => class object instance
# when to use: when we want our class object instance to access variable outside of class
class Employee:
    # passing parameter won't provide value to the instance we have to initialize explicitly using __init__
    # hence it's not a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print("{} is of age {}".format(self.name, self.age))
        print(f"{self.name} is of age {self.age}")


# emp_1 is class object instance
emp_1 = Employee("vaibhav", 23)

# instance calling method will automatically pass itself(instance) to the method hence we have to use self
emp_1.displayInfo()

print(emp_1.name, emp_1.age)
