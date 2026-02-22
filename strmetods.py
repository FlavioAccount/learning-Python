# name = input("Enter your full name: ")
# name = name.capitalize() #capitalize the first letter

# result = len(name) #return the length of the string
# result1 = name.find("a") #Find the position of the letter starting from 0. Only find the first ocurrency
# result2 = name.rfind("a") #Find the last occurrancy of the letter

# print(name)

# name = name.upper() #all characters are uppercase
# print(f"All characteres in uppercase {name}")

# name = name.lower() #all characters are uppercase
# print(f"All characteres in lowercase {name}")

# result3 = name.isdigit() #Return true or false if the string contains only digits
# print(f"Does it contain only digits? {result3}")

# result4 = name.isalpha() #return true or false if the string contains only alphabetic characteres. OBS: space is not considered alphabetic and it will return false
# print(f"Does it contain only alphabetic? {result4}")

phone_number = input("Enter your phone number: ")
phone_number1 = phone_number.count("5") #Count the numbers of specified characteres 

print(f"There are {phone_number1} characteres")

phone_number = phone_number.replace("-", "") #Replace the charactere to another one

print(f"The new format is: {phone_number}")

# *********** ATTENTION ***************
# Use the following command to check the available functions for a string

print(help(str))