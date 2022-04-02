# Импортирование в Python
# Импорт модуля из стандартной библиотеки

# import time
# import random
# print(time.time())
# print(random.random())

# Использование инструкции from

# from time import time
# from random import random
# print(time())
# print(random())

# Создание собственного модуля
# def show_msg():
#     print("Приветствие!")
#
#
# def simple_calc():
#     x = int(input("Введите значение x: "))
#     return x ** 2 - 1

# import my_functions
#
# my_functions.show_msg()
# print(my_functions.simple_calc())

# from my_functions import show_msg
# from my_functions import simple_calc
#
# show_msg()
# print(simple_calc())

# Запуск скрипта с параметрами

# from sys import argv
#
# script_name, first_param, second_param, third_param = argv
#
# print("Имя скрипта: ", script_name)
# print("Параметр 1: ", first_param)
# print("Параметр 2: ", second_param)
# print("Параметр 3: ", third_param)

# python script_params_test.py раз 2 true

# Генераторы списков и словарей

# Генераторы списков

# my_list = [2, 4, 6]
# new_list = [el+10 for el in my_list]
# print(f"Исходный список: {my_list}")
# print(f"Новый список: {new_list}")

# my_list = [2, 4, 6]
# print(f"Исходный список: {my_list}")
# new_list = []
# for el in my_list:
#    new_list.append(el + 10)
# print(f"Новый список: {new_list}")

# lines = [line.strip() for line in open('text.txt')]
# print(lines)

# my_list = [10, 25, 30, 45, 50]
# print(my_list)
# new_list = [el for el in my_list if el % 2 == 0]
# print(new_list)

# str_1 = "abc"
# str_2 = "d"
# str_3 = "efg"
# sets = [i+j+k for i in str_1 for j in str_2 for k in str_3]
# print(sets)

# my_tuple = (2, 4, 6)
# new_obj = (el+10 for el in my_tuple)
#
# print(new_obj)

# my_tuple = [2, 4, 6]
# new_obj = (el+10 for el in my_tuple)
#
# print(new_obj)

# Генераторы словарей и множеств

# my_dict = {el: el*2 for el in range(10, 20)}
# print(my_dict)

# my_set = {el**3 for el in range(5, 10)}
# print(my_set)

# Модуль random как генератор псевдослучайных чисел

# Генерация целых случайных чисел

# import random
# print(random.randint(0, 10))

# from random import randint
# print(randint(0, 10))

# from random import randint
# print(randint(-100, -10))

# from random import randrange
# print(randrange(10))

# from random import randrange
# print(randrange(10, 20))

# from random import randrange
# print(randrange(20, 30, 3))

# Генерация дробных случайных чисел

# from random import random
# print(random())

# from random import random
# print(random() * 10)

# from random import random
# print(random() * (10 - 4) + 4)

# Конструкция yield

# generator = (param * param for param in range(5))
#
# for el in generator:
#     print(el)

# generator = (param * param for param in range(5))
#
# for el in generator:
#     print(el)
#
# print(next(generator))

# def generator():
#     for el in (10, 20, 30):
#         yield el
#
# g = generator()
# print(g)
#
# for el in g:
#     print(el)

# Модуль functools

# Функция reduce()

# from functools import reduce
#
# def my_func(prev_el, el):
#     # prev_el - предыдущий элемент
#     # el - текущий элемент
#     return prev_el + el
#
# print(reduce(my_func, [10, 20, 30]))

# Функция partial()

# from functools import partial
#
# def my_func(param_1, param_2):
#     return param_1 ** param_2
#
# new_my_func = partial(my_func, 2)
# print(new_my_func)
# print(new_my_func(4))

# Модуль itertools

# Функция count()

# from itertools import count
#
# for el in count(7):
#     if el > 15:
#         break
#     else:
#         print(el)

# Функция cycle()

# from itertools import cycle
#
# с = 0
# for el in cycle("ABC"):
#     if с > 10:
#         break
#     print(el)
#     с += 1

# from itertools import cycle
#
# progr_lang = ["python", "java", "perl", "javascript"]
# iter = cycle(progr_lang)
#
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))

