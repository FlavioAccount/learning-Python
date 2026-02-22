# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property #This decorator doesn't allow to access the width directly
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter #You can add a setter method if you want to write or set an attribute
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    
    @height.setter #You can add a setter method if you want to write or set an attribute
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than zero")
    
    @width.deleter
    def width(self):
        del self._width
        print("The width has been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("The height has been deleted")

def main():
    rectangle = Rectangle(3, 4)
    print(rectangle.width)
    print(rectangle.height)

    rectangle.width = 7
    rectangle.height = 8

    print(rectangle.width)
    print(rectangle.height)

    del rectangle.width
    del rectangle.height

if __name__=="__main__":
    main()