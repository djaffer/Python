#!/usr/bin/env python3

# -----------
# Closures.py
# -----------

print("Closures.py")

class A :
    def __init__ (self) :
        self.a = []

    def get (self) :
        return self.a

    def add (self, v) :
        self.a.append(v)

x = A()
assert x.get() == [] #first it is empty so when you return the object
x.add(2)
assert x.get() == [2] #added 2 in the list
x.add(3)
assert x.get() == [2, 3]
x.a += [4]                  # violation of interface
assert x.get() == [2, 3, 4]
x.a = None
#x.get()+= [2] #not possible
print(x.get())                      # violation of interface
#assert x.get() == None

def A () :
    a = []

    class B :
        def get (self) :
            return a

        def add (self, v) :
            a.append(v)

    return B()

x = A()
assert x.get() == []
x.add(2)
assert x.get() == [2]
x.add(3)
assert x.get() == [2, 3]
#x.a += [4]              # AttributeError: 'A' object has no attribute 'a'
assert x.get() == [2, 3]
x.a = None               # ?
assert x.get() == [2, 3]
print(A().get()) #possible to call like that 

print("Done.")