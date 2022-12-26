# Напишите программу, в которой решается
# уравнение вида А(А - 1)* x=sin(A) ,
# причем при значении A = 0 должно
# вычисляться решение x= -1.








from math import sqrt,sin
def int_set():
    while True:
        try:
            ret = int(input("Введите число: "))
        except ValueError:
            print("Это не число")
        else:
            return ret

A = int_set()

print (f"{A}({A}-1)*x=sin({A})")
print("X = ", end="")
try:
    print(sin(A)/(A*(A-1)))
except ZeroDivisionError:
    print("-1")