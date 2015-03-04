class A :
    v = [2, 3, 4]

x = A()
print(A.v is x.v) #true
print(A.v)
print()

x.v += (5,) # added to both 
print(A.v is x.v) # true
print(A.v) # [2,3,4]
print()

x.v = [6, 7, 8] #mutable so points to different address
print(A.v is x.v) #false
print(A.v) #[2,3,4,5]
print()

x.v += (9,) 
print(A.v is x.v) #false
print(A.v) #[2,3,4]
print()



class A :
    v = (2, 3, 4)

x = A()
print(A.v is x.v) #true
print(A.v)#(2,3,4)
print()

x.v += (5,)
print(A.v is x.v)#false
print(A.v)# (2,3,4)
print()

x.v = (6, 7, 8) 
print(A.v is x.v) #false
print(A.v) # (2,3,4)
print()

x.v += (9,)
print(A.v is x.v) #false
print(A.v) #2,3,4