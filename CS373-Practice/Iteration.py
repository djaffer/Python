
# -------------
# Indexables.py
# -------------

from itertools import count
from types     import GeneratorType

print("Iteration.py")

a = [2, 3, 4]
assert type(a) is list
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
assert     hasattr(a, "__len__")
s = 0
for v in a :
    s += v
assert s == 9
a = (2, 3, 4)
assert type(a) is tuple
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
assert hasattr(a, "__len__")

s = 0
for v in a :
    s += v
assert s == 9

a = {1,2,3}
assert hasattr(a, "__len__")

a = ["abc", "def", "ghi"]
for v in a :
    v += "x"                      # ?
assert a == ["abc", "def", "ghi"]

a = [[2], [3], [4]]
for v in a :
    v += [5]
    v += (10,)
    v += {15}
print(a)
assert a == [[2, 5, 10, 15], [3, 5, 10, 15], [4, 5, 10, 15]]

a = [(2, "abc"), (3, "def"), (4, "ghi")]
s = 0
for u, v in a :
    s += u
assert s == 9
x = range(10)
assert type(x) is range
assert not hasattr(x, "__next__")
assert     hasattr(x, "__iter__")
assert list(x) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert list(x) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = [2, 3, 4]
y = map(lambda v : v * 5, x)
x += [5]
x[0] = 6
assert x       == [6,   3,  4,  5]
assert list(y) == [30, 15, 20, 25]
assert list(y) == []
    
