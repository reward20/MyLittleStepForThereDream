import random
# в текстовом файле nums.txt хранятся вещественные файлы
# Вывести их на экран и вычислить их количество
def create_txt_random():
    with open("nums.txt","w+") as fl:
        for i in range(1000):
            r = ",".join([str(round(random.random() * 10,2)) for i in range(4)])
            r = r + "\n"
            fl.write(r)
            fl.flush()
def open_txt():
    with open("nums.txt","r") as fl:
        lst_line = fl.readlines()
        for i in lst_line:
            print (i.replace("\n",""))
        print("Количество строк",lst_line.__len__())

if __name__ == '__main__':
    open_txt()


