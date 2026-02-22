#2d List is a List made of Lists

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats] #add these lists to the 2d list
# # print(groceries[0]) #Groceries index zero is my first list, not the first element of the first list
# # print(groceries[0][0]) #First index and first element

# # for collection in groceries: #It will print all lists inside groceries
# #     print(collection)

# for collection in groceries:
#     for food in collection:
#         print(food, end= " ") #It will create a space between words
#     print() #It will create a new line for each word

print ("NEXT CODE ------------------------------------------------------------------------------------------------")

#Create a num pad with numbers

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for number in row:
        print(number, end= " ")
    print()