# import sys
#
# hours, salary_per_our, bonus = map(float, sys.argv[1:])
# print('Salary - {}'.format(hours * salary_per_our + bonus))

# my_list = [1, 9, 1, 72, 3, 4, 5, 6, 3]
# new_list = [num for i, num in enumerate(my_list) if num > my_list[i - 1] and i != 0]
# print(new_list)

# print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])

# my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]
# new_list = [x for x in my_list if my_list.count(x) == 1]
# print(new_list)

# from functools import reduce
#
#
# def mul_list(n1, n2):
#     return n1 * n2
#
#
# my_list = [x for x in range(100, 1001) if x % 2 == 0]
# print(reduce(mul_list, my_list))

# # a
# from itertools import count, cycle
#
# for i in count(int(input('Введите стартовое число: '))):
#     print(i)
#
# # b
# my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]
#
# iter = cycle(my_list)
# stop = ''
# while stop != 'q':
#     print(next(iter), end='')
#     stop = input()

# from math import factorial
# from itertools import count
#
#
# def fibo_gen():
#     for el in count(1):  # бесконечный цикл, который начинается с 1
#         yield factorial(el)
#
#
# # a
# x = 1
# for i in fibo_gen():
#     print('Factorial {} - {}'.format(x, i))
#     if x == 15:
#         break
#     x += 1
# 
# # b
# for step, i in enumerate(fibo_gen(), start=1):
#     print('Factorial {} - {}'.format(step, i))
#     if step == 15:
#         break


# f_obj = open('test.txt')
# txt = f_obj.read()
# print(txt)

# lines = f_obj.readlines()

# print(lines)
# for line in lines:
#     print(line.strip())
#     print(line, end='')
# f_obj.close()
# print(f_obj.readline())
# print(f_obj.readline())
# print(f_obj.readline())
# print(f_obj.readline())
# print(f_obj.readline())
# print(f_obj.readline())
# for line in f_obj:
#     print(line)


# f_obj = open('2342.txt', 'w')
# f_obj.write('qwe\nasd\nzxc\n123\n13')
# f_obj.write('qwe\nasd\nzxc\n123\n13')
# lines = ['qwe\n', 'asd\n', 'zxc\n']
# f_obj.writelines(lines)
# f_obj.close()

# with open('2342.txt', 'w+', encoding='utf-8') as f_obj:
#     # f_obj.write('qwe\nasd\nzxc\n123\n13')
#     # f_obj.write('\n0')
#     # f_obj.seek(0)
#     # print(f_obj.tell())
#     # print(f_obj.read())
#     print(f_obj.closed)
#     print(f_obj.mode)
#     print(f_obj.name)

# with open("python.txt", "w") as f_obj:
#     print("Необычная работа функции print", file=f_obj)


# import os

# os.rename('1234.txt', '12344.txt')
# print(os.path.exists('12344.txt'))
# print(os.path.exists('123441111.txt'))
# os.remove('12344.txt')
# print(os.listdir())
# print(os.path.isdir('0610'))
# print(os.path.isfile('0610'))

# import json

# data = {'income': {'salary': 5000, 'bonus': [100, 200]}}

# print(json.dumps(data))
# with open('12022021.json', 'w') as f_json:
#     json.dump(data, f_json)

# with open('12022021.json') as f_json:
#     data_loaded = json.load(f_json)
#
# print(data_loaded)
# print(type(data_loaded))

# print(json.loads('{"income": {"salary": 5000, "bonus": [100, 200]}}'))


# import shutil
# shutil.copy('10042020.txt', '10042021123.txt')
# shutil.copyfile('10042020.txt', '10042021123.txt')

# import sys
# sys.exit(1)


# Работа с файлами. Открытие, закрытие, чтение и запись
# f = open("my_file.txt", 'r')

# Чтение данных из файла
# f_obj = open("my_file.txt")
# f_obj = open(r"C:\Users\User_1\Desktop\proj\text.txt", "r")

# Метод read()
# my_f = open("text.txt", "r")
# content = my_f.read()
# print(content)
# my_f.close()

# Метод readline()
# my_f = open("text.txt", "r")
# content = my_f.readline()
# print(content)
# my_f.close()

# Метод readlines()
# my_f = open("text.txt", "r")
# content = my_f.readlines()
# print(content)
# my_f.close()

# Чтение файла по частям
# my_f = open("text.txt", "r")
#
# for line in my_f:
#     print(line)
#
# my_f.close()

# my_f = open("text.txt", "r")
#
# while True:
#     content = my_f.read(1024)
#     print(content)
#
#     if not content:
#         break

# Чтение бинарных (двоичных) файлов
# my_f = open("text.pdf", "rb")

# Запись данных в файл
# out_f = open("out_file.txt", "w")
# out_f.write("String string string")
# out_f.close()

# out_f = open("out_file.txt", "w")
# str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
# out_f.writelines(str_list)
# out_f.close()

# Менеджеры контекста
# with open("text.txt") as f_obj:
#     for line in f_obj:
#         print(line)

# # было
# f_obj = open("text.txt")
#
# # стало
# with open("text.txt") as f_obj:

# Выявление ошибок при работе с файлами
# try:
#     f_obj = open("text.txt")
#     for line in f_obj:
#         print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     f_obj.close()

# try:
#     with open("text.txt") as f_obj:
#         for line in f_obj:
#             print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# Режимы доступа к файлу
# Режим x
# f_1 = open("my_file.txt", 'w')
# f_2 = open("my_file.txt", 'x')

# Режим a
# f_obj = open("new_f.txt", 'a')
# f_obj.write("My string")
# f_obj.close()

