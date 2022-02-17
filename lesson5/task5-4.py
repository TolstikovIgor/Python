file_1 = 'file_5_4in.txt'
file_1out = 'file_5_4out.txt'
lines = []
figures = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'zero': 'ноль'}
try:
    with open(file_1) as f:
        lines = f.readlines()
except IOError:
    print('Ошибка ввод-вывода')

try:
    with open(file_1out, 'w') as f:
        for line in lines:
            figure = figures[line.split()[0].lower()].title()
            f.write(figure + line[len(line.split()[0]):])
except IOError:
    print('Ошибка ввод-вывода')
