# while loop = execute some code WHILE some condition remains true

# name = input("Type your name: ")

# while name == "": #while this condition is false, it will ask for your name
#     print("You did not type your name")
#     name = input("Type your name: ") #once the condition is true, it will move to the next code

# print(f"Hello {name}")


# print("Next code ---------------------------------------------------------------------------------------------")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# print(" Next code ------------------------------------------------------------------------------------")

# food = input("Enter the food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}: ")
#     food = input("Type q to quit: ")

# print("bye")
# print("Next code -------------------------------------------------------------------------------------------------------------------")
# num = int(input("Type one number between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter your number again. Should be between 1 - 10:"))

# print(f"Your number is {num}")

#Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle can't be less than or equal to zero")


while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero")


while time <= 0:
    time = int(input("Enter the time amount: "))
    if time <= 0:
        print("time can't be less than or equal to zero")


print(time)
print(principle)
print(rate)

total = principle *pow(1 + rate / 100, time)

print(f"balance after {time} year/s $ {total:.2f}")