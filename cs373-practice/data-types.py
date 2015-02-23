tu = (2,3)
tu += (3,4)
#tu[0] = 1 "immutable but still can concatenate elements"
print(len(tu))

s = {1,2,3,5}
#s[0] = {0} # not indexable
s |= {6} #to add use | operator
try:
	assert 8 in s # #not indexable cannot contain duplicate
except:
	print("error")
print("length of set: ",len(s))
print(s)

print(type(type(type)))