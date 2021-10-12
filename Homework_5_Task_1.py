"""Ерошкина Ольга.DS_med 22.09, Практическое задание 5.
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
with open('h5t1_file_write.txt', 'w') as file:
    user_lines = input ('Enter your text: \n')
    while user_lines:
        file.write(f'{user_lines}\n')
        user_lines = input('Enter your text: \n')

