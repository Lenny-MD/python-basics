#Block of code meant to do a specific task.....makes the code reusable.

def greet():
    print("Hello world")

greet()

def greetings(name):
    print ("Hello "+name)

greetings("Lenny")
greetings("Mollen")
greetings("Ben")

def add_numbers(a,b):
    print(a+b)

add_numbers(12,76)

def details(name,age):
    print(f"Hello my name's {name} and I am {age} years old.")

details("Bonjee",18)

#Functionality=A FUNCTION

#With return values
 
def calculate_total(price,tax):
    return price+tax
total_amount=calculate_total(543,23)
print(total_amount)
    
def register_user(username,Email):
    print (f"Your account username is {username} and your Email is {Email}")
register_user("Muraya","MKava@gmail.com")

def is_Adult(age):
    if age >=18:
        return True
    else:
        return False
Adult=is_Adult(40)
print(Adult)

#With default parameters

def Hallo(name="Amadeus Mozart"):
    print("Hello "+name)
Hallo()
Hallo("Wolfgang")