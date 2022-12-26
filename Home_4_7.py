# Напишите программу для решения квадратного
# уравнения. В процессе поиска решения
# использовать обработку исключительных ситуаций.
# Ax^2+Bx + C
from math import sqrt
def int_set():
    while True:
        try:
            ret = int(input("Введите число: "))
        except ValueError:
            print("Это не число")
        else:
            return ret

A = int_set()
B = int_set()
C = int_set()


D = B**2 - 4*A*C
print (f"{A}*x^2{B:+}{C:+}=0")
print(f"Дискриминант = {D}")
try:
    if D < 0:
        print("Корни являются комплексными числами")
    elif D == 0:
        print (f"X1,2 = {(-B)/(2*A)}")
    else:
        print (f"X1 = {round((-B-sqrt(D))/(2*A),2)}\nX2 = {round((-B+sqrt(D))/(2*A),2)}")
except ZeroDivisionError:
    print("A не должен быть равен 0")