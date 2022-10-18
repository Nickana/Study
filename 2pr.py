import math
x=10
print ("x = ", x)
t=1
print ("t = ", t)
z= (9 * math.pi * t + 10 * math.cos(x))/(math.sqrt(t) - abs (math.sin(t)))*(math.e ** x)
print("{0:.2f}".format(z))
input ()