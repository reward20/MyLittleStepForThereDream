"""
Напишите функцию, принимающую сведения об авторе (в виде
произвольного списка именованных аргументов) и выводящая их на экран
в указанном формате
"""

def task_2(FIO,data_born, data_dead,info, **kwargs):
    print(f"{FIO}({data_born}-{data_dead}) - {info}")

def start():
    data = {'FIO' : input("Введите ФИО "),
    'data_born' :input("Введите дату рождения "),
    'data_dead' : input("Введите дату смерти "),
    'info' : input("Введите краткую информацию ")}
    return data

if __name__ == '__main__':
    task_2(**start())
