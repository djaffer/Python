#!/usr/bin/env python3

# --------
# Cache.py
# --------

print("Cache.py")

x = 2
y = 2 + 0
assert x is y #true because less than 257

x = 257
y = 257
assert x is y # true because less than 257

x = 257            # cache: [-5, 256] is same until then and can use is to compare
y = 257 + 0
assert x is not y #not same because integer becames immutable after 257
assert x ==     y #checks value
x -= 1
assert x is not y
assert x !=     y
y -= 1
assert x is y

x = -6             # cache: [-5, 256]
y = -6 + 0
assert x is not y
assert x ==     y
x += 1
assert x is not y
assert x !=     y
y += 1
assert x is y

x = 2.34
y = 2.34
assert x is y

x = 2.34
y = 2.34 + 0 #floating point if you add anything it becames a new floating
assert x is not y
assert x ==     y

s = "abc"
t = "abc"
assert s is t  #for string first it checks if it already has it in memory.

s = "abc"  # still works after concatanation
t = "ab" + "c"
assert s is t

s = "abc"
u = "ab"
v = "c"
t = u + v # had to trick python to make a new string
assert s is not t
assert s ==     t

a = []
b = []
c = a # pointing C to a 
c += [1,2] # adds to both c and a. Address is also same for both.
print(a)
assert a is not b # lists are mutable so it points to different address
assert a == c 
assert a is c 

b = ()
a = () 
assert a is b #tuples are imutable so it is pointing to same

b = (1,2,3)
a = b
b = b + (4,) # creates new tuple bc of immutable
a = a + (4,) #creates new tuple bc of immutable
print("tuple a and b:",a,b)
assert a is not b #tuples are imutable so it is pointing to same

a = set()
b = set()
assert a is not b
assert a ==     b

a = set()
b = a
b = b | {4,5} #this way in python only add in the datatype specified
a = b
b |= {1,2} #adds in both after pointing to a address
print("set a:",a)
print("set b:",b)
assert a is b
assert a == b

a = frozenset()
b = frozenset()
a = b
a |= {1,2}
b |= {1,2}
print("frozenset a and b",a,b)
assert a == b
# assert a is b #fails bc frozenset is immutable

a = {}
b = {}
assert a is not b 
assert a ==     b

a = {}
b = a
b = {1:"weqqe"} #immutable dictionary
print("dictionary a: ",a)
print("dictionary b:",b)
assert a is not b 
assert a != b

print("Done.")