# count (<Начало>, <Шаг>)
# Возвращает равномерно распределённые переменные, начиная с числа — стартового параметра. Можно указать параметр шага.
# from itertools import count
# for i in count(2, 3):
#     if i >= 20:
#         break
#     else:
#         print(i)

# cycle (<Итерируемый объект>)
# Итератор, создающий бесконечный цикл поочерёдного вывода неких символов или чисел.
# from itertools import cycle
# count = 1
# for i in cycle('DOG'):
#     if count > 7:
#         break
#     print(i)
#     count += 1

# repeat (<Объект>, <Количество повторений>)
# Итератор, осуществляющий повторение объекта, переданного в качестве первого параметра в функцию.
# from itertools import repeat
# data = [i for i in repeat('DOG', 5)]
# print(data)

# combinations (<Объект>, <Количество значений>)
# Функция комбинирования элементов последовательности. Комбинация всех возможных значений без повторяющихся элементов
# from itertools import combinations
# data = list(combinations('DOGA', 3))
# print(data)

# combinations_with_replacement (<Объект>, <Количество значений>)
# Комбинация всех возможных значений с повторяющимися элементами
# from itertools import combinations_with_replacement
# for i in combinations_with_replacement('DOG', 3):
#     print(''.join(i))

# permutations (<Объект>, <Количество значений>)
# Комбинация с перестановкой всех возможных значений
# from itertools import permutations
# for i in permutations('DOG', 3):
#     print(''.join(i))

# product (<Массив данных>)
# Комбинация, полученная из всех возможных значений вложенных списков
# from itertools import product
# data = list(product((0, 1), (2, 3), (3, 4)))
# print(data)

# Фильтрация последовательности
# filterfalse
# Все элементы, для которых функция возвращает ложь
# from itertools import filterfalse
# data = list(filterfalse(lambda i: i == 0, [1, 2, 3, 7, 0, 8, 4, 5, 1]))
# print(data)

# dropwhile
# Все элементы, начиная с того, для которого функция вернет ложь
# from itertools import dropwhile
# data = list(dropwhile(lambda i: i != 0, [1, 2, 3, 0, 8, 4, 5, 1]))
# print(data)

# takewhile
# Все элементы, до тех пор, пока функция не вернет истину
# from itertools import takewhile
# data = list(takewhile(lambda i: i != 0, [1, 2, 3, 7, 8, 0, 4, 5, 1]))
# print(data)

# compress
# Удаление элементов, для которых было передано значение ложь
# from itertools import compress
# data = list(compress('DOGa', [True, False, True, True]))
# print(data)

# chain
# Поочередное объединение списков при помощи итераторов
# from itertools import chain
# data1 = ['D', 'O', 'G']
# data2 = [0, 1, 2, 3, 4, 5]
# data = list(chain(data1, data2))
# print(data)

# chain.from_iterable
# Аналогично chain, но аргумент — список, в который вложены объединяемые списки.
# from itertools import chain
# data = [['D', 'O', 'G'], [0, 1, 2, 3, 4, 6]]
# data2 = [0, 1, 2, 3]
# data = list(chain.from_iterable(data))
# print(data)

# starmap
# В заданную функцию передает список подставляемых аргументов
# from itertools import starmap
# for i in starmap(pow, [(1, 2), (2, 2), (3, 2), (4, 3)]):
#     print(i)

# accumulate
# Каждый элемент результирующей последовательности равен сумме текущего и всех предыдущих исходной последовательности
# from itertools import accumulate
# data = list(accumulate([1, 2, 10, 4]))
# print(data)

# islice
# Получение среза, благодаря указанному количеству элементов
# from itertools import islice
# from itertools import count
# for i in islice(count(0, 2), 7):
#     print(i)

# zip_longest
# Объединение нескольких итераций с повышением размера до максимального
# from itertools import zip_longest
# for i in zip_longest('DOG', [0, 1, 2, 3, 4], fillvalue= ' '):
#     print(i)

# tee
# Создание кортежа из нескольких готовых итераторов
# from itertools import tee
# data = 'DOGa'
# i1, i2 = tee(data)
# for i in i1:
#     print(i)
# for i in i2:
#     print(i)

