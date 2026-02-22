# Membership Operators = Used to test whether a value or variable is found in a sequence
#                        (sstring, list, tuple, set or dictionary)
#                        1. In
#                        2. Not In
#----------------------------------------------------------------------------------------------------
# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# #If it uses a not in, it will need to replace the arguments
# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")
#----------------------------------------------------------------------------------------------------

# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

# #Replacing the arguments:
# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

#------------------------------------------------------------------------------------------------------

# grades = {"Sandy": "A",
#           "Squidward": "B",
#           "Spongebob" : "C",
#           "Patrick" : "D"}

# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}") #Grades[student] access the dictionary. This is a good choice
# else:
#     print(f"{student} was not found")

#--------------------------------------------------------------------------------------------------------

#Check if an e-mail is valid

# email = "brocode@gmail.com"

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")
from inheritance import Dog

def main():

    dog = Dog("Scooby")
    dog.speak()

if __name__ =="__main__":
    main()