# Oop's Assignment: Question - 3
# Write a program which contains one class named as Arithmetic.
# Arithmetic class contins Three instance versiables as Value1 Value2.
# Inside init method initialise all instance variable to 0
# There are five instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), and Division.
# Accept method will accept value of value1 and value2 from user.
# Addition() method will perform addition of value1 and value2 and return result
# Subtraction() method will perform Subtraction of value1 and value2 and return result
# Multiplication() method will perform Multiplication of value1 and value2 and return result
# Division() method will perform Division of value1 and value2 and return result
# After designing the above class call all instance methods by creating multiple objects

class Arithmetic: # class creating 
    def __init__(self,Value1,Value2):
        self.Value1 = Value1
        self.Value2 = Value1
        
    def Accept(self):      # Accepting two number from user
        self.Value1 = int(input("Enter Value1 : "))
        self.Value2 = int(input("Enter Value2 : "))
                
    def Addition(self):
        Addition = self.Value1 + self.Value2
        return Addition
        
    def Subtraction(self):
        Subtraction = self.Value1-self.Value2
        return Subtraction
        
    def Multiplication(self):
        Multiplication = self.Value1*self.Value2
        return Multiplication
        
    def Division(self):
        Division = self.Value1/self.Value2
        return Division

# Object creating 
Obj1 = Arithmetic(0,0)
Obj2 = Arithmetic(0,0)

# Method calling and printing 
Obj.Accept()

print("\nFirst calculation..")
print("Addition = ",Obj.Addition())
print("Subtraction = ",Obj.Subtraction())
print("Multiplication = ",Obj.Multiplication())
print("Division = ",Obj.Division())

print("\nSecond calculation..")
print("Addition = ",Obj.Addition())
print("Subtraction = ",Obj.Subtraction())
print("Multiplication = ",Obj.Multiplication())
print("Division = ",Obj.Division())

        