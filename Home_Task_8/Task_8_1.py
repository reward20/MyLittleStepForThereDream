"""
Нпишите программу, осуществляющую провeрку логина и пароля
для входа в систему. Проверка введенных пользователем данных
должна осуществляться в отдельной функции, принимающей 
следующие параметры: имя пользователя, пароль, количество попыток
входа в систему (по умолчанию 3), сообщение выводимое 
пользователю в случае, если все попытки входа в систему исчерпаны
(по умолчанию: "Система заблокирована. Повторите попытку позже"
"""
count = 1


def account_verification(input_login, input_password, count_of_attemps=3,
                         failure_message="Система заблокирована. Повторите попытку через 5 минут"):
    log_admin = "admin"
    pass_admin = "admin"
    global count
    if count < count_of_attemps:
        if input_login == log_admin and input_password == pass_admin:
            print("hello admin")
        else:
            count += 1
            print("input data not correct")
    else:
        print(failure_message)


def log_in_system():
    login = input("Enter your username: ")
    password = input("Enter your password: ")
    return [login,password]
if __name__ == '__main__':
    account_verification(*log_in_system())
    account_verification(*log_in_system())
    account_verification(*log_in_system())


