"""Ерошкина Ольга, DS_med 22.09, Практическое задание 2.
 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
 Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict."""

user_month = input("Введите месяц по номеру от 1 до 12: ")
winter = 'Зима'
spring = 'Весна'
summer = 'Лето'
autumn = 'Осень'
month_season_dict = {'1': winter,'2':winter, '3':spring, '4':spring, '5':spring, '6':summer, '7':summer, '8':summer, '9':autumn, '10':autumn, '11':autumn, '12': winter}
print(month_season_dict[user_month])
seasons_list = [winter, winter, spring, spring, spring, summer, summer, summer, autumn, autumn, autumn, winter]
print(seasons_list[int(user_month) - 1])



""" предыдущая версия
my_month = input(list[1,2,3,4,5,6,7,8,9,10,11,12])
year_seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
year_seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
    print(year_seasons_dict.get(1))
    print(year_seasons_list[0])
    elif month == 3 or month == 4 or month ==5:
    print(year_seasons_dict.get(2))
    print(year_seasons_list[1])
    elif month == 6 or month == 7 or month == 8:
    print(year_seasons_dict.get(3))
    print(year_seasons_list[2])
    elif month == 9 or month == 10 or month == 11:
    print(year_seasons_dict.get(4))
    print(year_seasons_list[3])
    else:
        print("Такого месяца не существует")"""