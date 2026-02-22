#format specifiers = {:flags} format a value based on what
#                               flags are inserted

# .(number)f = round to what many decimal places (fixed point
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14153
price2 = -98700.65
price3 = 12000.34

# print(f"Price 1 is $ {price1:.2f}") # They will change in a particular way depending what is inserted inside the comma
# print(f"Price 2 is $ {price2:.2f}") # 2f means the number of decimal that will be displayed
# print(f"Price 3 is $ {price3:.2f}")

# print(f"Price 1 is $ {price1:.1f}") # They will change in a particular way depending what is inserted inside the comma
# print(f"Price 2 is $ {price2:.1f}") # 2f means the number of decimal that will be displayed
# print(f"Price 3 is $ {price3:.1f}")

# print(f"Price 1 is $ {price1:10}") # Add 10 spaces before the price
# print(f"Price 2 is $ {price2:10}") 
# print(f"Price 3 is $ {price3:10}")

# print(f"Price 1 is $ {price1:010}") # Right justify the numbers with zeros
# print(f"Price 2 is $ {price2:010}") 
# print(f"Price 3 is $ {price3:010}")

# print(f"Price 1 is $ {price1:<10}") # Left justify the numbers
# print(f"Price 2 is $ {price2:<10}") 
# print(f"Price 3 is $ {price3:<10}")

# print(f"Price 1 is $ {price1:>10}") # Right justify the numbers
# print(f"Price 2 is $ {price2:>10}") 
# print(f"Price 3 is $ {price3:>10}")

# print(f"Price 1 is $ {price1:^10}") # center align the numbers
# print(f"Price 2 is $ {price2:^10}") 
# print(f"Price 3 is $ {price3:^10}")

# print(f"Price 1 is $ {price1:+}") # It shows the positive values
# print(f"Price 2 is $ {price2:+}") 
# print(f"Price 3 is $ {price3:+}")

# print(f"Price 1 is $ {price1:,}") # It uses the comma to separate big numbers
# print(f"Price 2 is $ {price2:,}") 
# print(f"Price 3 is $ {price3:,}")

print(f"Price 1 is $ {price1:+,.2f}") # It uses the comma to separate big numbers and displays 2 decimals and add a positive value
print(f"Price 2 is $ {price2:+,.2f}") 
print(f"Price 3 is $ {price3:+,.2f}")

