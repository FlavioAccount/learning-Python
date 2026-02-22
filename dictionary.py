#dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(capitals) 
#print(dir(capitals)) #If you want to see different a,ttributes and methods you need to use the dir function
#print(help(capitals)) #If you wanna see the descriptions of these methods, you can use help function


#print(capitals.get("China")) #if you want to print the value inside the key "China", you need to use the get element

#----------------------------------------------------------------------------------------
# print("type the name of a capital: ", end="")
# Capital = input()
# if capitals.get(Capital):
#     print(f"The capital of {Capital} is {capitals.get(Capital)}")
# else:
#     print("We don't have this information in our database or it is not valid")
  
#----------------------------------------------------------------------------------------  

# capitals.update({"Germany": "Berlin"})
# print (capitals) # If you want to update a new capital in your dictionary, you need to use this update

#---------------------------------------------------------------------------------------------------

# capitals.pop("China") #If you want to remove this key from your dictionary use this function
# print(capitals)

#----------------------------------------------------------------------------------------------------

# capitals.popitem() #It is used case you want to remove the last key from your dictionary
# print(capitals)

#----------------------------------------------------------------------------------------------------

# capitals.clear() #It is used if you want to clear the dictionary
# print(capitals)

#----------------------------------------------------------------------------------------------------

# for key in capitals.keys(): #For every key it is gonna to return one valid key inside capitals
#     print(key)

#-----------------------------------------------------------------------------------------------------

# for value in capitals.values(): #For every value inside capitals.values it is going to print in a For loop
#     print(value)

#----------------------------------------------------------------------------------------------------

# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")

#----------------------------------------------------------------------------------------------------
