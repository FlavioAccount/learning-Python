# Function = A block of reusable code
#            place () after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}, you are {age} years old")
#     print()

# happy_birthday("Bro", 45) #You can send values directly to a function inside the pharenthesis
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 56)

#---------------------------------------------------------------------------------------------------

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount: .2f} is due: {due_date}")

# display_invoice("John", 1500, "01/01")

#---------------------------------------------------------------------------------------------------
# return = statement used to end a function
#          and send a result back to the caller

# def add(x, y):
#     z = x+ y
#     return z

# def subtract(x , y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x - y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(1 , 2))
# print(multiply(1 , 2))
# print(divide(1 , 2))

#---------------------------------------------------------------------------------------------------------------------
# This function creates a new name

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("spongebob", "squarepants")

print(full_name)
    