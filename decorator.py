# Decorator = A function that extends the behavior of another function'
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")
import time
import functools #Imported for figonacci class

class Firstexample:
    def add_sprinkles(func):
        def wrapper(*args, **kwargs):
            print("You add sprinkles")
            func(*args, **kwargs)
        return wrapper

    def add_fudge(func):
        def wrapper(*args, **kwargs):
            print("You add a fudge")
            func(*args, **kwargs)
        return wrapper

    @add_sprinkles
    @add_fudge
    def get_ice_cream(flavor):
        print(f"Here is your {flavor} Ice Cream")

class Secondexample:

    def timer(func):
        def timer(*args, **kwargs): #This syntax means the function is gonna accept any (*args) number of position arguments that will be passed to it, and any number of Keyword arguments
            start_time = time.time() #Start time
            result = func(*args, **kwargs) # Call de decorated function
            end_time = time.time() # End time
            print(f"Function {func.__name__!r} took: {end_time - start_time:.4f} sec") #The !r is gonna add quotes in the terminal
        return timer
    
    @timer #It is a function that modifies another function. We can use it to see how many time such function takes to run
    def example_function(n):
        return f"The sum is {sum(range(n))}"
 
class Circle:

    def __init__(self, radius):
        self._radius = radius
    
    @property #The property is used to access one attribue indirectly
    def radius(self):
        """ Get the radius of the circle. """
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """ Set the radius ofthe circle. Must be positive """
        if value == 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def diameter(self):
        """Get the diameter of the circle."""
        return self._radius * 2
    
class Math:

    @staticmethod # The staticmethod is to define that the function belongs inside class but doesn't belong to a specific class
    def add(x, y):
        return x + y
    
    @staticmethod # Static methods doesn't have self arguments 
    def multiply(x, y):
        return x * y

class Person:

    species = "Homo Sapiens"

    @classmethod #This decorator allows to access only the attributes inside the class
    def get_species(cls):
        print(cls)
        return cls.species
    
    @functools.cache
    def fibonacci(n):
        if n < 2:
            return n
        return Person.fibonacci(n - 1) + Person.fibonacci(n - 2)

def main():
    Firstexample.get_ice_cream("Vanilla")
   
    print(Secondexample.example_function(1000000))
   
    circle = Circle(6)
   
    print(Math.add(5, 7)) #12
    print(Math.multiply(3, 4)) #12

    print(Person.get_species()) # Homo Sapiens


    print("Fibonacci")
    print(Person.fibonacci(100))
    

if __name__=="__main__":
    main()