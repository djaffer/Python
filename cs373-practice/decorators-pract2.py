
class cache_2:
    d = {}
    def __init__(self,f): #it is same thing to declare inside or outside
        self.f = f
        self.d = {} # same as declaring above
    # def __call__ (self, n) :
    #     if n not in self.d :
    #         self.d[n] = self.f(n)
    #         v = 1
    #     return self.d[n]
    def __call__ (self,n) :
        print(self.d)
        if n in self.d:
            v = self.d[n]
            print("cache: ",n)
            return v
        v = self.f(n)
        self.d[n] = v
        return v
 
# def __call__ (self,n) :
#         print(self.d)
#         if n in self.d:
#             v = self.d[n]
#             print("cache: ",n)
#             return v
#         v = self.f(n)
#         self.d[n] = v
#         return v
def cond (f):
    def g(n):
        assert n >=0
        return f(n)
    return g

@cache_2
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