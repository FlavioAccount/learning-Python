#In this exercise, we will code a calculator using 6 operators +,-,/,*,sqrt and exponencial
import math

operator = input("Which kind of operation do you want to do? /, -, +, *, sqrt or exp ")
num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))
result = 0
if operator == "/":
    result = num1/num2
elif operator == "-":
    result = num1 - num2
elif operator == "+":
    result = num1 + num2
elif operator == "*":
    result = num1 * num2
elif operator == "sqrt":
    result = math.sqrt(num1)
elif operator == "exp":
    result = int(math.pow(num1, num2))
else:
    print("Error, this is not allowed")

print(f"The result is: {result}")