# Default Arguments = A default value for certain parameters
#                    default is used when that argument is ommited
#                    make your functions more flexible, reduces # of arguments
#                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500, 0, 0.05)) # I need to send these parameters together to the function

#-----------------------------------------------------------------------------------------------
#If you want to send only the price, and the discount and taxes are always the same, try to define it inside the functions as it follows
# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

#print(net_price(500))

# print(net_price(500, 0.1)) #In this example,we defined the discount value to 10% and it will change the pre defined value inside the function
#print(net_price(500, 0.1, 0))

#------------------------------------------------------------------------------------------------
import time
def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(0, 10)