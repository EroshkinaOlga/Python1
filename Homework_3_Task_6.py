"""Ерошкина Ольга.DS_med 22.09, Практическое задание 3.
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
 Например, print(int_func(‘text’)) -> Text."""

txt = input("Введите текст: ")
def int_func(txt):
    line=txt.capitalize()
    return line
print(int_func(txt))
