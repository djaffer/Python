"""
#draws circle with squares
import turtle

def shape():
    dan = turtle.Turtle();
    dan.color("yellow")
    dan.shape("arrow")
    dan.speed(10)

    

    for i in range(0,36):
        for x in range(0, 4):
            dan.forward(100)
            dan.right(90)
        dan.right(10)


        
#main
window = turtle.Screen()
window.bgcolor("red")
shape()
window.exitonclick()

i = 5
c = 1
while i>1:
    if i%2==0:
        i = i//2
    else:
        i = 3*i + 1
    c +=1
print(i)
print(c)
"""
# from functools import reduce

a = [2, 3, 4]
b = [5, 6, 7]
z = (x+y for x in a if x%2 for y in b if y%2)
b[0] = 6
print(list(z))
print(list(z))
d = (x+x for x in a)
print(type(d))
print(list(d))
print(list(d))

for v in range(5) :
    print(v)
    if v == 3 :
        print()
        break
else :
    print("else")

g = iter(a)
f = iter(a)
h = g
print(g == f)


it = [1,2,3]
fun = lambda x: x*x
gen = filter(lambda x: x%2==0,it)

print(list(gen))
# print((lambda x: x**2)(2))
#print ((lambda x, y: x*y)(3, 4))

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print(list(result))