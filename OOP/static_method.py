'''
    depending upon the dependence of the methods we can define our methods
    if self/instance is needed in logic => def regularMethod(self):
    if cls/class is needed in logic => def classMethod(cls):
    if logic is independent of both cls/self => def staticMethod():
'''

import datetime

todayDate = datetime.date(2021, 5, 1)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # methods which are niether specific to class or it's object
    @staticmethod
    def isHoliday(inputDate):
        # terniary operator
        return True if inputDate.weekday() in [5, 6] else False


emp = Employee("vaibhav dwivedi", 23, 7_00_000_000)

print("It's Holiday") if Employee.isHoliday(
    todayDate) else print("It's work-day")
print("It's Holiday") if emp.isHoliday(todayDate) else print("It's work-day")
