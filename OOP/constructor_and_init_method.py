# then why init: passing parameter won't provide value to the instance hence we have to initialize explicitly using __init__
class Employee:
    # constructor
    def __new__(cls, *args, **kwargs):
        print("-------- __new__ ------------")
        # cls => class
        print(cls)
        print(args)
        print(kwargs)

        # create our object and return it
        obj = super().__new__(cls)
        return obj

    def __init__(self, name="vaibhav", age="23"):
        print("------------- __init__ ------------")
        self.name = name
        self.age = age

    def displayInfo(self):
        print(f"{self.name} is of age {self.age}")


# emp_1 is class object instance
emp_1 = Employee("vaibhav", 23)
emp_1.displayInfo()
