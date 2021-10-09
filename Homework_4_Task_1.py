"""Ерошкина Ольга.DS_med 22.09, Практическое задание 4.
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

import sys

if len(sys.argv) < 4:
    print(f'Введите все данные')
else:
    hour = float(sys.argv[1])
    per_hour = float(sys.argv[2])
    extra = float(sys.argv[3])
    salary = hour * per_hour + extra
    print(salary)



