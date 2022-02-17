summary = 0
is_ok = True
def my_sum(string_nums, start_sum):
    """Суммирует  все числа в строке и прибавляет к ранее вычисленному результату"""
    for num in string_nums.split(' '):
        try:
            start_sum += float(num)
        except:
            return start_sum, False
    return start_sum, True
while is_ok:
    summary, is_ok = my_sum(input('Введите числа рвзделенные пробелом: '), summary)
    print(summary)
