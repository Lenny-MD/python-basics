#Loop-means repeating an action for each item in a sequence
#For loop -it repeats an action as long as the condition is true
fruits=["apple","banana","mango"]

for fruit in fruits:
    print(fruit)

numbers=[10,20,30,40,50] 

for number in numbers:
    print(number)


name="Python"    

for letter in name:
    print(letter)

#Range
for i in range(1000):
    print(i)

for num in range(31):
    print(num)   

for number in range(7,56):
    print(number)   

#Using conditions inside a for loop   

marks=[20,70,50,45,78,34]  

for mark in marks:
    if mark >=50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

#break and continue
# Break-it means stop the loop
for number in range(1,12):
    if number ==4:
        break
    print(number)

#continue-skip that element
for num in range(5,30):
    if num==7:
        continue
    print(num)


#While-this runs the specified amount as long as the condition remains true

count=1
while count<=5:
    print(count)
    count+=1

#using while loop print all even numbers between 2-100
count=2
while count <=100:
    print(count)
    count+=2




