#!/usr/bin/env python3

# ----------------
# FunctionTuple.py
# ----------------

print("FunctionTuple.py")

def f (x, y = 1, *z) :
    assert type(z) is tuple
    return [x,y,z] 

def g (x, y, *z) :
    assert type(z) is tuple
    return [x, y, set(z)]

assert f(2, 3)       == [2, 3, ()] #z is set to tuple so even when it is not there it will be tuple
assert f(2, 3, 4)    == [2, 3, (4,)] #4 is taken as a part of tuple
assert f(2, 3, 4, 5) == [2, 3, (4, 5)] #extra argument just goes in the tuple

t = (3, 4)
u = (2,)
assert t            == (3, 4) # in tuple order does matter
assert t            != (4, 3)
assert f(2, t,  5)  == [2, (3, 4), (5,)] #last argument gets parsed in as tuple
assert f(2, 5,  t)  == [2, 5, ((3, 4),)] #if tuple already then tuple gets double parsed in tuple 
assert f(2, 5, *t)  == [2, 5, (3, 4)] #unpacks tuple and puts it in tuple bc of arg z set to type tuple 
assert f(2, *t)     == [2, 3, (4,)] #when unpacks first goes value to y and then remaining goes to z
assert f(*t)        == [3, 4, ()] #unpacks and assigns value to arg x and y. Empty tuple is for z.
assert f(y = 3, *u) == [2, 3, ()] #x gets value from u
assert f(*u, y = 3) == [2, 3, ()] # same as above unpacked first and x gets value as y is defined by name
#f(2, y = 5, *t)                          # TypeError: f() got multiple values for argument 'y'. When unpacking the args could not be more than total amount of args function can take
#f(x = 2, y = 5, *t)                      # TypeError: f() got multiple values for argument 'x'

l = [3, 4]
u = [2]
assert l            == [3, 4]
assert l            != [4, 3]
assert f(2, l,  5)  == [2, [3, 4], (5,)] #same as tuples 
assert f(2, 5,  l)  == [2, 5, ([3, 4],)] #l goes in the tuple without unpacking 
assert f(2, 5, *l)  == [2, 5, (3, 4)] #l is unpacked and gets parsed into tuple
assert f(2, *l)     == [2, 3, (4,)] #unpacks abd y get value from the list first and then rest of value goes into z 
assert f(y = 3, *u) == [2, 3, ()] 
assert f(*u, y = 3) == [2, 3, ()]
assert f(2,3,4,5,6,7) == [2,3,(4,5,6,7)] #if have more args then needed then those get added to the tuple. Only possible when there are non-keyword args. 
p = (2,3)
print(f(2, 3,p))
#f(2, y = 5, *l)                          # TypeError: f() got multiple values for argument 'y'. Unpacking should not have more args then the function args
#f(x = 2, y = 5, *l)                      # TypeError: f() got multiple values for argument 'x'. Unpacking should not have more args then the function args

s = {3, 4} #order does not matter for sets
u = {2}
assert s            == {4, 3}
assert s            == {3, 4}
assert f(2, s,  5)  == [2, {3, 4}, (5,)]
assert f(2, 5,  s)  == [2, 5, ({3, 4},)]
assert g(2, 5, *s)  == [2, 5, {3, 4}] # unpacks and puts in set again
assert g(2, *s)     == [2, 3, {4}]       # unpacks y gets 3 and z gets 4 which is typecasted to to set.
assert g(y = 3, *u) == [2, 3, set()]  #u gets unpacked and value goe to x
assert g(*u, y = 3) == [2, 3, set()]
print("g(2,s): ",g(2,s))
#g(2, y = 5, *s)                          # TypeError: f() got multiple values for argument 'y'
#g(x = 2, y = 5, *s)                      # TypeError: f() got multiple values for argument 'x'

p = {"bc" : 4, "ad" : 3, "ab":5}
d = {"b" : 4, "a" : 3} #order does not matter in dict
u = {2 : "c"}
assert d                    == {'b' : 4, 'a' : 3} 
assert d                    == {'a' : 3, 'b' : 4}
assert f(2, d,  5)          == [2, {'a' : 3, 'b' : 4}, (5,)] # y gets dict
assert f(2, 5,  d)          == [2, 5, ({'a' : 3, 'b' : 4},)] #d gets typcasted in set
assert g(2, 5, *d.keys())   == [2, 5, {'b', 'a'}] 
print("g(2, *p.keys()): ",g(2, *p.keys())) # [2,"bc",{"ad"}] # order does not matter so it gets multiple values
# assert g(2, *p) == [2,"bc",{"ad"}] or [2,"ad",{"bc"}]
assert g(2, 5, *d.values()) == [2, 5, {3, 4}] #additional values gets added to set
assert g(2, 5, *d.items())  == [2, 5, {('a', 3), ('b', 4)}] #gets the values in tuple and then typecasted to set
assert g(2, 5, *d)          == [2, 5, {'a', 'b'}] #gets the keys of dict same as d.keys

print("dictionary keys unpacking:g(2, 5, *d): ",g(2, 5, *d))

assert g(2, *d)             == [2, 'a', {'b'}] or [2, 'b', {'a'}]               # ?
assert g(y = 3, *u)         == [2, 3, set()]
assert g(*u, y = 3)         == [2, 3, set()]
#f(2, y = 5, *d)                                             # TypeError: f() got multiple values for argument 'y'
#f(x = 2, y = 5, *d)                                         # TypeError: f() got multiple values for argument 'x'
#f(**d)                                                      # TypeError: f() got an unexpected keyword argument 'a'

d = {"z" : 4, "y" : 3}
#f(2, **d)             # TypeError: f() got an unexpected keyword argument 'z'
#f(**d)                # TypeError: f() got an unexpected keyword argument 'z'

d = {"y" : 3, "x" : 2}
#f(2, **d)                   # TypeError: f() got multiple values for keyword argument 'x'
assert f(**d) == [2, 3, ()]

d = {"y" : 3}
assert f(2,     **d) == [2, 3, ()]
assert f(x = 2, **d) == [2, 3, ()]
#f(**d)                             # TypeError: f() takes at least 2 arguments (1 given)

d = {"y" : 3, "t" : 5}
#f(2,     **d)         # TypeError: f() got an unexpected keyword argument 't'
#f(x = 2, **d)         # TypeError: f() got an unexpected keyword argument 't'
#f(**d)                # TypeError: f() got an unexpected keyword argument 't'

x = set() #mutable
x = {1,2,3}

assert x == {2,3,1} # in sets and dictionary prder does not matter

print("Done.")