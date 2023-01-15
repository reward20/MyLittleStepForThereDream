"""Напише функцию, которая может принимать произвольное количество
аргументов (целых чисел), и определять, сколько среди них
двухзначниых и трехзначных чисел. Определение количества
разрядов в числе также оформить в виде отдельной функции"""

from math import log10
from random import randint

def task_3(*args):
    print(*args)
    print(f"Одноразрядных:{check_discharge(*args,0)}")
    print(f"Двухразрядных:{check_discharge(*args,1)}")
    print(f"Трехразрядных:{check_discharge(*args,2)}")


def check_discharge(turple_,discharge):
    count = 0
    for item in turple_:
        if discharge == log10(item)//1:
            count += 1
    return count





if __name__ == '__main__':
    task_3([randint(1,999) for i in range(100)])