def count_words(string):
    return len(string.split())

def count_lines(file):
    file.seek(0, 0)
    return len(file.readlines())

with open('test.txt', 'r') as f:
    for i, line in enumerate(f.readlines(), 1):
        print(f'Слов в {i} строке: {count_words(line)}')
    print(f'Количество строк: {count_lines(f)}')
