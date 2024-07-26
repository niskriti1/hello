class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return(f"Hello,my name is {self.name} and I am {self.age} years old.")
    
person1=Person("Niskriti",19)
print(person1.greet())

# Multiple inheritance

class Car:
    def fourwheeler(self):
        print("Car is a four wheeler.")
        
class Bus:
    def sixwheeler(self):
        print("Bus is a six wheeler.")
        
class Truck:
    def eightwheeler(self):
        print("Truck is a eight wheeler.")
        
class Vehicle(Car,Bus,Truck):
    def allspecies(self):
        print("All are vehicle.")
        
gadi = Vehicle()
gadi.allspecies()
gadi.fourwheeler()
gadi.sixwheeler()
gadi.eightwheeler()

# Hierarchical Inheritance

class Bird:
    def fly(self):
        print("All birds fly.")
        
class Eagle(Bird):
    def eat(self):
        print("Eagle eat meat.")

class Parrot(Bird):
    def talk(self):
        print("Parrot can talk.")
          
class Squirrel(Bird):
    def hop(self):
        print("Squirrels hop.")
        
obj=Eagle()
obj.eat()
obj.fly()

obj1=Parrot()
obj1.talk()
obj1.fly()

obj2=Squirrel()
obj2.hop()
obj2.fly()