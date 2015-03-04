#!/usr/bin/env python3

# -----------------
# ClassVariables.py
# -----------------

print("ClassVariables.py")

class A :
#   v                   # NameError: name 'v' is not defined
    v0     = 0
#   v1     =   A.v0 + 1 # NameError: name 'A' is not defined
    v1     =     v0 + 1
    __v2   =     v1 + 1 # __v2 and _A__v2 become synonymous
    _A__v3 =   __v2 + 1 # __v3 and _A__v3 become synonymous
    _A__v3 = _A__v2 + 1
    v4     =   __v3 + 1
    v4     = _A__v3 + 1
    __v5   = 9
   # __v8 = 0

assert hasattr(A, "__dict__")

assert hasattr(A, "v0")
assert A.v0             == 0
assert A.__dict__["v0"] == 0

assert hasattr(A, "v1")
assert A.v1             == 1
assert A.__dict__["v1"] == 1

print(A.v1)
A.v1 = 2
print(A.v1)

_A__v5 = 3 # modified private variable and still worked amazing syntax for 
print(_A__v5) 
print("hasattr(A,_A__v2): ", hasattr(A,"_A__v2"))# could check if variable private is in a class

assert hasattr(A,"_A__v2")  
assert not hasattr(A, "__v2") # v2 is private variable if without _A then it does not find it

#assert A.__v2             == 2 # AttributeError: type object 'A' has no attribute '__v2'
#assert A.__dict__["__v2"] == 2 # KeyError: '__v2'

assert hasattr(A, "_A__v2")      # not really!
assert A._A__v2             == 2
assert A.__dict__["_A__v2"] == 2

A.__v2 = [2, 3, 4]
assert hasattr(A, "__v2")
assert hasattr(A, "_A__v2")
assert A.__v2             == [2, 3, 4]
assert A.__dict__["__v2"] == [2, 3, 4]
assert A.__v2 is not A._A__v2 #local and global private class variable
print("_A__v2: ", A._A__v2) #when multiple variables created with __ it makes different local variable
assert A._A__v2 == 2

assert not hasattr(A, "__v3")   # __v3 is private
#assert A.__v3             == 3 # AttributeError: type object 'A' has no attribute '__v3'
#assert A.__dict__["__v3"] == 3 # KeyError: '__v3'

assert hasattr(A, "_A__v3")      # not really!
assert A._A__v3             == 3
assert A.__dict__["_A__v3"] == 3

assert hasattr(A, "v4")
assert A.v4             == 4
assert A.__dict__["v4"] == 4

assert not hasattr(A, "v5")
#assert A.v5             == 4 # AttributeError: type object 'A' has no attribute 'v5'
#assert A.__dict__["v5"] == 4 # KeyError: 'v5'

A.v5 = [2, 3, 4]
assert hasattr(A, "v5")
assert A.v5             == [2, 3, 4]
assert A.__dict__["v5"] == [2, 3, 4]

A.__v7 = 5
assert hasattr(A, "__v7") # can easily make variables outside class 
assert A.__dict__["__v7"] == 5 
print(A.__v7)             == 5 

A._A__v8 = 5
assert hasattr(A, "_A__v8") # can easily make private variables outside class as well so no privacy 
assert A.__dict__["_A__v8"] == 5 
print(A._A__v8)            

assert not hasattr(A, "__v6")
#assert A.__v6             == 5 # AttributeError: type object 'A' has no attribute '__v6'
#assert A.__dict__["__v6"] == 5 # KeyError: '__v6'

A.__v6 = [2, 3, 4]