# class Car:
#     wheels = 4
#     def drive(self):
#         print("The car is moving")

# Jeep=Car()
# print(Jeep.wheels)
# Jeep.drive()

class Car:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
        self.available=True
    def rent(self):
        if self.available:
            self.available=False
            print(f"{self.brand} {self.colour} has been rented out")
        else:
            print(f"Sorry {self.brand} {self.colour} is not available right now")
    def return_Car(self):
        self.available=True
        print(f"{self.brand} {self.colour} has been returned")

car1=Car("Mercedes","blue")
car1.rent()
car1.return_Car()

class MpesaAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} Ksh succesfully deposited, new balance is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"Insufficient Funds")
        else:
            self.balance-=amount
            print(f"{amount} Ksh Withdrawn successfully, new balance is {self.balance}")

Account1=MpesaAccount("John",5000)
Account1.deposit(2000)
Account1.withdraw(3500)

#Check balance
        
        
     