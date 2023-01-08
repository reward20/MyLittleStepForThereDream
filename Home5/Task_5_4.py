# Перевести csv файл в json.



import pandas as pd
from pathlib import Path


def convert_csv_to_json(file_csv_path):
    """
    # Перевести csv файл в json.
    :param file_csv_path:
    путь до csv файла
    :return:
    ничего не возвращает
    """
    if Path(file_csv_path).exists():
        file_csv_path = Path(file_csv_path)
        if file_csv_path.suffix == ".csv":
            pd.read_csv(file_csv_path).to_json(Path(file_csv_path.stem + ".json"))
        else:
            print("file is not csv")
    else:
        print("file not exist")

def create_file():
    """
        Напишите программу в которой создается текстовый файл.
        Имя файла вводится пользователем.
        Текст для файла вводится пользователем.
        При записи текста в файл все маленькие
        буквы заменяются на большие.
    """
    file_name = input("Input name file: ")
    text_for_file = input("inset a line: ")
    with open(file_name + ".txt","w") as file:
        file.write(text_for_file.upper())





if __name__ == '__main__':
    #convert_csv_to_json("data.csv")
    create_file()