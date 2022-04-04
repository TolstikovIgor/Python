list_1 = [1, 5, 3, 4, 7, 5, 6, 1, 48, 11, 10, 2, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]
list_2 = [x for x in list_1 if list_1.count(x) == 1]
print(list_2)