# groupby
# Группировка элементов последовательности по некоторым ключевым значениям
# from itertools import groupby
# animals = [('CAT', 'TOM'), ('MOUSE', 'JARRY')]
# for key, group in groupby(animals, lambda kind: kind[0]):
#     for kind, name in group:
#         print(f'{name} is a {kind}'.format(name = name, kind = kind))


# Модуль math

# from math import ceil, fabs, factorial, floor, \
#    fmod, isfinite, modf, sqrt, sin, cos, tan, degrees, radians
#
# print(f"ceil() -> {ceil(6.75)}")
# print(f"fabs() -> {fabs(-4)}")
# print(f"factorial() -> {factorial(5)}")
# print(f"floor() -> {floor(4.34)}")
# print(f"fmod() -> {fmod(9, 4)}")
# print(f"isfinite() -> {isfinite(10)}")
# print(f"modf() -> {modf(10.5)}")
# print(f"sqrt() -> {sqrt(16)}")
# print(f"sin() -> {sin(1.5708)}")
# print(f"cos() -> {cos(1.5708)}")
# print(f"tan() -> {tan(1.5708)}")
# print(f"degrees() -> {degrees(1.5708)}")
# print(f"radians() -> {radians(90)}")

# Циклы
# captains = ['Janeway', 'Picard', 'Sisko']
# for captain in captains:
#     print(captain)

# numbers_divisible_by_tree = [3, 6, 9, 12, 15]
# for num in numbers_divisible_by_tree:
#     quotient = num / 3
#     print(f"{num} делится на 3, результат {int(quotient)}.")

# Введение в range()
# for i in range(3, 16, 3):
#     quotient = i / 3
#     print(f"{i} делится на 3, результат {int(quotient)}.")

# for i in range(1, 8):
#     print(i)

# Инкрементация с range()
# for i in range(3, 100, 25):
#     print(i)

# Декрементация с range()
# for i in range(10, -6, -2):
#     print(i)

# for i in reversed(range(5)):
#     print(i)

# Углубляемся в range()
# float и range()
# float
# for i in range(3.3):
#     print(i)

# Использование NumPy
# import numpy as np
# np.arange(0.3, 1.6, 0.3)

# import numpy as np
# for i in np.arange(0.3, 1.6, 0.3):
#     print(i)

# Функции для получения целых "случайных" чисел – randint() и randrange()
# from random import random, randrange, randint
# random.randint(0, 10)

# Декораторы
# def my_shiny_new_decorator(function_to_decorate):
#     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
#     # получая возможность исполнять произвольный код до и после неё.
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает до вызова функции")
#         function_to_decorate() # Сама функция
#         print("А я - код, срабатывающий после")
#     # Вернём эту функцию
#     return the_wrapper_around_the_original_function
#
# # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
# def stand_alone_function():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
#
# stand_alone_function()
# # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# # который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# # готовую к использованию функцию:
# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()

# stand_alone_function = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function()

# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print("Оставь меня в покое")
#
# another_stand_alone_function()

# def bread(

# Передача декоратором аргументов в функцию
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print("Смотри, что я получил:", arg1, arg2)
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
#
# # Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку",
# # передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
#
# print_full_name("Vasya", "Pupkin")

# Декорирование методов
# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie -= 3
#         return method_to_decorate(self, lie)
#     return wrapper
#
# class Lucy:
#     def __init__(self):
#         self.age = 32
#     @method_friendly_decorator
#     def sayYourAge(self, lie):
#         print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))
#
# l = Lucy()
# l.sayYourAge(-3)

# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     # Данная "обёртка" принимает любые аргументы
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         print("Передали ли мне что-нибудь?:")
#         print(args)
#         print(kwargs)
#         function_to_decorate(*args, **kwargs)
#     return a_wrapper_accepting_arbitrary_arguments
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print("Python is cool, no argument here.")
#
# function_with_no_argument()
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print(a, b, c)
#
# function_with_arguments(1, 2, 3)
# @a_decorator_passing_arbitrary_arguments
# def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
#     print("Любят ли {}, {} и {} утконосов? {}".format(a, b, c, platypus))
#
# function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
# class Mary(object):
#     def __init__(self):
#         self.age = 31
#     @a_decorator_passing_arbitrary_arguments
#     def sayYourAge(self, lie=-3): # Теперь мы можем указать значение по умолчанию
#         print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))
#
# m = Mary()
# m.sayYourAge()

