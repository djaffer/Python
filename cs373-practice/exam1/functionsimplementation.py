


def zip1(x,y):
	i = 0

	assert hasattr(x,"__iter__")
	assert hasattr(y,"__iter__")
	
	if len(x)<len(y):
		i = len(x)
	else:
		i = len(y)

	l = []
	xiter = iter(x)
	yiter = iter(y)
	for i in range(i):
		yield((next(xiter),next(yiter)))


def map1(f,i,j):
	x = zip(i,j)

	for g,h in x:
		yield(f(g,h))



def reduce1(f,i,initalizer=None):
	val = initalizer
	for v in i:
		val += f(v)
	return val


def filter1(f,it):
	l = []
	for i in it:
		l += f(i)
		#l.append(f(i))

	return l


gen = map1(lambda x,y : x+y ,[1,2,3],[1,2,3])

for i in gen:
	print(i)
red = reduce1(lambda x : x ,[1,2,3],0)

print("reduce",red)

li = filter1(lambda x: x>1,[-5,-4,-3,13])
print(li)
