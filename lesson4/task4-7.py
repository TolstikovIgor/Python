from math import factorial

def gen_fact(f_n):
    for el in range(1, f_n + 1):
        yield el, factorial(el)

for el in gen_fact(int(input('Для вычисления факториала введите число: '))):
    print(f'{el[0]}! = {el[1]}')
