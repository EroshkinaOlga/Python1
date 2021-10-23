"""Ерошкина Ольга.DS_med 22.09, Практическое задание 8.
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
 их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных."""

class Data:
    def __init__(self, date):
        # self.day = day
        # self.month = month
        # self.year = year
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []

        for i in date.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Корректная дата'
                else:
                    return f'Некорректное значение года'
            else:
                return f'Некорректное значение месяца'
        else:
            return f'Некорректное значение дня'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.date)}'


today = Data('23 - 10 - 2021')
print(today)
print(Data.valid(23, 10, 2023))
print(today.valid(23, 10, 2011))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(1, 11, 2000))