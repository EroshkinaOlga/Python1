"""Ерошкина Ольга, DS_med 22.09, Практическое задание 2.
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input()."""

band_list = input('Band names:')

split_band_list = band_list.split()

len_band_list = len(split_band_list)
element = 0
if element < len_band_list - 1:
    new_element = split_band_list[element]
    split_band_list[element] = split_band_list[element + 1]
    split_band_list[element + 1] = new_element
    element += 2
print(split_band_list)








"""Предыдущая версия 
random_list = input("Введите элементы списка: ").split(',')
random_list[:-1:2], random_list[1::2] = random_list[1::2], random_list[:-1:2]
print(random_list)"""