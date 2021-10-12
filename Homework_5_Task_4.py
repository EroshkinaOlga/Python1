"""Ерошкина Ольга.DS_med 22.09, Практическое задание 5.
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

numbers_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('h5_t4_1234.txt') as file, open('new_numbers.txt', 'w') as new_numbers:
    file_lines = file.readlines()
    for line in file_lines:
        content = line.split()
        num_in_russian = numbers_dict.get(content[0])
        new_numbers.write(f'{line.replace(content[0], num_in_russian)}')