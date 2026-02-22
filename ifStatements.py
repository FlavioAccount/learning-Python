#if = Do some code only if some condition is True
#Else do something else

# age = int(input("Enter your age "))

# if age >= 18:
#     print("You can take credit ")
# elif age == 17:
#     print("You can apply for a credit in advanced ")
# else:
#     print("You are not allowed to take credit ")

#How to use a string

# name = input("Type your name: ") #for input() is not necessary to define the format

# if name == "":
#     print("You did not type your name: ")
# else:
#     print(f"Hello {name}")

#How to use for a boolean

# for_sale = False

# if for_sale: #Is not necessary to compare the boolean value to something else
#     print("This item is for sale")
# else:
#     print("This item is not allowed for sale")

#Conditional Expressions = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          x if condition else Y

num = 5
a = 6
b = 7
age = 13

print("Positive" if num > 0 else "Negative")

print("EVEN" if num % 2 == 0 else "ODD") #Verifica se o numero é par ou impar

max_num = a if a > b else b #Return the max value
min_num = a if a < b else b #Return the min value

print(max_num)

#String

status = "Adult" if age >= 18 else "Child"
print(status)