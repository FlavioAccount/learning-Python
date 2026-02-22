# Variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in
# Open this link to see the LEGB - https://pbs.twimg.com/media/GLC4wJ1WoAIC4Le.jpg

#Functions can't see what is inside another function. It is like a house in a neighbor,
#you can see the house but you cannot see what is inside the house.

# local -> Enclosed -> Global -> Built-in

#------------------------------------------------------------------------------------------
# Local functions has the declarations inside them

def func1():
    x = 1
    print(x)

def func2():
    x = 1
    print(x)

func1()
func2()

#-------------------------------------------------------------------------------------------
#Enclosed function - It occurs when the code has one function inside another function

def func1():
    x = 1 
    print(x)

    def func2():
        x = 2
        print(x) #If you declare the x = 1 in the first function but keep The x = 2, it will print x = 2

func1()
func2()

#But instead if you delete the x = 2 but keep the x = 1, It will print x = 1

def func3():
    x = 3 
    print(x)
    def func4():
        print(x)
    func4( ) 

func3()

#---------------------------------------------------------------------------------------------------------------
#Global Declaration 

x = 42 # If there is one global declaration of X but you keep the declarations inside the functions, I will print the Declarations inside the function

def func1():
    x = 5
    print(x)

def func2():
    x = 6
    print(x)

func1()
func2()

#If you delete the x inside the functions, It will print x = 42:

x = 42 

def func1():
    print(x)

def func2():
    print(x)

func1()
func2()

#-----------------------------------------------------------------------------------------------------------------------------
# If you try to print the code bellow, it will print the euller number rather than 3. The e = euller will be printed
# This will happen because the python is looking for local -> Enclosed -> Global -> Built-in
# The built-in is the last that will be seen by Python

from math import e #This is also the built-in version of e

def func1():
    print(e) #This is the built-in version of e

e = 3 #This is the Global version of e

func1()




