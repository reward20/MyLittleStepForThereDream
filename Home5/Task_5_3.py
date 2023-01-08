# Создать и прочитать CSV файл с помощью Pandas.

# Запросить у пользователя данные (имя, фамилия, возраст)
#  и создать файл с этими значениями.

# Напишите программу, которая будет открывать
# определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай
# проверим, что задано положительное целое число).

# Требуется реализовать программу, которая выводит слово,
# имеющее максимальную длину
#(или список слов, если таковых несколько).

import pandas as pd
from pathlib import Path
# Создать и прочитать CSV файл с помощью Pandas.
class CSV_file():
    """
    Создать и прочитать CSV файл с помощью Pandas.
    """
    def __init__(self,file_path = Path(__file__).parent / "new.csv"):
        self.path_file = Path(file_path)
        if not self.path_file.exists():
            try:
                file = open(self.path_file, "w")
            except Exception as ex:
                print(ex)
            finally:
                file.close()

    def __str__(self):
        return self.path_file.__str__()

    def read(self):
        try:
            data = pd.read_csv(self.path_file,header= None,names = ["Name","Surname","Age"])
            if data.empty:
                print ("Base is empty")
            else:
                print(data.head())
        except pd.errors.EmptyDataError:
            print("File is empty")

    def write(self,lines: tuple):
        with open(self.path_file,"a+") as file:
            file.writelines(lines)


def open_read_file(file_path,number_off_line):
    """
    Напишите программу, которая будет открывать
    определенный файл file и выводить на печать построчно
    последние строки в количестве lines (на всякий случай
    проверим, что задано положительное целое число).
    """
    def print_l(line: list):
        for i in line:
            print(i,end="")

    path_open_file = Path(file_path)
    if path_open_file.exists():
        with open(path_open_file,"r") as file:
            lines = file.readlines()
            if lines.__len__() <= number_off_line:
                print_l(lines)
            else:
                print_l(lines[lines.__len__()-number_off_line:])

def user_input():
    """
    Запросить у пользователя данные (имя, фамилия, возраст)
    и создать файл с этими значениями.
    """
    name = input("write down your name: ")
    surname = input("write down your surname: ")
    age = input("write down your age: ")
    return f"{name},{surname},{age}\n"

def max_len_word(*lis_t: list):
    """
    Требуется реализовать программу, которая выводит слово,
    имеющее максимальную длину
    (или список слов, если таковых несколько).
    """
    temp_list = []
    max_len = 0
    for i in lis_t:
        if i.__len__() > max_len:
            max_len = i.__len__()
            temp_list.clear()
            temp_list.append(i)
        elif i.__len__() == max_len:
            temp_list.append(i)
    for i in temp_list:
        print(temp_list, sep=",")


if __name__ == '__main__':
    p = CSV_file()
    p.read()
    p.write(user_input())
    p.read()
    open_read_file("nums.txt",10)
    max_len_word("Bambino","Bentley","Cointrius","CUKY","Fourrmi","FYB","IBEH","JIEC","Malien","TipOK")
