# Oop's Assignment: Question - 1
# Write a program which contains one class named as Demo.
# Demo class contins two instance versiables as no1, no2.
# That class contains one class variables as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance variables.
# Initialise instance variable in init method by accepting the values from user.

class Demo:   # Class creation 
    Value = 0            # Class veriable
    def __init__(self,no1,no2):
        
        # Instance variables Initialzation 
        self.no1 = no1           
        self.no2 = no2
        
    def Fun(self):        # Printing value no1 and no2 in Fun function 
        print(f"\nno1 value is : {self.no1}")
        print(f"no2 value is : {self.no2}")
        
    def Gun(self):        # Printing value no1 and no2 in Gun function 
        print(f"\nno1 value is : {self.no1}")
        print(f"no2 value is : {self.no2}")

# Accepting user input for the Instance variable
no1 = int(input("Enter number1 :" ))
no2 = int(input("Enter number2 :" ))

obj1 = Demo(no1, no2)

# Instance method calling
obj1.Fun()
obj1.Gun()