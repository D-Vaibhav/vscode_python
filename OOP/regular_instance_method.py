'''
    depending upon the dependence of the methods we can define our methods
    if self/instance is needed in logic => def regularMethod(self):
    if cls/class is needed in logic => def classMethod(cls):
    if logic is independent of both cls/self => def staticMethod():
'''

# uses self and will pass class object's instance as first parameter while calling any method
# who can use: class as well it's instances
# self = class_object_instance


class Employee:
    def __init__(self, name):
        self.name = name

    # regular method
    def displayInfo(self):
        print("employee is {}".format(self.name))


emp = Employee("vaibhav")
emp.displayInfo()