# Режим b
# f_obj = open("data.bin", "wb")
# my_var = "if5s"
# f_obj.write(my_var)
# f_obj.close()

# Режим +
# with open("file.dat", "w+") as f_obj:
#     f_obj.write("another string")
#     f_obj.seek(0)
#     content = f_obj.read()
#     print(content)

# f_obj.write("another string")

# Параметры файлового объекта
# f_obj = open("new_f.txt", "w")
# print("Файл. Имя: ", f_obj.name)
# print("Файл. Закрыт: ", f_obj.closed)
# print("Файл. Режим: ", f_obj.mode)

# Определение позиции указателя в файле
# f_obj = open("new_f.txt", "r")
# content = f_obj.read()
# print(content)
# content = f_obj.read()
# print(content)
# f_obj.close()

# f_obj = open("new_f.txt")
# f_obj.read(10)
# print("Текущая позиция:", f_obj.tell())
# f_obj.close()

# file_obj.seek(offset, [from])

# f_obj = open("new_f.txt")
# print(f_obj.read(3))
# print("Мы находимся на позиции: ", f_obj.tell())
# # Перемещаемся в начало
# f_obj.seek(0)
# print(f_obj.read(10))
# f_obj.close()

# Print в файл
# with open("python.txt", "w") as f_obj:
#     print("Необычная работа функции print", file=f_obj)

# Модуль os
# os.remove()
# import os
#
# os.remove("my_file.txt")

# os.rename()
# import os
#
# os.rename("test.txt", "pytest.txt")

# os.listdir()
# import os
#
# content = os.listdir(path=".")
# print(content)

# import os
#
# content = os.listdir()
# print(content)

# import os
#
# content = os.listdir(path="..")
# print(content)

# os.path
# os.path.basename()
# import os
#
# print(os.path.basename(r"C:\Users\Администратор\settings.py"))

# os.path.dirname()
# import os
#
# print(os.path.dirname(r"C:\Users\Администратор\settings.py"))

# os.path.exists()
# import os
#
# print(os.path.exists(r"C:\Users\Администратор\settings.py"))

# os.path.isdir(), os.path.isfile()
# print(os.path.isdir(r"C:\Users\Администратор\settings.py"))
# print(os.path.isfile(r"C:\Users\Администратор\settings.py"))

# os.path.join()
# import os
#
# print(os.path.join(r"C:\Users\Администратор", "settings.py"))

# os.path.split()
# import os
#
# print(os.path.split(r"C:\Users\Администратор\settings.py"))

# Модуль json
# {
#     "worker": "Jon Smith",
#     "skills": ["programming", "design", "engineering"],
#     "age": 40,
#     "workplaces": [
#         {
#             "first": "IBM",
#             "time": "2010-2014"
#         },
#         {
#             "second": "Apple",
#             "time": "2014-2018"
#         }
#     ]
# }

# JSON и Python
# import json

# Сериализация
# data = {
#     "income": {
#         "salary": 50000,
#         "bonus": 20000
#     }
# }

# with open("my_file.json", "w") as write_f:
#     json.dump(data, write_f)

# {"income": {"salary": 50000, "bonus": 20000}}

# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))

# Десериализация
# with open("my_file.json") as read_f:
#     data = json.load(read_f)
#
# print(data)
# print(type(data))

# json_str = """{"income": {"salary": 50000, "bonus": 20000}}"""
# data = json.loads(json_str)
#
# print(data)
# print(type(data))

# Модуль shutil
# shutil.copyfileobj(f_obj_1, f_obj_2)

# shutil.copyfile(f_1, f_2)

# shutil.copy(my_f, my_target)

# shutil.copy(my_tree, my_target)

# shutil.rmtree(path)

# shutil.move(my_obj, my_target)

# Модуль sys
# sys.argv
# sys.executable
# import sys

# print(sys.executable)

# sys.exit
# import sys
#
# sys.exit(0)

# import sys
#
# print(sys.path)

# sys.platform
# import sys
#
# print(sys.platform)

# sys.stdin / stdout / stderr

# handle = open("test.txt")
# handle = open(r"/home/igor/PycharmProjects/1/test.txt", "r")

# handle = open("test.txt", "r")
# data = handle.read()
# print(data)
# handle.close()

# handle = open("test.txt", "r")
# data = handle.readline() # read just one line
# print(data)
# handle.close()

# handle = open("test.txt", "r")
# data = handle.readlines() # read ALL the lines!
# print(data)
# handle.close()

# handle = open("test.txt", "r")
#
# for line in handle:
#     print(line)
#
# handle.close()

# handle = open("test.txt", "r")
#
# while True:
#     data = handle.read(1024)
#     print(data)
#
#     if not data:
#         break

# handle = open("test.pdf", "rb")

# handle = open("test.txt", "w")
# handle.write("This is a test!")
# handle.close()

# with open("test.txt") as file_handler:
#     for line in file_handler:
#         print(line)

# try:
#     file_handler = open("test.txt")
#     for line in file_handler:
#         print(line)
# except IOError:
#     print("An IOError has occurred!")
# finally:
#     file_handler.close()

# try:
#     with open("test.txt") as file_handler:
#         for line in file_handler:
#             print(line)
# except IOError:
#     print("An IOError has occurred!")

# f = open('test.txt')
# f.read(1)
# f.read()

# f = open('test.txt')
# for line in f:
#     line

# l = [str(i)+str(i-1) for i in range(20)]
# l
#
# f = open('test.txt', 'w')
#
# for index in l:
#     f.write(index + '\n')
#
# f.close()

# f = open('text.txt', 'r')
# l = [line.strip() for line in f]
# l
# f.close()
