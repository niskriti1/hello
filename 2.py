# Abstraction

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class rectangle(shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width*self.height
    
rect =rectangle(10,5)
print(rect.area())


# Method overloading
from multipledispatch import dispatch

@dispatch(int,int)
def product(a,b):
    print(a*b)
 
@dispatch(int,int,int)   
def product(a,b,c):
    print(a*b*c)
    
@dispatch(int,int,int,int)
def product(a,b,c,d):
    print(a*b*c*d)
    
product(2,3)
product(2,5,3)
product(2,3,4,5)

# Exception handling
def divide(a,b):
        try:
            result = a/b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            print("Division successful")
            return result
        finally:
            print("Execution completed.")
            
print(divide(10,3))
print(divide(10,0))
            