from random import *
#1
lst = [randint(-1, 10) for x in range(10)]
print (lst)
for i in range(len(lst)):
	print(lst[i],lst[i+1]) if lst[i]<0 and lst[i+1]<0 else None

#2
arr2 = []

for el in lst:

   if el not in arr2:

       arr2.append(el)

print(arr2)
