# "Duck typing" = Another way to achieve polymorphism besides inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

def main():
    animals = [Dog(), Cat()]
    for animal in animals:
        animal.speak()

if __name__ =="__main__":
    main()

