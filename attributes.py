# # Attribute : Variables declared inside the class..
#     # Instance attribute : Those attribute which we can access only with object..
#     # Class Attribute : Those attributes which we can access with both object and class.


# class Employee:
#     address = "Hyderabad" # class attribute
#     # mobile = "1389289233"

#     def __init__(self,name,email,mobile): # (instance attributes) # __init___ is called as constructor..
#         pass
#         # print(name)
#         self.name = name
#         self.email = email
#         self.mobile = mobile
#         # print(email)
#         # return name # __init__ method will not return any output at any cost, it return only None..

    
# emp1 = Employee('ramesh','ramesh@gmail.com',839892333)


# print(emp1.name)
# print(emp1.email)
# print(emp1.address)
# # print(emp1.mobile)

# print(Employee.address)
# print(Employee.mobile)

# # print(Employee.name)
# print(emp1.mobile)

# print("------------------------------------")
# emp2 = Employee('suresh','suresh@gmail.com',93998489448)

# print(emp2.name)
# print(emp2.email)
# print(emp2.address)
# print(emp2.mobile)

# # print(emp2.mobile)
# print(Employee.mobile)


# Methods: Functions defined inside the class.
    # Instance Methods : Those methods which we can access with only object and which contains self as default.
    # Class Methods: Those methods which we can access with object and class, which contains cls as default.
    # Static Methods: Those methods which we can access with object and class, which doesnot not take any defult argument..

class Employee:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        # print(email)
        # print(f"Emial has been sent to {self.email}")

    def send_email(self):
        print(self.email)
        return f"Emial has been sent to {self.email}"
    
    def send_otp(self,mobile):
        self.mobile = mobile
        return f"Hi {self.name} OTP sent to {mobile}"
    
    def contact_info(self):
        return f"You can contact {self.name} at {self.mobile}"
    
    @classmethod
    def send_email_cls(cls,name,email):
        cls.name = name
        cls.email = email
        return f"{email} recived an email"


    def send_otp_cls(cls,mobile):
        cls.mobile = mobile
        return f"Hi {cls.name} OTP sent to {mobile}"

# emp1 = Employee("ramesh","ramesh@gmail.com")

# print(emp1.send_email())

# # print(Employee.send_email()) # This is an error..

# print(emp1.send_otp('838238209290'))

# print(emp1.contact_info())

# emp2 = Employee("suresh","suresh@gmail.com")
# print(emp2.send_email())

# print(emp2.send_otp('832989823'))


emp1 = Employee("ramesh","ramesh@gmail.com")

print(emp1.send_email_cls("mahesh","mahesh@gmail.com"))
print(Employee.send_email_cls("venkat","venkat@gmail.com"))

emp2 = Employee("suresh","suresh@gmail.com")