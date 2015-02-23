
x = [1,2,3,4,5,6,7,8,9,10]
l = (v for v in x if v%2)
x[2] = 13
print(list(l))
print(list(l))