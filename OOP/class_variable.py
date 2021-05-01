# class variable: class scope variable and methods
# when to use: when we want our class to have consistent class variables which can be exploited by their instance/class
class Employee:
    # class variables => can be used by class as well as instance
    mail_domain = "@vaibhav.com"
    annual_raise = 1.07
    count = 0

    # class callable
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        # it's more appropriate to use Employee.count (not self.count) cause we dont want ot to get changed as per instance
        Employee.count += 1

    # class callable
    def independent_fun():
        print(
            f"can't access self.instance_vars but can access Employee.mail_domain eg:{Employee.mail_domain} class variables")

    # class and instance callable
    def displayInfo(self):
        print(f"{self.name} is of age {self.age}")

    def apply_rasie_using_class_variable(self):
        self.salary = self.salary * Employee.annual_raise
        print(self.salary)

    # is more appropriate, cause it makes sense that we want change the value of as per instance
    def apply_rasie_using_instance_variable(self):
        self.salary = self.salary * self.annual_raise
        return self.salary


# emp_1 is class object instance
emp_1 = Employee("vaibhav", 23, 70_000_000)
emp_outSourced = Employee("deadpool", 23, 70_000_000)

# calling class variable and passing it's object instance which get reffered as self inside class
Employee.displayInfo(emp_1)
print(Employee.annual_raise)

print(emp_1.salary)
emp_1.apply_rasie_using_class_variable()
print(emp_1.salary)

Employee.independent_fun()

# class variables
print(Employee.__dict__, end='\n\n')

# instance variable
print(emp_1.__dict__, end='\n\n')
print(emp_1.mail_domain, end='\n\n')  # getting this from class

emp_outSourced.mail_domain = "@gmail.com"
print(emp_outSourced.__dict__, end='\n\n')
print(emp_outSourced.mail_domain)    # getting this from it's own instance

print(Employee.count)
print(emp_1.count)
