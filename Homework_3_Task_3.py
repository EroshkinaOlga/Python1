"""Ерошкина Ольга.DS_med 22.09, Практическое задание 3.
3.Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

num_1 = int(input('Введите число 1'))
num_2 = int(input('Введите число 2'))
num_3 = int(input('Введите число 3'))

def my_func(num_1, num_2, num_3):
    sum_num = num_1 + num_2 + num_3
    return sum_num - min(num_1, num_2, num_3)

result = my_func(num_1, num_2, num_3)
print(result)
