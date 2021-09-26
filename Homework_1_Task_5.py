"""Ерошкина Ольга, группа DS 22.09
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

gain = float(input("Введите сумму выручки"))
expense = float(input("Введите сумму издержек"))
result = (gain-expense)
if result > 0:
    print("Ура! Фирма отработала с прибылью!")
    number_of_employees = int(input("Введите количество сотрудников"))
    print(number_of_employees)
    margin = (result / number_of_employees)
    print("Прибыль фирмы в расчете на одного сотрудника:", margin)
if result < 0:
    print("По результатам расчета выявлен убыток: издержки больше выручки!")
elif gain == expense:
    print("Фирма работает без прибыли")