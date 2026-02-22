# super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

class Shape: #this is the super class. When you have attributes repeting, you can use a super class 
    
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}") #Pay attention!!! Very important to understand this structure

class Circle(Shape):

    def __init__(self, color, filled, radius):
        super().__init__(color, filled) #For the super() is necessary to call the constructor again everytime
        self.radius = radius

    def describe(self):
        print(f"It is a circle with a an area of {3.14 * self.radius * self.radius}")
        super().describe() #This is refering to the describe inside the super()

class Square(Shape):
    
    def __init__(self, color, filled, width):
        super().__init__(color, filled) #For the super() is necessary to call the constructor again everytime
        self.radius = width

class Triangle(Shape):
    
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled) #For the super() is necessary to call the constructor again everytime
        self.radius = width
        self.height = height

def main():
    circle = Circle("Red", True, 6)
    square = Square("Red", True, 5)
    triangle = Triangle("Blue", True, 6, 7)

    print("Circle --------------------------\n")
    print(circle.color)
    print(circle.filled)
    circle.describe()
    print("\nSquare ------------------------\n")
    print(square.color)
    print(square.filled)
    print("\nTriangle ----------------------\n")
    print(triangle.color)
    print(triangle.filled)
    print("\n---------------------------------")
    
if __name__=="__main__":
    main()