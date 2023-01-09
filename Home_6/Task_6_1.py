# Есть матрица A размерностью 3*3 (список списков),
#  напишите программу, которая создает транспонированную матрицу.


import numpy as np



def transpond(list_A:list) -> list:
    print(list_A)
    list_B = list(zip(*list_A))
    print (list_B)



if __name__ == '__main__':
    list_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data = np.array(list_A)
    transpond(list_A)
    print(data.transpose())