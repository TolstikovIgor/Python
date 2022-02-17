my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]
new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)
