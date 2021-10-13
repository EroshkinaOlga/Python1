"""Ерошкина Ольга.DS_med 22.09, Практическое задание 5.
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('H5_t3_surnames_and_wage.txt') as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
average_sal = sum_salary / len(employees)
print(f'Average = {average_sal}\n')

for i, value in employees.items():
    if value < 20000:
        print(f'unlucky employee:')
        print(f'{i}:{value}\n')
