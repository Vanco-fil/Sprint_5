import random
import string


def create_random_user():
    name = ''.join(random.choices(string.ascii_letters, k=6))
    login = f"Ivan_Ashchepkov_8_{random.randint(100, 999)}@yandex.ru"
    password = random.randint(100000, 999999)
    return name, login, password


def incorrect_password_user():
    name = ''.join(random.choices(string.ascii_letters, k=6))
    login = f"Ivan_Ashchepkov_8_{random.randint(100, 999)}@yandex.ru"
    password = random.randint(10000, 99999)
    return name, login, password
