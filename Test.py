#LISTS
numbers = [12, 2, 36, 4]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", True]

#Indexed
#print(numbers)
#print(names)
#print(mixed)

numbers.sort()
#print(numbers)
numbers[0]   # 1
numbers[-1]  # 4

#print(numbers)
#print(numbers[-1])
numbers.append(56)
#print(numbers)
numbers.remove(4)
#print(numbers)
student = {
    "name": "Lenny Wisdom",
    "age":18 ,
    "grade": "A-",
    "School":"Mang'u"
}

#print(student)        


student = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "grade": input("Enter grade: ")
}

print(student)

name = input("Enter name: ")
age = int(input("Enter age: "))
grade = input("Enter grade: ")
school = input("Name of your School Nigga: ")

student2 = {
    "name": name,
    "age": age,
    "grade": grade,
    "school": school,
}

print(student2)

#Prac functions
