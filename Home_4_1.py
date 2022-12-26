"""
Напишите программу, в которой пользователь
вводит целое число а программа определяет,
сколько в этом числе цифр 0, 1, 2 и так далее
до 9.
"""
from collections import Counter
str_ = input("Введите число: ")
if str_.isdigit():
    c = Counter(str_)
    for number, count in list(c.most_common()):
        print(f"Число {number} встречено {count} раз(а)")


