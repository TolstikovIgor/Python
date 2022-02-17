class Road:
    def __init__(self, _length, _width, weight, height):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.height = height

    def count_mass(self):
        road_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Масса асфальта для покрытия дороги 20м * 5000м * 25кг * 5см = {road_mass} т.')

build_road = Road(20, 5000, 25, 5)
build_road.count_mass()
