from itertools import count, cycle

iterator = count(int(input('Для генерации списка введите первое число: ')))
print('Первые десять чисел начиная с введенного вами числа:')
for i in range(10):
    print(next(iterator), end=' ')

print('\nСтрока цикла')
lst = ['list', 1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]
iterator = cycle(lst)

for i in range(len(lst) * 2):
    print(next(iterator), end=' ')
