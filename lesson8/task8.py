import random


class LotoGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        # Тут с помощью random.sample я получаю не повторяющиеся числа
        self._NUMBERS_COUNT = 90
        MAX_NUMBER = 90
        # Вы можете использовать random.shuffle на сгенерированном списке, например генератором списков!
        self._numbers_in_bag = random.sample(range(1, MAX_NUMBER + 1), self._NUMBERS_COUNT)

    def _get_number(self):
        return self._numbers_in_bag.pop()

    def start(self):
        for i in range(self._NUMBERS_COUNT):
            print(self._player, self._computer)
            number = self._get_number()
            print('Новый бочонок {}, осталось {}'.format(number, len(self._numbers_in_bag)))
            choice = input('Хотите зачеркуть? y/n:\n')
            if choice == 'y':
                # Тут мы зачеркиваем число если оно есть, если нет, а игрок попытался, то он проиграл.
                if not self._player.try_stroke_number(number):
                    print('Игрок проиграл!')
                    break
            elif self._player.has_number(number):
                print('Игрок проиграл!')
                break
            # Компьютер не ошибается =)
            # if random.random() < 0.02:
            #     pass  # в 2% случаеав
            if self._computer.has_number(number):
                self._computer.try_stroke_number(number)


class LotoCard:

    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [[],
                      [],
                      []]
        self._MAX_NUMBER = 90
        self._MAX_NUMBERS_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5

        # Числа для будущей карты лото
        # random.sample - позволяет получить набор случайных, но уникальных чисел!
        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBERS_IN_CARD)

        # цикл вставляющий пробелы и цифры в нашу карту
        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        # Данная функция возвращает либо число, которое непосредственно на линии, либо случайное, чтобы случайно расставить пробелы.
        def check_sort_item(item):
            if isinstance(item, int):
                return item
            return random.randint(1, self._MAX_NUMBER)

# [' ',' ',' ',' ', 80,2,1,3,5]
# [' ', 80, 3,2,1, ' ']
# [1, ' ', 2, 3, ' ', 80]
#[3 25]

        # Здесь мы именно сортируем списки внутри списка
        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)


    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
        return False

    def try_stroke_number(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '-'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._MAX_NUMBERS_IN_CARD:
                        raise Exception('{} победил!'.format(self.player_type))
                    return True
        return False
# ['23 ', '11 ', '3  ', ' 56']
# [     1  3 56]
    # Метод для строкового представления объекта
    def __str__(self):
        MAX_FIELD_LENGTH = 3
        header = '\n{}:\n--------------------------'.format(self.player_type)
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(MAX_FIELD_LENGTH)  # Выравниваем, добавляя пробелы, если это необходимо.
            body += '\n'
        return header + body

human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = LotoGame(human_player, computer_player)
game.start()
