class Car:
    _registry = []

    def __init__(self, speed=None, color=None, name=None, is_police=False):
        self._registry.append(self)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return self.name + ' - машина поехала'

    def stop(self):
        return self.name + ' - машина остановилась'

    def turn(self, direction):
        return self.name + ' повернула ' + direction

    def get_show_speed(self, max_speed=None):
        speed_message = f'{self.name}\nТекущая скорость: {self.speed}'
        return speed_message

class TownCar(Car):

    def get_show_speed(self, max_speed=40):
        message_error = ''
        if max_speed:
            if self.speed > max_speed:
                message_error = f'\nПревышение скорости на {self.speed - max_speed}!' \
                                f'\nМаксимальная скорость: {max_speed}\n'

        return super().get_show_speed() + message_error

class SportCar(Car):
    pass

class WorkCar(Car):

    def get_show_speed(self, max_speed=60):
        message_error = ''
        if max_speed:
            if self.speed > max_speed:
                message_error = f'\nПревышение скорости на {self.speed - max_speed}!' \
                                f'\nМаксимальная скорость: {max_speed}\n'
        super().get_show_speed()
        return super().get_show_speed() + message_error

class PoliceCar(Car):
    pass

town_car = TownCar(140, 'Серая', 'Городская машина')
sport_car = SportCar(240, 'Красная', 'Спортивная машина')
work_car = WorkCar(60, 'Желтая', 'Рабочая машина')
police_car = PoliceCar(210, 'Синяя', 'Полицейская машина', True)

for car in Car._registry:
    print('Название: {}, цвет: {}, текущая скорость: {}, полицейская: {}'
          .format(car.name, car.color, car.speed, car.is_police))
print(work_car.get_show_speed())
print(sport_car.stop())
print(town_car.go())
print(police_car.turn('налево'))
