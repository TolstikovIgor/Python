class Cell():
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return self.num

    def __add__(self, other):
        return f"Сумма {self.num} + {other.num} = {self.num + other.num}"

    def __sub__(self, other):
        return self.num - other.num if self.num - other.num > 0 \
            else f"Ячеек в первой клетке меньше или равно второй"

    def __mul__(self, other):
        return f"Умножение {self.num} * {other.num} = {self.num * other.num}"

    def __truediv__(self, other):
        return f"Деление {self.num} / {other.num} = {self.num / other.num:.3f}" if other.num != 0 \
            else f"Делить на ноль нельзя"

    def make_order(self, rows):
        return "\n".join(["*" * rows for i in range(self.num // rows)]) + "\n" + "*" * (self.num % rows)

c_1 = Cell(10)
c_2 = Cell(44)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_2.make_order(10))
