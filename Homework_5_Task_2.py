"""Ерошкина Ольга.DS_med 22.09, Практическое задание 5.
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""
with open('h5_t2_manually_created_file.txt', 'r') as file:
    lines_from_file = file.readlines()
    string_count = 0
    for i, item in enumerate(lines_from_file):
        string_count += 1
        words_count = len(item.split())
        print(f'#{i + 1} - {words_count} words')
    print(f'{string_count} lines')
