#these are strings
print("This is the main method")
def main():
    print("Hello")
print(__name__)
if __name__=='__name__':
    first_name = "bro"
    food = "pizza"
    email = "bro@fake.com"

    print(f"Hello {first_name}")#f means format
    print(f"You like {food}")
    print(f"Your e-mail is {email}")

    #Integers
    age = 25
    quantity = 3 
    print(f"you are {age} old")
    print(f"You are buying {quantity} cakes")

    #float
    price = 10.99
    distance = 5.54

    print(f"The price is ${price}")
    print(f"You ran {distance} Km")

    #Boolean
    is_student = False

    if is_student:
        print("you are a student")
    else:
        print("you are not a student")

    #Type casting = This process of converting a variable from one data type to another 
    # str(), int(), float(), bool()


    print("typecasting ----------------------------------------------------------")
    gpa = 3.4

    type(first_name)
    print(type(first_name))     #return which type of variable it is

    gpa = int(gpa)      #convert the data type
    print(f"The new variable is {gpa}")

    gpa += gpa
    print(f"the new gpa is {gpa}")

    print("input() data ----------------------------------------------------------")

    name = input("What is your name? ") #prompts the user to enter data
    #IMPORTANT: Returns the entered data as a STRING
    age2 = input("How old are you?")
    age2 = int(age2) #convert the data type from string to integer
    print(f"Your name is {name}")
    print(f"You are {age2} years old")
    age2 = age2 + 1  
    print(f"Next year you will be {age2}")

    age3 = int(input("How old are you"))#This solution is better
    print(f"You are {age3} years old")



