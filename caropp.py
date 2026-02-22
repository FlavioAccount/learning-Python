#This is a support library for the carmain.py file. It contains the class definition for the Car class and the creation of two car objects. It also prints out the attributes of each car object.

from carmain import Car
car3 = Car("Camaro", 2023, "yellow", True)

print("Car 3: ----------------------------------------------------------------------------------")
print(car3) #If you print this object, I will show you the address of the object
print(car3.model) #This will print the model of the car rather than the address of
print(car3.year) #This will print the year of the car rather than the address of the object
print(car3.color) #This will print the color of the car rather than the address of
print(car3.for_sale) #This will print whether the car is for sale or not rather
car3.drive()
car3.stop()
print("----------------------------------------------------------------------------------------")
