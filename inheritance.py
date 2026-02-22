# Part I:

# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and externsibility
#               class Child(Parent)
#******************************************************************************************************************************************
# Part II

# Multilevel inheritance = inherit from more than one parent class
#                           C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                           C(B) <- B(A) <- A
#******************************************************************************************************************************************
# Part I - Classes
class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True #If you define one attribute inside your constructor, you are not obligated to define it into __init__
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):#When you use methods from another class, you are doing an innheritance
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")
#*****************************************************************************************************
# Part II - Classes

#OBS: If you are not assigning any attributes to your class, you don't need a constructor
class Prey(Animal): #Animal is the grandparent class and Prey is the parent class
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):#Children classes can inherit from more than one parent
        pass

class Hawk(Predator):#Child class
    pass

class Fish(Prey, Predator):
    pass



#*****************************************************************************************************
#Part I and Part II main function

def main():
#Part I -----------------------------------------------    
    dog = Dog("Scooby")
    cat = Cat("Garfield")
    mouse = Mouse("Mickey")
    print("--------------------------")
    print(dog.name)
    print(dog.is_alive)
    dog.eat()
    dog.sleep()
    dog.speak()
    print("--------------------------")
    print(cat.name)
    print(cat.is_alive)
    cat.eat()
    cat.sleep()
    cat.speak()
    print("--------------------------")
    print(mouse.name)
    print(mouse.is_alive)
    mouse.eat()
    mouse.sleep()
    mouse.speak()
    print("--------------------------")
#------------------------------------------------------
# Part II ---------------------------------------------
    rabbit = Rabbit("Antonio")
    hawk = Hawk("Sandra")
    fish = Fish("Janaina")
    
    fish.eat() # Inherited from grandparent class
    fish.flee()
    fish.hunt()


#------------------------------------------------------
if __name__ == "__main__":
    main()

#*****************************************************************************************************************************************************