# Декораторы с аргументами
# def decorator_maker():
#     print("Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать декоратор.")
#     def my_decorator(func):
#         print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")
#         def wrapped():
#             print ("Я - обёртка вокруг декорируемой функции.\n"
#                    "Я буду вызвана каждый раз, когда ты вызываешь декорируемую функцию.\n"
#                    "Я возвращаю результат работы декорируемой функции.")
#             return func()
#         print("Я возвращаю обёрнутую функцию.")
#         return wrapped
#     print("Я возвращаю декоратор.")
#     return my_decorator
#
# # Давайте теперь создадим декоратор. Это всего лишь ещё один вызов функции
# new_decorator = decorator_maker()
# # Теперь декорируем функцию
# def decorated_function():
#     print("Я - декорируемая функция.")
#
# decorated_function = new_decorator(decorated_function)
# # Теперь наконец вызовем функцию:
# decorated_function()

# @decorator_maker()
# def decorated_function():
#     print("Я - декорируемая функция.")
#
# decorated_function()

# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
#     print("Я создаю декораторы! И я получил следующие аргументы:",
#            decorator_arg1, decorator_arg2)
#     def my_decorator(func):
#         print("Я - декоратор. И ты всё же смог передать мне эти аргументы:",
#                decorator_arg1, decorator_arg2)
#         # Не перепутайте аргументы декораторов с аргументами функций!
#         def wrapped(function_arg1, function_arg2):
#             print ("Я - обёртка вокруг декорируемой функции.\n"
#                    "И я имею доступ ко всем аргументам\n"
#                    "\t- и декоратора: {0} {1}\n"
#                    "\t- и функции: {2} {3}\n"
#                    "Теперь я могу передать нужные аргументы дальше"
#                    .format(decorator_arg1, decorator_arg2,
#                            function_arg1, function_arg2))
#             return func(function_arg1, function_arg2)
#         return wrapped
#     return my_decorator
#
# @decorator_maker_with_arguments("Леонард", "Шелдон")
# def decorated_function_with_arguments(function_arg1, function_arg2):
#     print ("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
#            " {1}".format(function_arg1, function_arg2))
#
# decorated_function_with_arguments("Раджеш", "Говард")

# Некоторые особенности работы с декораторами
# def foo():
#     print("foo")
#
# print(foo.__name__)
# # Однако, декораторы мешают нормальному ходу дел:
# def bar(func):
#     def wrapper():
#         print("bar")
#         return func()
#     return wrapper
#
# @bar
# def foo():
#     print("foo")
#
# print(foo.__name__)
# import functools  # "functools" может нам с этим помочь
# def bar(func):
#     # Объявляем "wrapper" оборачивающим "func"
#     # и запускаем магию:
#     @functools.wraps(func)
#     def wrapper():
#         print("bar")
#         return func()
#     return wrapper
#
# @bar
# def foo():
#     print("foo")
#
# print(foo.__name__)

# Примеры использования декораторов
# def benchmark(func):
#     """
#     Декоратор, выводящий время, которое заняло
#     выполнение декорируемой функции.
#     """
#     import time
#     def wrapper(*args, **kwargs):
#         t = time.clock()
#         res = func(*args, **kwargs)
#         print(func.__name__, time.clock() - t)
#         return res
#     return wrapper
#
# def logging(func):
#     """
#     Декоратор, логирующий работу кода.
#     (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
#     """
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(func.__name__, args, kwargs)
#         return res
#     return wrapper
#
# def counter(func):
#     """
#     Декоратор, считающий и выводящий количество вызовов
#     декорируемой функции.
#     """
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         res = func(*args, **kwargs)
#         print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
#         return res
#     wrapper.count = 0
#     return wrapper
#
# @benchmark
# @logging
# @counter
# def reverse_string(string):
#     return ''.join(reversed(string))
#
# print(reverse_string("А роза упала на лапу Азора"))
# print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura,"
# "maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag,"
# "a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash,"
# "a jar, sore hats, a peon, a canal: Panama!"))
