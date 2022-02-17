import json
import codecs

with codecs.open('7.json', 'w') as jf:
    with open('7.txt') as f:
        subjects = {}
        middle = {}
        k, o = 0, 0
        line = f.read().split("\n")
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            subjects[i[0]] = profit
            if profit > 0:
                k += profit
                o += 1
            middle["average_profit"] = k / o
        all_list = [subjects, middle]
        json.dump(all_list, jf, ensure_ascii=False, indent=4)

print(f'Полная информация:\n{line}\nСреднее значение для всех фирм:\n{all_list}')
