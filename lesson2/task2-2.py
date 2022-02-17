list_input = [int(i) for i in input('Введите числа через пробел: ').split()]
print(f'Ваш список {list_input}')
i = 0
while True:
    if i >= len(list_input) - 1:
        break
    list_input[i], list_input[i+1] = list_input[i+1], list_input[i]
    i += 2
print(f'Теперь ваш список выглядит так: {list_input}')
