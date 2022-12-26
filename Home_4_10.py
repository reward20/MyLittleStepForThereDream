# Создать матрицу 3*3, заполнить ее
# рандомными значениями. Заменить все
# четные числа на нули.

import numpy as np
from random import randint

matrix = np.zeros((3,3),int)

for c,i in enumerate(matrix):
    for f,j in enumerate(i):
        temp = randint(1,9)
        matrix[c,f] = temp if temp % 2 == 0 else 0

print(matrix)