"""Ерошкина Ольга, группа DS 22.09
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

n = int(input("Введите число - "))
number_sum = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел:", number_sum)
