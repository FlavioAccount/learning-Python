# module = a file containing code you want to include in your program
#          use 'import' to include a mode (built-in or your own)
#          useful to break up a large program reusable separate files

#-------------------------------------------------------------------------------------------------------------------------
import math

# print(help("modules")) #In this command you can access the modules containig code to include in your program

print(math.pi)

#----------------------------------------------------------------------------------------------------------------------------------------------
import math as m #If you want to use another name rathen than the usual name, you can 'import math as m' or whatever name the module has

print(m.pi)

#-----------------------------------------------------------------------------------------------------------------------------------------------

from math import pi #It will import the module only. You no longer will need the module's name

print(pi)

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Be car eful when importing module as something, because it can make some confision

from math import e

a,b,c,d,e = 1,2,3,4,5

print (e ** a) # In this example, we are importing the module with name 'e' but at the same time we are using the variable 'e' to receive one integer
#The correct conding would be

import math
a,b,c,d,e = 1,2,3,4,5

print (math.e ** a) #Read this as math.e to the power of a

#---------------------------------------------------------------------------------------------------------------------------------------------------
#You can create your own modules externaly of your code. Here is an example

#On this first example, I will create an external module called moduleexample.py and I am gonna import it

import moduleexample 

print(moduleexample.area(2))
print(moduleexample.circumference(2))
print(moduleexample.cube(2))

#--------------------------------------------------------------------------------------------------------------------------------------------------



