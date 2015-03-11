#! usr/bin/env


class A:

	g1 = 9
	__g2__ = 8
	g3 = [1,2,3]
	g4 = (1,2,3)

x = A()

print("global vars****************************************************************************")
print("x has g1: ",hasattr(x,"g1"))#by default it is in attr
print("g1 in x.__dict__[g1]","g1" in x.__dict__)#it is not in unless you modify var
print("x g1: ",x.g1)
print("A g1 :",A().g1)

x.g1 = 2 #only the instance var gets changed
print("g1 in x.__dict__[g1]","g1" in x.__dict__)#it gets added in dict only when value is changed
print("x g1: ",x.g1)
print("A g1: ",A().g1)
print("Ag1 is xg1: ",A().g1 is x.g1) 
print("*********************************************************************************")

print("global list****************************************************************************")
print("x has g1: ",hasattr(x,"g3"))#by default it is in attr
print("g1 in x.__dict__[g1]","g3" in x.__dict__)#it is not in unless you modify var
print("x g3: ",x.g3)
print("A g1 :",A().g3) 
print("Ag1 is xg3: ",A().g3 is x.g3) # if mutable it is going to be same


A.g3 += [4] #only the instance var gets changed
x.g3 += [5]
print("g1 in x.__dict__[g1]","g1" in x.__dict__)#it gets added in dict only when value is changed
print("x g3: ",x.g3)
print("A g1: ",A().g3)
print("Ag1 is xg3: ",A().g3 is x.g3)
f = A()
print("different class calling g3",f.g3)#variable is modified and reflected in anty new class 
del A.__g2
print("*********************************************************************************")


print("global private vars****************************************************************************")
print("x has g2: ",hasattr(x,"g2"))
print("g2 in x","g2" in x.__dict__)#it gets added in dict only when value is changed
print("x g1: ",x.__g2__)

print("Ag1 :",A().__g2__)	
print("Ag2 is xg2: ",A().__g2__ is x.__g2__)

x.__g2__ = 1
print("x has g2: ",hasattr(x,"g2"))
print("g2 in x","g2" in x.__dict__)#it gets added in dict only when value is changed
print("x g1: ",x.__g2__)
print("Ag1 :",A().__g2__)
print("Ag1 is xg1: ",A().__g2__ is x.__g2__)
print("*********************************************************************************")