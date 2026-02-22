# List Comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [Expression for value in iterable if condition]
#            doubles = [expression for value in iterable]

#-----------------------------------------------------------------------------------------------
# This is the traditional way to create functions 
# doubles = []

# for x in range(1, 11): # Remember: In range function, the second number is exclusive
#     doubles.append(x * 2)

# print(doubles)

#------------------------------------------------------------------------------------------------

#In List Comprehension we can do the same in one line

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range (1 , 11)]

# print(doubles)
# print(triples)

#------------------------------------------------------------------------------------------------

# fruits = ["apple", "orange", "banana", "coconut"]

# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

#------------------------------------------------------------------------------------------------

# numbers = [1, -2, 3, -4, 5, -6]
# positive_nums = [num for num in numbers if num >= 0] #If you don´t want to return an expression, just put the number 
# negative_nums = [num for num in numbers if num < 0] 

# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]

# print(f"Numeros positivos: {positive_nums}")
# print(f"Numeros negativos: {negative_nums}")

# print(f"Numeros pares: {even_nums}")
# print(f"Numeros impares: {odd_nums}")

#---------------------------------------------------------------------------------------------------

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)