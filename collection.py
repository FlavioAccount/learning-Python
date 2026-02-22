# collection = single "variable" used to store multiple values
#   List    =   [] ordered and changeable. Duplicates OK
#   Set     =   {} unordered and immutable, but add/Remove OK. NO duplicates
#   Tuple   =   () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]
fruit = len(fruits)
# print(fruits)    #Use this to access all values inside the list
# print(fruits[0])     #Use this to access one value inside the list

# print(fruits[::2])   #Jumps two by two

# print(fruits[::-1])  #access the values backward

# for fruit in fruits:
#     print(fruit)
    
# print("Next code ---------------------------------------------------------------------------------------------")

# print("How to use HElp")

# # print(help(fruits))

# print("Next code ----------------------------------------------------------------------------------------------")
# #print(dir(fruits)) #dir means it is a collection
# print("apple" in fruits)#Returns a boolean with true or false case there are these elements inside

# print("Next code --------------------------------------------------------------------------------------------------")

# fruits[0] = "pineapple"

# # for fruit in fruits:
# #     print(fruits)

# # print("Next code-------------------------------------------------------------------------------------------------------")
# # #Append method

# # fruits.append("pineapple")
# # print(fruits)

# # #Remove method
# # fruits.remove("orange")

# fruits.insert(0, "rice") #insert this new string in first position
# print(fruits)
# fruits.sort() #changes the order to alphabetic order
# print(fruits)
# # fruits.clear() #Clears the list
# print(fruits)
# print(fruits.index("coconut")) #search for this string and returns the position. Won´t return a valid value if it doesn't find anything

#print("Ola Adilson")

print("Exercise____________________________________________________________________________________________________________________")
"shopping cart program"
foods = []
prices = []
total = 0
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower == "q": #This will make the input lowercase
        break
    else:
        price = input(f"Enter the price of a {food}: $")
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food, end= " ")
