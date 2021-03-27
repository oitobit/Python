"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

myVar = "Rodrigo"
MYVAR = "Rodrigo"
myvar = "Rodrigo"
_my_var_ = "Rodrigo"
myVar2 = "Rodrigo"

print(myVar)
print(MYVAR)
print(myvar)
print(_my_var_)
print(myVar2)

"""
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:
"""

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "Rodrigo Franca"
print(myVariableName)
