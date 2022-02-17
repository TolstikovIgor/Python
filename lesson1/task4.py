num_user = int(input('Enter int: '))
current_max = 0
num = num_user  # отдельная переменная для хранения оставшейся части

while num > 0:
    digit = num % 10  # отделяем последнюю цифру
    if digit > current_max:
        current_max = digit
        if current_max == 9:  # Необязательно, максимальное число в любом случае 9
            break
    num = num // 10  # отсекаем от числа последнюю цифру

print(f'Наибольшая цифра у введенного числа {num_user}:', current_max)
