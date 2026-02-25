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
            print("Car not available")

#Inheritance
class Electric_Car(Car):
    def charge(self):
        print(f"{self.brand} is charging")

Tesla=Electric_Car("Tesla","Matt Black")
Tesla.rent()
Tesla.charge()
        
class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited.New balance is {self.balance}")

class Savings_Account(Account):
    def add_interest(self):
        interest=self.balance*0.05
        self.balance+=interest
        print(f"Interest of {interest} added,new balance is {self.balance}")

class Business_Account(Account):
    def take_loan(self,amount):
        self.balance+=amount
        print(f"Loan of {amount} received,your new balance is {self.balance}")

ACC1=Savings_Account("Legend",67000)
ACC1.deposit(3000)
ACC1.add_interest()

ACC2=Business_Account("Magel",100000)
ACC2.take_loan(400000)
        