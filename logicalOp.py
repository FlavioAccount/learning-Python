#Logical operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not false, not True)

temp = 25
is_raining = False
is_sunny = True
# or operator
if temp > 35 or temp < 0 or is_raining: # is_raining must be True
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# and operator

if temp >= 28 and is_sunny:
    print("it is HOT outside ")
    print("it is SUNNY ")
elif temp <= 0 and is_sunny:
    print("It is COLD outside ") 
    print("It is snowing")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside ")
    print("It is SUNNY ")