# This Python program is for Booking Travel Tickets

class Traveling:             # Class creation
    
    def __init__(self,Pickup,DropPoint,TicketsPrice,Time):
        self.Pickup = Pickup
        self.DropPoint = DropPoint
        self.TicketsPrice = TicketsPrice
        self.Time = Time

    def Greeting(self):        # Class Methods
        print("Happy Journey")

class Delhi(Traveling):        # Child Class 1 creation 
    def Greeting(self):               # Polymorphism methods - Greeting method is common for all classes 
        print("Happy Journey!!")

class Chennai(Traveling):     # Child Class 2 creation
    def Greeting(self):              # Polymorphism methods
        print("Happy Journey!!")

class Hedrabad(Traveling):   # Child Class 3 creation
    def Greeting(self):              # Polymorphism methods
        print("Happy Journey!!")

class Banglore(Traveling):   # Child Class 4 creation
    def Greeting(self):             # Polymorphism methods
        print("Happy Journey!!")

# Object creation and Value assigning 
Obj1 = Delhi("ShivajiNagar - Pune","Gurgram - Delhi","3000","11:30pm")
Obj2 = Chennai("Katraj - Pune","abc - Chennai","2800","10:20pm")
Obj3 = Hedrabad("Katraj - Pune","ijk - Hedrabad","1600","11:30pm")
Obj4 = Banglore("Swarget - Pune","xyz - Banglore","4000","9:00pm")

for i in (Obj1,Obj2,Obj3,Obj4):
    
    print(f"\nPickup : {i.Pickup},\nDropPoint : {i.DropPoint},\nTicketsPrice : {i.TicketsPrice},\nTime : {i.Time}")
    
    i.Greeting()