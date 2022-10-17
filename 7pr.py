from random import *
import math


def NOD(a, b):
    a = abs(a)
    b = abs(b)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a+b


a = -23	
b = 14
c = 1
d = 15

if d == b:  # same denominator
    a += c
    if NOD(a, b) == 1:
        print("Дробь и так не сократима", a, "/", b)
else:
    nok = (b * d) / NOD(b, d)
    a = a * (nok / b)
    c = c * (nok / d)
    print(a - c, "/", nok)










