"""Ерошкина Ольга.DS_med 22.09, Практическое задание 7.
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
 Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def usage(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def usage(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def usage(self):
        return 2 * self.h + 0.3

    def total_usage(self, suits):
        i = 0
        for suit in suits:
            i += suit.usage
        return i

coat = Coat(10)
costume = Suit(2)
costume_2 = Suit(2.5)
costume_3 = Suit(3)
costume_4 = Suit(3.5)
costumes = [costume, costume_2, costume_3, costume_4]
print(coat.usage)
print(costume.usage)
print(costume.total_usage(costumes))




