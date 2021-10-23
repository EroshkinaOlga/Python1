"""Ерошкина Ольга.DS_med 22.09, Практическое задание 8.
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""
class DivisionByNull:
    def __init__(self, numerator, denominator):
        self.divider = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_null(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f'Ошибка при попытке деления на ноль!')


print(DivisionByNull.divide_by_null(2, 0))
print(DivisionByNull.divide_by_null(0.1, 0.1))
print(DivisionByNull.divide_by_null(100, 0))