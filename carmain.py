# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object


class Car:  # The class should always have the first letter capitalized
    def __init__(self, model, year, color, for_sale):  # constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    def describe(self):
        print(f"{self.year}{self.color}{self.model}")
def main():
    car1 = Car("Mustang", 2024, "red", False)

    car2 = Car("Corvette", 2025, "blue", True)
    print("Car 1: ----------------------------------------------------------------------------------")
    print(car1) #If you print this object, I will show you the address of the object
    print(car1.model) #This will print the model of the car rather than the address of the object
    print(car1.year) #This will print the year of the car rather than the address of the object
    print(car1.color) #This will print the color of the car rather than the address of
    print(car1.for_sale) #This will print whether the car is for sale or not rather than the address of the object
    car1.drive()
    car1.stop()


    print("----------------------------------------------------------------------------------------")
    
    print("Car 2: ----------------------------------------------------------------------------------")
    print(car2) #If you print this object, I will show you the address of the object
    print(car2.model) #This will print the model of the car rather than the address of the object
    print(car2.year) #This will print the year of the car rather than the address of the object
    print(car2.color) #This will print the color of the car rather than the address of
    print(car2.for_sale) #This will print whether the car is for sale or not rather than the address of the object
    print("----------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()