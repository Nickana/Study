a=input ("Первое число\n")
b=input ("Второе число\n")
c=input ("Третье число\n")
if a < b and c:
	print (a, "Меньше переменной " + b + " и " + c)
elif b < a and c:
	print (b, "Меньше переменной " + a + " и " + c)
else:
	print (c, "Меньше переменной " + a + " и " + b)