# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0
print("--------MENU---------")
for key, value in menu.items():
    print(f"{key:10} : {value}") #In {key:10} means we allocated 10 spaces for the keys

while True:
    food = input("Select an item (q to quit)").lower() # when we add this .lower() it means we want to consider the capital Q also
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-------ORDER-------")   
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is: $ {total}")