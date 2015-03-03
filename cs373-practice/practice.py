
x = [1,2,3,4,5,6,7,8,9,10]
l = (v for v in x if v%2)
x[2] = 13
print(list(l))
print(list(l))

def g (x=set()) : # SyntaxError: non-default argument follows default argument
	x |= {2}
	return x

print(g())
print(g())

x = {3}
y = {3}

print(x == y)

x = 10 - 5
y = 15 - 10
print(x is y)

def f () :
    x, y = 1, 1
    print("outside loop")
    while True :
        yield x
        x, y = y, x + y

p = f()
q = f()
print(p is q)
r = iter(p)
print(r is p)
v = next(p)
print(v)
v = next(p)
print(v)
v = next(p)
print(v)
v = next(p)
print(v)
v = next(q)
print(v)


def f (x = 2, y = 3, *z, **t) :
    return [x, y, z, t]

t = (4, 5)
d = {"z" : 6 , "t" : 7}


print(f())
print(f( t,   d))
print(f( t,  *d))
print(f(t,3,**d))
print(f(*t, **d))
print(f(7, *t, **d))

assert (f()) == [2, 3, (), {}]
assert (f( t,   d)) == [(4,5),{"z" : 6 , "t" : 7},(),{}]
assert (f( t,  *d)) == [(4,5),'z',('t',),{}] or [(4,5),'t',('z',),{}]
assert (f( t, **d)) == [(4,5),3,(),{"z" : 6 , "t" : 7}]
assert (f(*t, **d)) == [4,5,(),{"z" : 6 , "t" : 7}]
assert (f(7, *t, **d)) == [7,4,(5,),{"z" : 6 , "t" : 7}]

d = {"x":1,"y":3}
print(f(t=3,z=2,**d))