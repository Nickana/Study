# a = int(input())#5
# b = int(input())#2
# c = int(input())#5
# d = int(input())#1
a = 5
b = 2
c = 5
d = 1




def NOD(a,b):
	i = a
	j = b
	while i !=0 and j != 0:
		if i > j:
			i = i%j
		else:
			j = j%i

	return (i+j)

d1 = a*d - c*b
d2 = b*d


print ((-15//4))