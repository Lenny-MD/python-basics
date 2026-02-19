fruits=["apple","banana","mango"]

#Accessing List Items
#indexing -0
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[-1])

#Common used list methods
# .append
fruits.append("kiwi")
print(fruits)

# .insert
fruits.insert(1,"orange")
print(fruits)

#.remove
fruits.remove("mango")
print(fruits)

#.pop
fruits.pop()
print(fruits)

#.reverse
fruits.reverse()
print(fruits)

#len
print(len(fruits))

# sort
marks=[12,4,60,7,8,45]
print(marks)
marks.sort()
print(marks)