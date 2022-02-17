revenue = int(input('Введите значение выручки компании: '))
cost = int(input('Введите значение издержек компании: '))
profit = revenue - cost
if profit > 0:
    print(f'Компания работает с прибылью, рентабельность составляет {profit / revenue}')
    workers = int(input('Численность сотрудников компании: '))
    print(f'Прибыль компании в пересчете на одного сотрудника составляет {profit / workers}')
elif profit < 0:
     print('Компания работает с убытком:', profit)
else:
    print('Компания работает в ноль')
