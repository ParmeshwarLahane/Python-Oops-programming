# Oop's Assignment: Question - 2
# Write a program which contains one class named as Circle.
# Circle class contins Three instance versiables as Radius,Area and Circumference.
# That class contains one class variables as PI which is initalise to 3.14.
# Inside init method initialise all instance variable to 0.0
# There are three instance methods inside class as Accept(), CalculateArea(), and CalculateCircumference() method will calculateCircumference of circle and store in into instance varialbe Circumference.
# and Display() method will display value of all the instance variable as Redius, Area, Circumference.
# After designing the above class call all instance methods by creating multiple objects

import math

class Circle:
    
    PI = 3.14
    
    def __init(self,Radius,Area,Circumference):
        self.Radius = Radius
        self.Area = Area
        self.Circumference = Circumference

    def Accept(self):      # Accepting Redius from user
        self.Radius = int(input("\nEnter Radius : "))
        
    def CalculateArea(self):    # Calculating Area of the circlse
        self.Area = Circle.PI*(self.Radius**2)
        
    def CalculateCircumference(self):   # Calculating Circumference of circlse
        self.Circumference = 2*Circle.PI*self.Radius

    def Display(self):       # Printing the Radius, Area and Circumference
        print(f"Radius : {self.Radius}\nArea : {self.Area}\nCircumference : {self.Circumference}")
    
# Objects creating    
Circle1 = Circle()
Circle2 = Circle()

# Methods calling
print("\nFirst Circle..")
Circle1.Accept()
Circle1.CalculateArea()
Circle1.CalculateCircumference()
Circle1.Display()

print("\nSecond Circle..")
Circle2.Accept()
Circle2.CalculateArea()
Circle2.CalculateCircumference()
Circle2.Display()