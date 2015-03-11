def cond (f):
	def g(n):
		assert n >=0
		return f(n)
	return g

def cache (f) :
    d = {}
    def g (n) :
    	if n in d:
    		v = d[n]
    		print("cache: ",n)
    		return v
    	v = f(n)
    	d[n] = v
    	return v
    return g

def cache_1 (f) :
    d = {}
    def g (n) :
        if n not in d :
            d[n] = f(n)
        return d[n]
    return g

@cache
@cond
def fib(n):
	if n <=1:
		return n
	else:
		return fib(n-1)+fib(n-2)

print(fib(5))
print(fib(2))
print(fib(3))

print(fib(10))
print(fib(14))
print(fib(10))
print(fib(5))