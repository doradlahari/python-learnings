# datahiding or encapsulation:
    # Providing the restrictions in accessing the attributes and methods outside the class..
    # Public Attributes : Those attributes which we can access throught out the program.
    # Public Methods : Those methods which we can access throught out the program.
    # Private Attributes : Those attributes which we can access Only inside the classes not outside.
    # Private Methods: Those methods which we can access Only inside the classes not outside.


class Sample:
    name = "mahesh" # public attributes
    email = "mahesh@gmail.com"
    __mobile = "9938283293" # private attribute

    def info(self): # public method
        return f"Hi {self.name} your email is {self.email} and mobile is {self.__mobile}"
    
    def __contact_info(self): # private method
        return f"Hi {self.name} your email is {self.email} and mobile is {self.__mobile}"

    def check(self):
        return self.__contact_info()
    
obj1 = Sample()


print(obj1.info())
print(obj1.name)

print(obj1.email)

# print(obj1.__mobile)

# print(obj1.__contact_info())

# print(obj1.check())

# print(obj1._Sample__contact_info())

# print(obj1._Sample__mobile)