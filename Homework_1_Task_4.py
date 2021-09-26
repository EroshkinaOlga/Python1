"""Ерошкина Ольга, группа DS 22.09
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции."""

a = int(input("Введите число:"))
m = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > m:
        m = a % 10
    if a != 0:
        continue
    else:
        print("Максимальное цифра в числе ", m)
        break

"""целочисленное деление и остаток от целочисленного деления цикл while
Пусть переменная a — заданное число, переменная m — максимальная цифра.
Предположим, что последняя цифра числа и есть максимальная. Извлечем ее с помощью операции нахождения остатка при делении на 10.
Поскольку последнюю цифру мы уже учли, то избавимся от нее с помощью операции деления нацело на 10.
Далее в цикле будем извлекать с конца числа каждую его цифру и сравнивать со значением m. Если очередная цифра больше, то будем присваивать ее переменной m.
Также в цикле надо избавляться от последней, уже учтенной, цифры. Цикл завершает свою работу, когда переменная a станет равной нулю, т. е. он работает, пока переменная a больше нуля.
В конце программы выведем значение m на экран. Это и будет наибольшая цифра исходного числа.
"""
