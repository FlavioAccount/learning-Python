# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multimple keyword-arguments
#           * UNPACKING OPERATOR
#           1. positional 2. default 3. keyword 4 ARBITRARY

# def add(*arg): #When you use this *args you are going to create a tuple with the arguments declared
#     print(arg) 

# print(add(1, 2))
#------------------------------------------------------------------------------------------------------------
# def add(*args): #When you use this *args you are going to create a tuple with the arguments declared
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1, 3, 5))
#------------------------------------------------------------------------------------------------------------
# def display_name(*args):
#     for arg in args:
#         print(arg, end =" ")
# display_name("Spongebob", "Harold", "Squarepants", "III") #You can add multiple inputs in the same tuple
#------------------------------------------------------------------------------------------------------------
# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street ="123", #If you do like this, you are going to put these variables inside a dictionary
#               city="Detroit", 
#               state="Michigan", 
#               zip="54321")
#-------------------------------------------------------------------------------------------------------------
def shipping_label(*args, **kwargs):#You can add both args and kwargs together and receive this input from another place
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()
    if "apt" in kwargs:
        print(f"The street is: {kwargs.get("street")} apartment: {kwargs.get("apt")}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get("street")}")
        print(f"PObox: {kwargs.get("pobox")}")
    
    print(f"{kwargs.get("city")} {kwargs.get("state")} {kwargs.get("zip")}")
shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
            street="123 Fake St.",
            apt= 100,
            pobox="PO box #1001",
            city="Detroit",
            state="MI",
            zip="54321")


