item_name = input('Введите название товара (закончить Enter): ')
i = 1
items = []
while item_name != '':
    item_price = float(input('Введите стоимость товара: '))
    item_count = int(input('Введите кол-во товара: '))
    item_unit = input('Введите единицу измерения товара: ')
    items.append((i, {'название': item_name, 'цена': item_price, 'количество': item_count, 'ед': item_unit}))
    i += 1
    item_name = input('Введите название товара (закончить Enter): ')
analytics = {'название': set(), 'цена': set(), 'количество': set(), 'ед': set()}
for item in items:
    print(item)
    analytics['название'].add(item[1].get('название'))
    analytics['цена'].add(item[1].get('цена'))
    analytics['количество'].add(item[1].get('количество'))
    analytics['ед'].add(item[1].get('ед'))
for item in analytics:
    print('Аналитика', item, ':', list(analytics[item]))
