with open("5.txt", "w+") as f:
    try:
        user_enter = input('Введите числа через пробел: ')
        f.writelines(user_enter)
        answer = user_enter.split()
    except ValueError:
        print('Ошибка ввода данных')
    print(sum(map(int, answer)))
