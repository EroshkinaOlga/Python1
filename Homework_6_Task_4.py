"""Ерошкина Ольга.DS_med 22.09, Практическое задание 6.
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

class Car:
    def __init__(self, speed, colour, name, is_police = False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go!')

    def stop(self):
        print('Stop!')

    def turn(self, direction):
        print(f'Совершен поворот: {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Внимание! Зафиксировано превышение скорости.')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Внимание! Зафиксировано превышение скорости.')

class PoliceCar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name, True)

town = TownCar(70, 'grey', 'Town')
sport = SportCar(200, 'yellow', 'Sport')
work = WorkCar(50, 'black', 'Work')
police = PoliceCar(110, 'white', 'Police')

town.show_speed()
work.show_speed()

work.speed = 30
work.show_speed()

police.turn('Left')


