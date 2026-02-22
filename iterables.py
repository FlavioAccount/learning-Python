# Iterables = An object/collection that can return its elements one at a time
#             Allowing it to be iterated over in a loop

my_dictionary = {"A":1, "B":2, "C":3}

# for key in my_dictionary: #If you do a loop for my_dictionary it will only access the keywords inside the loop
#     print(key)

# for value in my_dictionary.values(): #For this loop, It will access the values
#     print(value)

for key, value in my_dictionary.items():
    print(f"{key} : {value}")

