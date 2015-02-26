
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