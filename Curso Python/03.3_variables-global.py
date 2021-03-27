"""Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""
x = "awesome"
def myFunc():
    print("Python is " + x)
myFunc()

"""If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
"""

x2 = "awesome"
def myFunc2():
    x2 = "fantastic"
    print("Python is " + x2)
    
myFunc2()
print("Python is " + x2)

"""The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Also, use the global keyword if you want to change a global variable inside a function.
"""

r = "awesome"
def Func3():
    global r
    r = "nice"
Func3()
print("Python is " + r)
