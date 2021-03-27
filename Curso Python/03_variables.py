"""
Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""

name = "Rodrigo"
number = 25

print(name, number)

"""
Variables do not need to be declared with any particular type, and can even change type after they have been set.
"""
#last variable is that will appear
x = 25
x = "Rodrigo"

print(x)

"""
Casting
If you want to specify the data type of a variable, this can be done with casting.
"""
x1 = str(3) #type string
y1 = int(3) #type integer
z1 = float(3) #type float

print(x1)
print(y1)
print(z1)

"""
Get the Type
You can get the data type of a variable with the type() function.
"""

x2 = "Rodrigo"
y2 = 5

print(type(x2))
print(type(y2))

