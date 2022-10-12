from random import *

lst = [randint(-1, 10) for x in range(50)]
print (lst)
for i in range(len(lst)):
	print(lst[i],lst[i+1]) if lst[i]<0 and lst[i+1]<0 else None