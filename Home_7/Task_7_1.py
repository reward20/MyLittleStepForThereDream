import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from math import sqrt




def task_1():
    """
    Назвать график, обозначить оси,
    рассчитать среднеквадратичное отклонение,
    построить график и сохранить
    его в формате jpeg.
    """
    pd_r = pd.read_csv(Path("data.csv"), sep=",")
    pd_r.X = list([float(i.replace(",", ".")) for i in pd_r.X.to_list()])
    pd_r.Y = list([float(i.replace(",", ".")) for i in pd_r.Y.to_list()])
    plt.title("График")
    plt.xlabel("Ось Х")
    plt.ylabel("Ось Y")
    plt.plot(pd_r.X, pd_r.Y)
    plt.savefig("ping.jpeg")
    plt.show()
    print(pd_r.to_numpy()[0:1])

def task_2():
    labels = ['1 Mo', '3 Mo', '6 Mo', '1 Yr', '2 Yr', '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr']
    july16_2007 = [4.75, 4.98, 5.08, 5.01, 4.89, 4.89, 4.95, 4.99, 5.05, 5.21, 5.14]
    july16_2020 = [0.12, 0.11, 0.13, 0.14, 0.16, 0.17, 0.28, 0.46, 0.62, 1.09, 1.31]

    fig = plt.figure()
    axes = fig.add_axes([2, 0, 1, 1])
    plt.title("Кривая доходности")
    plt.plot(labels, july16_2007, label="2007")
    plt.plot(labels, july16_2020, label="2020")
    plt.grid(True)
    plt.legend()
    plt.show()

def task_3():

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

    D = B ** 2 - 4 * A * C
    print(f"{A}*x^2{B:+}x{C:+}=0")
    print(f"Дискриминант = {D}")
    try:
        if D < 0:

            raise ValueError
        elif D == 0:
            x1 = x2 = (-B) / (2 * A)
            print(f"X1,2 = {x2}")
        else:
            x1 = round((-B - sqrt(D)) / (2 * A), 2)
            x2 = round((-B + sqrt(D)) / (2 * A), 2)
            print(f"X1 = {x1}\nX2 = {x2}")
    except ZeroDivisionError:
        print("A не должен быть равен 0")
    except ValueError:
        print("Корни являются комплексными числами")
    else:
        plt.grid(True)
        plt.plot([i for i in range(-100, 100)], [A * x ** 2 + B * x + C for x in range(-100, 100)])

if __name__ == '__main__':
    task_1()
    task_2()
    task_3()