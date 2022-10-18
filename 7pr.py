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

print("Задание 1, вычитание дробей через НОД ")
print("введите нумератор первой дроби: ")
a = int(input())
print("введите деноминатор первой дроби: ")
b = int(input())
print("введите нумератор второй дроби: ")
c = int(input())
print("введите денуменатор второй дроби: ")
d = int(input())

if d == b:  # same denominator
    a += c
    if NOD(a, b) == 1:
        print("Дробь и так не сократима", a, "/", b)
else:
    nok = (b * d) / NOD(b, d)
    a = a * (nok / b)
    c = c * (nok / d)
    print(a - c, "/", nok)

#---------------------------------------------------------------------

print("Задание 2, все делители числа, введите число: ")
a=int(input())
print([i for i in range(1,a+1) if a % i ==0 ])









