# # Method overriding
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
        
# class dog(Animal):
#     def sound(self):
#         print("Dog barks...")
        
# class cat(Animal):
#     def sound(self):
#         print("Cat meows...")
        
# obj1 = dog()
# obj1.sound()

# obj2 = cat()
# obj2.sound()

# # Static method
# class Mathutlis:
#     @staticmethod
#     def add(x,y):
#         print(x+y)
        
#     @staticmethod
#     def sub(x,y):
#         print(x-y)
        
#     @staticmethod
#     def multiply(x,y):
#         print(x*y)
        
# Mathutlis.add(4,5)
# Mathutlis.sub(5,2)
# Mathutlis.multiply(4,9)

# class variable,instance variable,class method,instance method
class Circle:
    # class variable
    pi = 3.14159
    
    def __init__(self,radius):
        self.radius = radius    #instance variable
        
    def calculate_area(self):
        print(Circle.pi*self.radius*self.radius)
        
    @classmethod
    def froom_diameter(cls,diameter):
        radius = diameter/2
        return cls(radius)
    
circle1 = Circle(7)
circle2 = Circle.froom_diameter(10)

circle1.calculate_area()
circle2.calculate_area()