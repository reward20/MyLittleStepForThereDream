


def task_1_fibonachi(border:int):
    """
    Написать функцию, которая
    выводит ряд Фибоначчи
    по заданной границe N.
    """
    a = 0
    b = 1
    for i in range(border):
        print (a)
        c = a
        a = b + a
        b = c

def task_2(*args: list):
    from itertools import compress
    """
    Дана последовательность целых чисел.
    Найти минимальное среди простых чисел
    и максимальное среди чисел не
    являющихся простыми
    """
    lst_true = list(map(brute_force_of_divisors,args))
    ls_prime = list(compress(args,lst_true))
    ls_composite = list(compress(args,[not i for i in lst_true]))
    print ("Минимальное среди прсстых " + str(min(ls_prime)),"\n","Максимальное среди составных "+str(max(ls_composite)))


def brute_force_of_divisors(N:int) -> bool:
    j = 0
    i = 2
    while i*i <= N and j != 1:
        if N % i == 0:
            j = 1
        i = i + 1
    else:
        if j == 1:
            return False
        else:
            return True


if __name__ == '__main__':
    task_1_fibonachi(15)
    task_2(1,2,3,4,5,6,7,8,9)