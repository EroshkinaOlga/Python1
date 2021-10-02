"""Ерошкина Ольга, DS_med 22.09, Практическое задание 2.
 1. Создать список и заполнить его элементами различных типов данных.
 Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
 Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

my_random_list = ['Name', 'Surname',  25, 3.1415926535, True, (56,34,78,56), [23,56,58], {'band_name':1, 'Album_name':2}]
for i in my_random_list:
    print(type(i))



"""Предыдущая неудачная версия
my_random_list = ['Name', 'Surname',  25, 3.1415926535, True]
print(my_random_list)
print(type(my_random_list[0]))
print(type(my_random_list[1]))
print(type(my_random_list[2]))
print(type(my_random_list[3]))
print(type(my_random_list[4]))"""




