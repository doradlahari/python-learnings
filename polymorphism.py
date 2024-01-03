# # Polymorphism(Multiple Forms) : Writing the method with same name but different functionalities..
    # Method Overriding: Considering the child class method by overriding the parent class method..
    # Method Overloading: Python doesnot support the concept of method overloading.


class Father:
    def add(self,a,b):
        return a+b
    

class Child(Father):
    def add(self,a,b):
        return (a+b)-(a-b)
    
    def add(self,a,b,c,d):
        return a+b+c+d
obj1 = Child()
print(obj1.add(4,8))