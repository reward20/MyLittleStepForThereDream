# Создать файл, прочесть его, вывести количество строк файла.
# Создать файл, заменить в этом файле строку.
# Удалить строку из файла по ее индексу.
# Вставить строку в указанную позицию файла.
import random

def create_txt_random():
    with open("nums_2.txt","w") as fl:
        for i in range(1000):
            r = ",".join([str(round(random.random() * 10,2)) for i in range(4)])
            r = r + "\n"
            fl.write(r)
            fl.flush()
def open_txt():
    with open("nums_2.txt","r") as fl:
        lst_line = fl.readlines()
        for i in lst_line:
            print (i.replace("\n",""))
        print("Количество строк",lst_line.__len__())

def del_line_txt(y=0):
    with open("nums_2.txt","r") as fl:
        lst_line = fl.readlines()
        if lst_line.__len__():
            if lst_line.__len__() < y:
                del lst_line[lst_line.__len__()-1]
            else:
                del lst_line[y-1]
    with open("nums_2.txt", "w") as fl:
        fl.writelines(lst_line)


def insert_line_txt(str_n,y=0):
    str_n = str_n + "\n"
    with open("nums_2.txt", "r") as fl:
        lst_line = fl.readlines()
        if lst_line.__len__():
            if lst_line.__len__() < y:
                lst_line.append(str_n)
            else:
                lst_line.insert(y-1,str_n)
    with open("nums_2.txt", "w") as fl:
        fl.writelines(lst_line)


if __name__ == '__main__':
    create_txt_random()
    open_txt()
    del_line_txt(2)
    insert_line_txt("Jupyter",1)