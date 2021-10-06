"""Ерошкина Ольга.DS_med 22.09, Практическое задание 3.
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу."""

"""def my_func_sum(nums_str, stop):
    user_list = nums_str.split(' ')
    sum_list = 0
    for i in user_list:
        if i == stop:
            break
        sum_list += int(i)

    return sum_list

stopper = 'st'
finished = False
s = 0
while not finished:
    nums_str_user = input("Введите числа через пробел:")
    s += my_func_sum(nums_str_user, stopper)
    finished = stopper in nums_str_user
    print(f"sum = {s}")"""


''' 
    result = 0
    n=int(input("введите числа: "))
    for n in args:
        result += n
    return my_func_sum(*args)
print("Сумма:", result)'''


'''def adder(*nums):
    sum = 0
    for n in nums:
        sum += n
return sum
    print("Sum: ", sum)'''

