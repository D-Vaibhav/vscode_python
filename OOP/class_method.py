'''
    depending upon the dependence of the methods we can define our methods
    if self/instance is needed in logic => def regularMethod(self):
    if cls/class is needed in logic => def classMethod(cls):
    if logic is independent of both cls/self => def staticMethod():
'''

# uses cls and will pass class as first parameter
# who can use: class as well it's instances
# cls = class_name
# when to use: when we want multiple ways to create class object


class Employee:
    annual_raise = 1.07

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def setAnnualRaise(cls, revised_annual_raise):
        cls.annual_raise = revised_annual_raise

    # creating additional ways to create object
    @classmethod
    def objectFromString(cls, instance_string):
        # will create an object like this
        name, age, salary = instance_string.split("-")
        return cls(name, age, salary)


emp = Employee("vaibhav dwivedi", 23, 7_00_000_000)

Employee.setAnnualRaise(1.11)
print(Employee.annual_raise, emp.annual_raise)

# creating object instance via class method, alternative __init__ and constructor
emp_1 = Employee.objectFromString("deadpool-101-500000")
print(emp_1.name, emp_1.salary)
