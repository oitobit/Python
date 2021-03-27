"""Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
"""

"""Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
    """
    
a = "hello world"
b = 123
c = 1.2
d = 1j
e = ["banana","laranja","morango"]
f = ("banana","laranja","morango")
g = range(6)
h = {"name": "Joao", 
     "age": 25}
i = {"banana","laranja","morango"}
j = frozenset({"banana","laranja","morango"})
l = True
m = b"hello"
n = bytearray(5)
o = memoryview(bytes(5))

#types class
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(l))
print(type(m))
print(type(n))
print(type(o))

