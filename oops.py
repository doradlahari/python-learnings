# oops : Object Oriented Programings

# class - Detailed or Blueprint of an object..
# object  - Its a varibales which has permission ot access anything inside the class..(Instance of a class..)

# Syntax :

"""
class Classname:
    statements 
"""

# Its recommended to start the class name with upper case characters..

# class Employee:
#     name = "ramesh"
#     email = "ramesh@gmail.com"
#     print("HI1")
#     print(name,email)

# def employee():
#     name = "ramesh"
#     email = "ramesh@gmail.com"
#     print("Hi2")
#     print(name,email)

# employee()


# object - Instance of a class.

# class Employee:
#     name = "ramesh" # attributes
#     email = "ramesh@gmail.com"
#     print("HI1")
#     print(name,email)


# print(name) # we cannot access it as varibales inside the class can be accessed only with objeect or classname.
# obj = Employee()

# print(obj.name)
# print(Employee.name)

# print(obj.name)



# class Employee:
#     name = "ramesh" # attributes
#     email = "ramesh@gmail.com"
#     print("HI1")
#     def info(self): # Every method inside the class should take self as default argument..
#         # return(f"Hi {Employee.name}, Your email id is {Employee.email}")
#         return(f"Hi {self.name}, Your email id is {self.email}")

# obj1 = Employee()

# print(Employee.info())

# print(obj1.info())

# self -- same as this in java.


class Employee:
    name = "ramesh" # class attributes
    email = "ramesh@gmail.com"
    print("HI1")
    def __init__(self,name,email): # instance attributes
        self.name = name
        self.email = email

    def info(self): # Every method inside the class should take self as default argument..
        # return(f"Hi {Employee.name}, Your email id is {Employee.email}")
        return(f"Hi {self.name}, Your email id is {self.email}")

# constructor :

# __init__ -- Default method in python which is used to pass arguments to the class call..

# obj1 = Employee() # Error

emp1 = Employee("suresh","suresh@gmail.com")

emp2 = Employee("Mahesh","mahesh@gmail.com")

print(Employee.name) # Class Attributes

print(emp1.name)

print(emp1.info())



print(Employee.name) # Class Attributes

print(emp2.name)

print(emp2.info())


# Attributes -- Varibales declared inside the class..
    # Instance Attributes
    # Class Attributes

# Methods -- Functions delcared inside the class..

    # Instance Methods
    # Class Methods
    # Static Methods