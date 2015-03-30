#! usr/bin/env python

def g(n):
        try:
            x=n
            if x==3:
                raise e
            return x
        except Exception as e:
            print(Exception)

        

g(1)
g(3)

x = 1.0
y = 6
y = x
print(x is y)
y = 1.0 + 0
print("x :", x)
print("y :",y)
print(x is y)
