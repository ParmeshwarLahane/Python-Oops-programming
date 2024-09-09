# This program is iterating the 10 number 

class Myclass:      # Class creating as name Myclass

    def __iter__(self):
        self.IterVer = 1     # iterator is set point 1 number 
        return self         # iterator return itself any time

    def __next__(self):

        if self.IterVer <= 10:          # fixed the iterator stop point

            Count = self.IterVer
            self.IterVer += 1       # Incresing the iterator variable by 1
            return Count 
        
        else:
            raise StopIteration
        

obj = Myclass()
Myiter = iter(obj)

print("\nDiplay the number by using iter funtion..")
for i in Myiter:
    print(i)
