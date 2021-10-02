"""Ерошкина Ольга, DS_med 22.09, Практическое задание 2.
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
 Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове."""

user_text = input('Введите строку: ')
split_text = user_text.split()
for num, word in enumerate(split_text):
    print(f'{num+1}) {word[:10]}')



"""user_text = input('Введите строку: ')
split_text = user_text.split()
num = enumerate(split_text)
word = (split_text [:10])
print(f'{num}), {split_text}')"""
