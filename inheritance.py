# # Inheritance : A class getting or acquiring the properties from some other class..
#     # Single Inheritance
#     # Multiple Inheritance
#     # Multilevel Inheritance
#     # Hybrid Inheritance
#     # Hierirical Inheritance

# # Single Inheritance: A clas getting the properties from single parent class.

# # class Parent:
# #     name = "ramesh"
# #     acres = 12

# #     def property_info(self):
# #         return f"Hi {self.name} you have {self.acres} acres of land"
    

# # class Child(Parent):
# #     name = "suresh"
# #     mobile = "838929832938"

# #     def property_info(self):
# #         return f"{self.acres} acres of land is registered with {self.name}"

# # obj1 = Child()

# # print(obj1.name)
# # print(obj1.acres)
# # print(obj1.mobile)
# # print(obj1.property_info())


# # Multiple Inheritance:
#     # A class getting the properties from multiple parent classes..


# class Father:
#     name = "ramesh"
#     acres = 12

#     def property_info(self):
#         return f"Hi {self.name} you have {self.acres} acres of land"
    
# class Mother:
#     name = "radha"
#     acres = 5

#     def property_info(self):
#         return f"{self.acres} acres of agricultural land is under your name {self.name}"

# class Child(Mother,Father):
#     name = "suresh"
#     mobile = "838929832938"

#     def property_info(self):
#         return f"{self.acres} acres of land is registered with {self.name}"

# # obj1 = Child()

# # print(obj1.name)

# # print(obj1.acres)

# # print(obj1.property_info())


# # MRO -- Method Resolution Order -- Order that python follow while inheriting the classes..


# # Multilevel Inheritance : 
#     # A class getting the proeperties from Parent class, But that Parent again has a Parent(GrandParent) class..
#     # Now the child can go and get the proeprties from both Parent and Grand Parent..

class GrandFather:
    name = "ramesh"
    acres = 12

    def property_info(self):
        return f"Hi {self.name} you have {self.acres} acres of land"
    
class Father(GrandFather):
    # name = "Mahesh"
    acres = 5

    def property_info(self):
        return f"{self.acres} acres of agricultural land is under your name {self.name}"

class Child(Father):
    # name = "suresh"
    mobile = "838929832938"

    def property_info(self):
        return f"{self.acres} acres of land is registered with {self.name}"

obj1 = Child()

print(obj1.name)


# # Hybrid Inheritance : Its a combination of multitypes of inheritances..
    

# # class GrandFather:
# #     name = "ramesh"
# #     acres = 12

# #     def property_info(self):
# #         return f"Hi {self.name} you have {self.acres} acres of land"
    
# # class Father(GrandFather):
# #     # name = "Mahesh"
# #     acres = 5

# #     def property_info(self):
# #         return f"{self.acres} acres of agricultural land is under your name {self.name}"


# # class Mother:
# #     name = "Radha"
# #     acres = 7

# #     def property_info(self):
# #         return f"{self.acres} acres of agricultural land is under your name {self.name}"

# # class Child(Mother,Father):
# #     # name = "suresh"
# #     mobile = "838929832938"

# #     def property_info(self):
# #         return f"{self.acres} acres of land is registered with {self.name}"

# # obj1 = Child()

# # print(obj1.name)


# # Hiererical Inheritance : Multiple Child classes are getting the properties from single parent class..
    

# class Father:
#     name = "mahesh"
#     acres = 12
#     def property_info(self):
#         return f"{self.acres} acres of land is registered with {self.name}"


# class Son1(Father):
#     name = "venkat"
#     # acres = 8

#     def property_info(self):
#         return f"{self.name} you have {self.acres} of land with you."

# obj1 = Son1()
# print(obj1.name)

# print(obj1.property_info())

# class Son2(Father):
#     name = "rajesh"
#     # acres = 7

#     def property_info(self):
#         return f"you have {self.acres} of land with you."
    
# obj2 = Son2()

# print(obj2.name)

# print(obj2.property_info())
