"""Ерошкина Ольга.DS_med 22.09, Практическое задание 6.
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return '{0} {1}'.format(self.name, self.surname)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

employee_object = Position('Helga', 'Pataki', 'poet', 50000, 10000)
print(employee_object.name)
print(employee_object.surname)
print(employee_object._income)
print(employee_object.get_full_name() )
print(employee_object.get_total_income() )

